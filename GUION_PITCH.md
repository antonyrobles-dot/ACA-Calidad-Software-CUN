# Guion de sustentación y verificación de ACA

Actualizado el 5 de noviembre de 2026. Preparación; no constituye entrega.

## Calidad del Software: guion para grabar (máximo 5 minutos)

**0:00–0:35. Objetivo y alcance.**
Presento la evaluación de un controlador de automatización domótica en Python. El objetivo es comprobar dos comportamientos funcionales y dos controles de validación de entradas, y medir tres indicadores. El laboratorio utiliza CPython y un adaptador IoEClient simulado. No demuestra el funcionamiento de una red en Packet Tracer.

**0:35–1:25. Sistema y pruebas funcionales.**
El sistema decide órdenes de aire acondicionado, iluminación, ventana y bloqueo según entradas de usuario y temperatura. Primero mostraré F01: con temperaturas de 29, 26 y 25 grados, las órdenes de aire son uno, uno y cero. Esto comprueba la conservación del estado entre los umbrales de encendido y apagado. Después mostraré F02: cuando se solicitan simultáneamente aire y ventana en modo manual, la ventana tiene prioridad y la orden de aire queda apagada. Cada caso contrasta un resultado esperado con el obtenido.

**Acción de grabación:** abrir controlador_pt.py y señalar los umbrales y el interbloqueo. Ejecutar `python evaluar.py` desde la carpeta calidad. Mostrar F01 y F02 en la salida real.

**1:25–2:15. Validación de entradas.**
S01 introduce seis valores inválidos para el comando de aire y verifica su rechazo. S02 intenta escribir directamente estados de salida que deben ser de solo lectura. En este laboratorio se ignoran esas escrituras y las salidas siguen siendo calculadas por el controlador. Estos casos evalúan controles concretos; no equivalen a una auditoría completa de ciberseguridad ni comprueban la autenticación de una red real.

**Acción de grabación:** mostrar S01 y S02, y explicar el adaptador simulado sin llamarlo dispositivo físico o Packet Tracer.

**2:15–3:30. Métricas y prueba de sensibilidad.**
El primer indicador es el porcentaje de casos funcionales aprobados sobre ejecutados: dos sobre dos, multiplicado por cien, da cien por ciento. El segundo mide el rechazo de entradas inválidas: seis sobre seis, cien por ciento en esta muestra. El tercero mide detección de mutaciones seleccionadas: dos mutantes detectados sobre dos creados, cien por ciento. Para evaluar sensibilidad se cambia deliberadamente el umbral y se desactiva el interbloqueo en copias temporales. F01 detecta la primera alteración y F02 la segunda. Estos porcentajes describen esta batería pequeña; no prueban ausencia de defectos ni cobertura completa.

**Acción de grabación:** mostrar las tres fórmulas, numeradores, denominadores y resultados en resultados.json. Mostrar los dos mutantes detectados. Verificar que el SHA-256 del código original coincide con el informe.

**3:30–4:35. Análisis y conclusiones.**
Los resultados respaldan los comportamientos evaluados y muestran que los casos detectan dos defectos introducidos intencionalmente. Las limitaciones principales son el tamaño de la muestra y el uso de dobles para las interfaces del simulador. La siguiente fase es probar integración, comunicaciones y actuadores dentro de Packet Tracer. Una orden calculada no es una confirmación de que el dispositivo haya actuado. Por eso separo los resultados locales comprobados de la integración pendiente. Como mejora ampliaría las combinaciones de estados, los fallos de comunicación y la observación de actuadores.

**4:35–4:50. Cierre.**
El repositorio y el informe deben permitir reproducir estos resultados. Se incorporarán únicamente enlaces reales y los aportes de integrantes confirmados. El trabajo requiere equipo de tres a cinco estudiantes o autorización expresa para entrega individual.

**Pendiente real:** grabar, revisar duración máxima de cinco minutos, publicar con autorización, comprobar acceso al video y al repositorio e incorporar sus enlaces al PDF. Este archivo es un guion; no es un video grabado.

