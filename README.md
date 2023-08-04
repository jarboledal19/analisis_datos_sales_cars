## **Paso 1: Alcance del proyecto y captura de datos**
 **Identificar y recopilar los datos que usaras para tu proyecto**
- Se obtienen los datos desde la plataforma Kaggle Datasets.
- Este conjunto de datos contiene información sobre las ventas de automóviles de un concesionario en el transcurso de un año (2022-2023).
- Es un archivo .CSV con  2.500.000 registros.
- Con base a este, se analizaran las ventas a lo largo del tiempo y el desempeño de los vendedores.

**Explicar para qué casos de uso final deseas preparar los datos, por ejemplo: tabla de análisis, 
aplicación de fondo base de datos de fuentes de verdad  etc.**
- Monitoreo de ventas y comisiones por fecha.
- Identificación de tendencias de ventas por marca y modelo de auto.
- Análisis de rendimiento de ventas por vendedor.
- Analisis y seguimiento de ventas por cliente.

## **Paso 2: Explorar y evaluar los datos, el EDA**
- se carga el archivo .csv
- conteo total de registros
- se muestran las primeras filas del archivo
- A manera de ejercicio se analiza el campo 'car year', con el fin de filtrar los registros y trabajar con una copia del dataframe donde la antiguedad de los autos sea mayor o igual al 2013.
- Se analiza los valores unicos de cada columna
- se conulta la descripcio de los datos
- se valida los datos nulos
- se validan los registros duplicados

**Documentar los pasos necesarios para limpiar los datos, indicar que tipo de pasos se sugieren para la limpieza**

- Identificar y trata los valores faltantes en el DataFrame, eliminando filas con valores faltantes o imputar valores medios o medianos. (En este caso no hay valores faltantes)
- Identificar y eliminar las filas duplicadas del DataFrame(En este caso no hay filas duplicadas)
- Corregir o eliminar los datos inconsistentes, por ejemplo, datos negativos en una columna que debe de ser positiva.(En este caso no aplica).
- Convertir los tipos de datos que sean necesarios para el analisis ( en este caso se cambia el tipo de dato de la columna 'Date' , 'Sale Price' y 'Commission Earned').
- Se crean nuebas columnas: year, month con base a la fecha.
 -Para el analisis no se necesita la taza de porcentaje de la comision por lo que elimino el campo 'Commission Rate' 
 
 ## Paso 3: Definir el modelo de datos
**Trazar el modelo de datos conceptual y explicar por qué se eligió ese modelo**
https://github.com/jarboledal19/Prueba_Yohana_Arboleda/blob/main/Modelo_conceptual_cars_sale.jpg

Elegí este modelo de entidad-relación porque refleja claramente la estructura de los datos proporcionados y las relaciones entre ellos. La entidad Venta es el elemento central, que vincula vendedores, clientes y automóviles a cada venta específica. De esta manera, podemos rastrear qué vendedor realizó una venta, qué cliente compró el automóvil y qué automóvil se vendió en cada caso.

**Indique claramente los motivos de la elección de las herramientas y tecnologías para el proyecto.**

Python es el lenguaje sugerido en el proyecto además es un lenguaje muy popular para el análisis de datos y uno de los más demandados en el medio.
Pandas al serla libreria exclusiao de Python ayuda a que sus funciones para la manipulación de datos permita realizar la limpieza y transformación de datos de manera sencilla.
Jupyter Notebook proporciona un entorno interactivo que facilita la exploración y el análisis de datos paso a paso de datasets con gran volumen de datos. Además, permite documentar el proceso. .


**Proponga con qué frecuencia deben actualizarse los datos y por qué.**

- 	Creería que en este caso los datos deben de ser actualizados mensualmente, ya que lo que se quiere analizar es el comportamiento de las ventas  y el desempeño de los vendedores mes a mes; normalmente en este tipo de negocio se revisan las ventas y demás, basado en los cierres mensuales  y de ahí en adelante, es decir trimestral , semestral y anual.
## Paso 5: Completar la redacción del proyecto

**¿Cuál es el objetivo del proyecto?**
##### optimizar las estrategias de ventas y comisiones para maximizar las ganancias. Esto incluiría identificar los vendedores más exitosos, las marcas y modelos de automóviles más populares y fidelización de clientes.
- Identificar tendencias de ventas a lo largo del tiempo, lo que ayudaría a la empresa a planificar y ajustar sus operaciones y estrategias.
- Evaluar el rendimiento individual de los vendedores, identificando fortalezas y áreas de mejora para cada uno de ellos.
- identificar las tendencias de compras de los clientes, para generar estrategias de marketing personalizadas y fidelizacion de los clientes.

#####  ¿Qué preguntas quieres hacer?
1. ¿Total de ventas por mes y por año? 
2. ¿Total de comisiones pagadas por mes y por año? 
3. ¿Top 5 de los vendedores con mayores y menores ventas?
4. ¿ cual es la marca de auto mas vendida?
5.¿Cuáles son los modelos de autos más vendidos?
6. Con el fin de realizar campañas de mercadeo y de fidelizacion ¿ cual es el cliente que mas compra y su preferencia en marca de carro?

###**Incluya una descripción de cómo abordaría el problema de manera diferente en los siguientes escenarios:**
    
**Si los datos se incrementaran en 100X**

- **Capacidad de procesamiento:** se necesitaría contar con un hardware más potente o utilizar servicios en la nube con los que puedan manejar grandes volúmenes de datos, como Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP).

- **Muestreo aleatorio:** Si el tamaño de los datos se vuelve demasiado grande para trabajar de manera eficiente en un entorno local, se puede considerar realizar un muestreo aleatorio de los datos para obtener una muestra representativa y más manejable para el análisis.

- **Uso de tecnologías Big Data:** Si el volumen de datos es masivo y supera la capacidad de manejo de una sola máquina, se podría considerar el uso de tecnologías Big Data como Apache Hadoop o Apache Spark, que están diseñadas para procesar y analizar grandes conjuntos de datos distribuidos en clústeres de máquinas.

