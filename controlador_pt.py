# -*- coding: utf-8 -*-
"""ACA CUN: controlador propuesto para SBC-PT.

Logica comprobable en CPython; integracion con Packet Tracer PENDIENTE.
Copiar este archivo como main.py en un proyecto Python de SBC-PT.
No instalar paquetes con pip dentro de Packet Tracer.
"""


def inicial():
    return {"ac": 0, "luz": 0, "ventana": 0, "bloqueo": 1, "error": 0}


def entradas_iniciales():
    return {"ModoAuto": 1, "Ocupado": 1, "Noche": 0,
            "ACManual": 0, "LuzManual": 0, "VentanaManual": 0,
            "BloqueoManual": 1}


def bit(value):
    if value is True or value == 1 or str(value).lower() in ("1", "true"):
        return 1
    if value is False or value == 0 or str(value).lower() in ("0", "false"):
        return 0
    raise ValueError("Solo se admiten 0/1 o true/false")


def paso(temperatura, entradas, anterior):
    """Devuelve ordenes, NO confirmaciones del estado real de actuadores.

    Temperatura de demostracion domestica valida: 5 a 50 grados C.
    Noche y Ocupado son entradas manuales desde el panel, no sensores.
    """
    out = inicial()
    try:
        temp = float(temperatura)
        valido = 5.0 <= temp <= 50.0
    except (ValueError, TypeError):
        temp = 0.0
        valido = False
    out["error"] = 0 if valido else 1
    if not entradas["Ocupado"]:
        return out
    out["bloqueo"] = entradas["BloqueoManual"]
    if entradas["ModoAuto"]:
        out["luz"] = entradas["Noche"]
        if valido:
            if temp >= 28.0:
                out["ac"] = 1
            elif temp <= 25.0:
                out["ac"] = 0
            else:
                out["ac"] = anterior["ac"]
            out["ventana"] = 1 if (not out["ac"] and 24.0 <= temp <= 27.0) else 0
    else:
        out["luz"] = entradas["LuzManual"]
        out["ventana"] = entradas["VentanaManual"]
        out["ac"] = entradas["ACManual"] if valido else 0
    # Prioridad de interbloqueo: ventana abierta impide encender el AC.
    if out["ventana"]:
        out["ac"] = 0
    return out


def esquema():
    states = []
    for name in ("ModoAuto", "Ocupado", "Noche", "ACManual", "LuzManual",
                 "VentanaManual", "BloqueoManual"):
        states.append({"name": name, "type": "bool", "controllable": True})
    states.append({"name": "Temperatura", "type": "number", "unit": "C",
                   "decimalDigits": 1, "controllable": False})
    for name in ("OrdenAC", "OrdenLuz", "OrdenVentana", "OrdenBloqueo", "ErrorSensor"):
        states.append({"name": name, "type": "bool", "controllable": False})
    return {"type": "Controlador CUN", "states": states}


def reporte(temperatura, entradas, salida):
    return [entradas["ModoAuto"], entradas["Ocupado"], entradas["Noche"],
            entradas["ACManual"], entradas["LuzManual"], entradas["VentanaManual"],
            entradas["BloqueoManual"], temperatura, salida["ac"], salida["luz"],
            salida["ventana"], salida["bloqueo"], salida["error"]]


def ejecutar():
    from environment import Environment
    from ioeclient import IoEClient
    from time import sleep

    entradas = entradas_iniciales()
    salida = inicial()

    def recibir_estado(name, value):
        if name in entradas:
            try:
                entradas[name] = bit(value)
            except ValueError:
                print("Entrada rechazada: " + str(name))

    def recibir_todos(data):
        values = str(data).split(",")
        names = ["ModoAuto", "Ocupado", "Noche", "ACManual", "LuzManual",
                 "VentanaManual", "BloqueoManual"]
        if len(values) != 13:
            print("Paquete ignorado: numero de estados incorrecto")
            return
        pending = {}
        try:
            for i in range(7):
                pending[names[i]] = bit(values[i].strip())
        except ValueError:
            print("Paquete ignorado: valores de control invalidos")
            return
        for name in names:
            entradas[name] = pending[name]

    IoEClient.setup(esquema())
    # Seleccionar UNA via de recepcion segun soporte de la version instalada.
    try:
        IoEClient.onStateSet(recibir_estado)
    except AttributeError:
        IoEClient.onInputReceive(recibir_todos)

    print("Controlador iniciado. Ordenes aun NO verificadas en actuadores.")
    while True:
        try:
            temperatura = Environment.getMetricValue("Ambient Temperature")
        except Exception:
            temperatura = -999.0
        salida = paso(temperatura, entradas, salida)
        IoEClient.reportStates(reporte(temperatura, entradas, salida))
        print("T=" + str(temperatura) + " AC=" + str(salida["ac"]) +
              " Luz=" + str(salida["luz"]) + " Ventana=" + str(salida["ventana"]) +
              " Bloqueo=" + str(salida["bloqueo"]) + " Error=" + str(salida["error"]))
        sleep(1)


if __name__ == "__main__":
    ejecutar()
