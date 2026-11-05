"""Evidencia de laboratorio CPython: no ejecuta Packet Tracer ni red real."""
import contextlib
import hashlib
import importlib.util
import io
import json
import sys
import types
from pathlib import Path

ROOT=Path(__file__).resolve().parent
TARGET=ROOT/'controlador_pt.py'

def cargar(path):
    spec=importlib.util.spec_from_file_location('controlador_evaluado',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def assert_eq(actual, expected):
    if actual!=expected:
        raise AssertionError('obtenido='+repr(actual)+'; esperado='+repr(expected))

def simulacion_remota(module,commands):
    report=[]
    class StopLaboratorio(Exception): pass
    class IoEClient:
        @staticmethod
        def setup(api): assert len(api['states'])==13
        @staticmethod
        def onStateSet(callback):
            for name,value in commands: callback(name,value)
        @staticmethod
        def reportStates(states): report.append(states)
    class Environment:
        @staticmethod
        def getMetricValue(name): return 29
    def sleep(seconds): raise StopLaboratorio()
    old={name:sys.modules.get(name) for name in ('environment','ioeclient','time')}
    env=types.ModuleType('environment');env.Environment=Environment
    client=types.ModuleType('ioeclient');client.IoEClient=IoEClient
    timer=types.ModuleType('time');timer.sleep=sleep
    log=io.StringIO()
    try:
        sys.modules.update(environment=env,ioeclient=client,time=timer)
        with contextlib.redirect_stdout(log):
            try: module.ejecutar()
            except StopLaboratorio: pass
    finally:
        for name,value in old.items():
            if value is None: sys.modules.pop(name,None)
            else: sys.modules[name]=value
    assert len(report)==1
    return report[0],log.getvalue()

def casos(module):
    results=[]
    def run(id_,tipo,fn):
        try:
            detail=fn();results.append({'id':id_,'tipo':tipo,'estado':'APROBADO','detalle':detail})
        except Exception as e:
            results.append({'id':id_,'tipo':tipo,'estado':'FALLO','detalle':str(e)})
    def f01():
        entradas=module.entradas_iniciales();state=module.inicial();ac=[]
        for temp in (29,26,25):
            state=module.paso(temp,entradas,state);ac.append(state['ac'])
        assert_eq(ac,[1,1,0]);return 'T=[29,26,25]; AC='+repr(ac)
    def f02():
        e=module.entradas_iniciales();e.update(ModoAuto=0,ACManual=1,VentanaManual=1)
        r=module.paso(29,e,module.inicial());assert_eq((r['ac'],r['ventana']),(0,1))
        return 'Manual AC=1, ventana=1 -> orden AC=0, ventana=1'
    def s01():
        payloads=['<script>alert(1)</script>','1; abrir_puerta()','__import__("os")','-1','2','true,false']
        rejected=0
        for payload in payloads:
            r,log=simulacion_remota(module,[('ModoAuto',0),('ACManual',payload)])
            assert_eq(r[3],0);assert_eq(r[8],0)
            if 'Entrada rechazada: ACManual' not in log:raise AssertionError('falta registro de rechazo')
            rejected+=1
        return str(rejected)+'/'+str(len(payloads))+' valores invalidos rechazados; AC permanece apagado'
    def s02():
        r,log=simulacion_remota(module,[('ModoAuto',0),('OrdenAC',1),('OrdenBloqueo',0)])
        assert_eq(r[8],0);assert_eq(r[11],1)
        return 'Escrituras de OrdenAC/OrdenBloqueo ignoradas; salidas siguen AC=0, bloqueo=1'
    run('F01','Funcional',f01);run('F02','Funcional',f02)
    run('S01','Seguridad: validacion de entradas',s01);run('S02','Seguridad: estados de solo lectura',s02)
    return results

def main():
    source=TARGET.read_text();module=cargar(TARGET);results=casos(module)
    mutants=[]
    specs=[('M01','temp >= 28.0','temp >= 35.0'),('M02','if out["ventana"]:','if False:')]
    for id_,old,new in specs:
        assert old in source
        tmp=ROOT/('mutante_'+id_+'.py');tmp.write_text(source.replace(old,new,1))
        try:
            failures=[x['id'] for x in casos(cargar(tmp)) if x['estado']=='FALLO']
            mutants.append({'id':id_,'detectado':bool(failures),'casos_detectores':failures})
        finally:tmp.unlink()
    metrics=[
        {'nombre':'Efectividad funcional de la bateria','formula':'casos funcionales aprobados / ejecutados * 100','numerador':sum(x['estado']=='APROBADO' for x in results if x['tipo']=='Funcional'),'denominador':2,'unidad':'%'},
        {'nombre':'Rechazo de entradas invalidas en muestra','formula':'payloads rechazados / payloads invalidos * 100','numerador':6 if next(x for x in results if x['id']=='S01')['estado']=='APROBADO' else None,'denominador':6,'unidad':'%'},
        {'nombre':'Deteccion de mutaciones seleccionadas','formula':'mutantes detectados / mutantes creados * 100','numerador':sum(x['detectado'] for x in mutants),'denominador':len(mutants),'unidad':'%'}]
    for m in metrics:m['resultado']=None if m['numerador'] is None else m['numerador']/m['denominador']*100
    data={'entorno':'CPython; adaptador IoEClient simulado, sin Packet Tracer',
          'sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),'casos':results,'mutantes':mutants,'metricas':metrics}
    (ROOT/'resultados.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
    print(json.dumps(data,ensure_ascii=False,indent=2))
    if any(x['estado']!='APROBADO' for x in results):raise SystemExit(1)

if __name__=='__main__':main()
