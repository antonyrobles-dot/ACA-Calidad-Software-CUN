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

El adaptador IoEClient es un doble de laboratorio. Ningún resultado prueba funcionamiento de WiFi o dispositivos de Packet Tracer. El guion de pitch está preparado; el video no está grabado. Repositorio privado: https://github.com/antonyrobles-dot/ACA-Calidad-Software-CUN . Su consulta requiere permiso explícito; el enlace por sí solo no da acceso al profesor. No se cambia la visibilidad ni se invitan colaboradores sin autorización. Esta carpeta contiene únicamente materiales técnicos sin datos personales sensibles.
