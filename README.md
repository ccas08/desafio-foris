# Attendance Tracker

## Introducción

Este proyecto procesa un archivo de entrada para detectar a los estudiantes que más asisten a clases. Se proporcionan comandos `Student` y `Presence` para registrar estudiantes y sus presencias en la universidad. El programa genera un reporte que lista cada estudiante con el total de minutos registrados y la cantidad de días que asistió, ordenado por la cantidad de minutos de mayor a menor.

## Decisiones de Diseño

### Modelamiento del Problema

Para modelar el problema, he creado tres clases principales:

1. **Student**: Representa a un estudiante y maneja sus registros de presencia.
2. **Presence**: Representa la presencia de un estudiante en la universidad en un día específico.
3. **AttendanceTracker**: Clase principal que maneja el registro de estudiantes y presencias, y genera el reporte.

Opté por utilizar clases para encapsular la lógica relacionada con estudiantes y presencias, lo que facilita la extensión y el mantenimiento del código.

### Estructura del Código

El código está estructurado en tres clases principales para mantener la separación de responsabilidades:

- **Student**: Maneja la lógica relacionada con los estudiantes, como agregar presencias y calcular el total de minutos y días asistidos.
- **Presence**: Encapsula los detalles de la presencia de un estudiante, incluyendo el cálculo de la duración de la presencia.
- **AttendanceTracker**: Coordina el registro de estudiantes y presencias, y genera el reporte final.

### Enfoque al Testing

He implementado pruebas unitarias utilizando el módulo `unittest` de Python. Las pruebas verifican:

1. La correcta adición de estudiantes.
2. La correcta adición de presencias.
3. La generación correcta del reporte.
4. La correcta lectura y procesamiento de un archivo de entrada.

### Uso de Idioms y Prácticas Propias del Lenguaje

- Uso de Sets para Evitar Duplicados.
- Comprensiones de Generadores.
- Uso de Clases y Objetos.
- Utilización de `datetime` para manejar y calcular tiempos de manera precisa.
- Uso de listas y conjuntos para almacenar presencias y días asistidos.
- Métodos Encapsulados.


### Conclusión
Este proyecto cumple con los criterios de evaluación al abordar el problema de seguimiento de asistencia de manera estructurada y clara. Utilicé clases para representar los datos y operaciones relacionados con estudiantes y sus presencias, lo que facilita la extensión y mantenimiento del código. El código está organizado de manera modular: cada clase tiene responsabilidades claras, con Student manejando los datos de los estudiantes, Presence encapsulando la información de presencia y su duración, y AttendanceTracker coordinando el registro y reporte de estos datos.

Implementé pruebas unitarias utilizando el módulo unittest de Python para verificar la correcta adición de estudiantes y presencias, así como la generación precisa del reporte final. Las pruebas también incluyen impresiones del reporte para confirmación visual.

En cuanto al uso de idioms y prácticas propias del lenguaje, utilicé datetime para manejar y calcular tiempos, asegurando precisión. También empleé listas y conjuntos para almacenar presencias y días asistidos, aprovechando sus eficiencias. Utilicé sort con una función lambda para ordenar los resultados del reporte de manera clara y concisa, y empleé el manejo de archivos con with open para asegurar la correcta gestión de recursos y evitar fugas de memoria.

En resumen, el proyecto demuestra un enfoque bien estructurado y detallado para resolver el problema del seguimiento de asistencia. La implementación es clara, fácil de mantener y extensible, siguiendo las mejores prácticas de Python.