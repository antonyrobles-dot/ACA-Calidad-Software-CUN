# Laboratorio de calidad del controlador domótico

Proyecto académico en Python estándar. El controlador evaluado tiene SHA-256 `6d22c005477ccd280779ba8f72f70c0da579effb3bfdfe7e2cfcce0ade6f8274`.

## Reproducción

Desde esta carpeta: `python3 evaluar.py`. El comando escribe resultados.json y devuelve error si algún caso funcional o de validación falla. M01 y M02 se crean en copias temporales y se eliminan al terminar; no se altera el controlador original.

Se requieren Python 3 y permisos de escritura en la carpeta. No requiere instalar dependencias externas. No ejecutar datos o código de terceros para esta demostración.

## Evidencias

- F01: temperaturas 29, 26 y 25; órdenes de aire 1, 1 y 0.
- F02: simultaneidad manual aire/ventana; aire 0 y ventana 1.
- S01: seis entradas inválidas rechazadas; aire permanece apagado.
- S02: escrituras a estados de salida ignoradas.
- M01: umbral modificado a 35, detectado por F01.
- M02: interbloqueo desactivado, detectado por F02.

Las tres métricas usan denominadores explícitos: 2 casos funcionales, 6 entradas inválidas y 2 mutantes seleccionados. Los porcentajes no miden toda la seguridad, cobertura ni confiabilidad del sistema.

El adaptador IoEClient es un doble de laboratorio. Ningún resultado demuestra funcionamiento de WiFi ni de dispositivos de Packet Tracer; el proyecto de Redes es un entregable independiente.

## Acceso y estado de entrega

Repositorio público verificado: https://github.com/antonyrobles-dot/ACA-Calidad-Software-CUN . La entrega individual fue autorizada por el docente. La publicación del repositorio y del pitch fue indicada por el profesor.

El video personal todavía está pendiente de grabación. Debe durar como máximo cinco minutos, mostrar la ejecución real del evaluador y publicarse en YouTube con acceso público. Cuando exista, su enlace real se incorporará al informe y a este README. No se ha realizado la entrega definitiva del ACA de Calidad.

Consultar GUION_PITCH.md y README_ENTREGA.md. Esta carpeta contiene exclusivamente materiales técnicos, sin credenciales ni documentación administrativa personal.
