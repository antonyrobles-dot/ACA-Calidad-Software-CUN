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
Los resultados respaldan los comportamientos evaluados y muestran que los casos detectan dos defectos introducidos intencionalmente. Las limitaciones principales son el tamaño de la muestra y el uso de dobles para las interfaces del simulador. Estas pruebas locales no comprueban integración, comunicaciones ni actuadores dentro de Packet Tracer. Una orden calculada no es una confirmación de que un dispositivo haya actuado. El proyecto de Redes fue comprobado por el estudiante por separado; esta medición corresponde exclusivamente a la versión de código y al laboratorio de Calidad. Como mejora ampliaría las combinaciones de estados, los fallos de comunicación y la observación de actuadores.

**4:35–4:50. Cierre.**
El repositorio público permite consultar el código y reproducir los resultados. Presento el trabajo de manera individual, conforme a la autorización docente. El informe incluye los resultados, sus limitaciones y el enlace del repositorio. El enlace público de esta sustentación se incorporará después de grabarla.

**Pendiente real:** grabar, revisar duración máxima de cinco minutos, publicar con autorización, comprobar acceso al video y al repositorio e incorporar sus enlaces al PDF. Este archivo es un guion; no es un video grabado.


## Preparación de la grabación en Windows

1. Descargar los archivos desde el repositorio público: Code → Download ZIP. Extraerlos juntos en una carpeta.
2. Abrir la terminal en esa carpeta y ejecutar `py --version`. Si Python no está disponible, instalarlo con autorización del dueño del computador. No aceptar acuerdos personales en nombre de otra persona.
3. Abrir controlador_pt.py y resultados.json en el editor. Tener las siete diapositivas preparadas como apoyo; la demostración debe mostrar la terminal real.
4. Hacer un ensayo. Ejecutar `py evaluar.py` y localizar F01, F02, S01, S02 y los mutantes M01 y M02. Usar el resultado real; si aparece un error, corregirlo antes de grabar.
5. Grabar la pantalla con narración propia usando el grabador disponible. Ocultar correo, notificaciones y otros datos personales. Mostrar la ejecución durante la toma.
6. Seguir el guion de 4:50; comprobar que el archivo completo no supere cinco minutos, se escuche y permita leer los resultados.
7. Subir la grabación a YouTube desde la cuenta del estudiante con visibilidad Pública, conforme a la indicación docente. Evitar datos privados en título o descripción.
8. Copiar el enlace real, comprobar reproducción sin sesión y añadirlo al PDF y al README. No colocar un enlace de ejemplo ni declarar el video publicado antes de verificarlo.

## Límites de las afirmaciones

No atribuir estas pruebas a una red WiFi real. El evaluador utiliza dobles de laboratorio. No volver a construir ni modificar el proyecto de Redes para este pitch. No grabar ni firmar en nombre del estudiante. La grabación personal y la comprobación de su enlace siguen pendientes.
