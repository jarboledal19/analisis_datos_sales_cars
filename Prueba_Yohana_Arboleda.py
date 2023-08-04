#!/usr/bin/env python
# coding: utf-8

# ## **Paso 1: Alcance del proyecto y captura de datos**
#  **Identificar y recopilar los datos que usaras para tu proyecto**
# - Se obtienen los datos desde la plataforma Kaggle Datasets.
# - Este conjunto de datos contiene información sobre las ventas de automóviles de un concesionario en el transcurso de un año (2022-2023).
# - Es un archivo .CSV con  2.500.000 registros.
# - Con base a este, se analizaran las ventas a lo largo del tiempo y el desempeño de los vendedores.
# 
# **Explicar para qué casos de uso final deseas preparar los datos, por ejemplo: tabla de análisis, 
# aplicación de fondo base de datos de fuentes de verdad  etc.**
# - Monitoreo de ventas y comisiones por fecha.
# - Identificación de tendencias de ventas por marca y modelo de auto.
# - Análisis de rendimiento de ventas por vendedor.
# - Analisis y seguimiento de ventas por cliente. 
# 

# ## Paso 2: Explorar y evaluar los datos, el EDA

# In[408]:


# Importar la biblioteca Pandas
import pandas as pd


# Cargar datos desde un archivo CSV
df = pd.read_csv('car_sales_data.csv')

# Crea una copia del DataFrame original para realizar modificaciones
df_copia = df.copy()  


# In[409]:


#total de registros
total_registro = len(df)
print('Total de registros data frame original:',total_registro)


# In[410]:


# Mostrar las primeras filas del archivo
print(df.head())


# A manera de ejercicio se analiza el campo 'car year', con el fin de filtrar los registros y trabajar con una copia del dataframe donde la antiguedad de los autos sea mayor o igual al 2013. 

# In[411]:


# contar valores del campo 'car year'
car_year_counts = df['Car Year'].value_counts()

# mostrar registros
print("Salesperson diferentes y sus recuentos:")
print(car_year_counts)


# Filtro por el campo 'Car Year' donde este sea mayor o igual al 2013, y seguire trabajando con dataframe : df_fil

# In[412]:


# Filtrar el DataFrame por el campo 'Car Year', >= 2013
df_fil = df[df['Car Year'] >= 2013].copy()

#imprimir total de registro
total_registro = len(df_fil)
print('Total de registros data frame:',total_registro)


# In[413]:


# información general sobre los datos
print('información general sobre los datos')
print(df_fil.info())


# In[414]:


# valores únicos en cada columna
print(' valores únicos en cada columna')
print(df_fil.nunique())


# In[415]:


# descripción de los datos 
print(df_fil.describe())


# In[416]:


# valores nulos en los campos
print('valores nulos')
print(df_fil.isnull().sum())


# In[417]:


# registros duplicados
print('Registros duplicados')
duplicates = df_fil[df_fil.duplicated(keep=False)]
print(duplicates)


# **Documentar los pasos necesarios para limpiar los datos, indicar que tipo de pasos se sugieren 
# para la limpiez**
# 
# - Identificar y trata los valores faltantes en el DataFrame, eliminando filas con valores faltantes o imputar valores medios o medianos. (En este caso no hay valores faltantes)
# - Identificar y eliminar las filas duplicadas del DataFrame(En este caso no hay filas duplicadas)
# - Corregir o eliminar los datos inconsistentes, por ejemplo, datos negativos en una columna que debe de ser positiva.(En este caso no aplica).
# - Convertir los tipos de datos que sean necesarios para el analisis ( en este caso cambiare el tipo de dato de la columna 'Date' , 'Sale Price' y 'Commission Earne
# s.
#  

# In[418]:


# Convertir la columna 'Date' al tipo de datos fecha
df_fil['Date'] = pd.to_datetime(df_fil['Date'])

# Convertir la columna 'Sale Price' a valores numéricos
df_fil['Sale Price'] = pd.to_numeric(df_fil['Sale Price'])

# Convertir la columna 'Commission Earned' a int
df_fil['Commission Earned'] = df_fil['Commission Earned'].astype(int)


print(df_fil.info())
print(df_fil.head())


# - Para el analisis necesito separar la fecha en año, mes y dia en columnas independientes.

# In[419]:


# Insertar las columnas 'Year', 'Month' y 'Day'
df_fil.insert(1, 'Year', df_fil['Date'].dt.year)
df_fil.insert(2, 'Month', df_fil['Date'].dt.month)
df_fil.insert(3, 'Day', df_fil['Date'].dt.day)

# Imprimir el DataFrame con las nuevas columnas
print(df_fil)


# - En este caso no necesito la columna 'Day' por lo que la elimino.
# - Para este analisis no necesitare la taza de porcentaje de la comision por lo que elimino  el campo 'Commission Rate'
# 

# In[420]:


# Eliminar la columna 'Day'
df_fil.drop(columns=['Day'], inplace=True)

# Eliminar la columna 'Car Year'
df_fil.drop(columns=['Commission Rate'], inplace=True)

# Columnas actualizadas
print(df_fil.columns)


# ## Paso 3: Definir el modelo de datos
# **Trazar el modelo de datos conceptual y explicar por qué se eligió ese modelo**
# ![modelo_conceptual](Modelo_conceptual_cars_sale.JPG)
# 
# Elegi este modelo de entidad-relación porque refleja claramente la estructura de los datos proporcionados y las relaciones entre ellos. La entidad Venta es el elemento central, que vincula vendedores, clientes y automóviles a cada venta específica. De esta manera, podemos rastrear qué vendedor realizó una venta, qué cliente compró el automóvil y qué automóvil se vendió en cada caso.
# 

# **Indique claramente los motivos de la elección de las herramientas y tecnologías para el
# proyecto.**
# 
# -	**Python** es el lenguaje sugerido en el proyecto además es un lenguaje muy popular para el análisis de datos y uno de los más demandados en el medio.
# -	**Pandas** al serla libreria  exclusiao de Python ayuda a que sus funciones para la manipulación de datos permita realizar la limpieza y transformación de datos de manera sencilla.
# -	**Jupyter Notebook** proporciona un entorno interactivo que facilita la exploración y el análisis de datos paso a paso de datasets con gran volumen de datos. Además, permite documentar el proceso.
# .
# 

# **Proponga con qué frecuencia deben actualizarse los datos y por qué.**
# 
# - 	Creería que en este caso los datos deben de ser actualizados mensualmente, ya que lo que se quiere analizar es el comportamiento de las ventas  y el desempeño de los vendedores mes a mes; normalmente en este tipo de negocio se revisan las ventas y demás, basado en los cierres mensuales  y de ahí en adelante, es decir trimestral , semestral y anual.
# 

# ## Paso 5: Completar la redacción del proyecto

# **¿Cuál es el objetivo del proyecto?**
# ##### optimizar las estrategias de ventas y comisiones para maximizar las ganancias. Esto incluiría identificar los vendedores más exitosos, las marcas y modelos de automóviles más populares y fidelización de clientes.
# - Identificar tendencias de ventas a lo largo del tiempo, lo que ayudaría a la empresa a planificar y ajustar sus operaciones y estrategias.
# - Evaluar el rendimiento individual de los vendedores, identificando fortalezas y áreas de mejora para cada uno de ellos.
# - identificar las tendencias de compras de los clientes, para generar estrategias de marketing personalizadas y fidelizacion de los clientes.
# 

# #####  ¿Qué preguntas quieres hacer?
# 1. ¿Total de ventas por mes y por año? 

# In[536]:


# ventas agrupadas año
ventas_total_año = df_fil.groupby(['Year'])['Sale Price'].sum().reset_index()
ventas_total_año.columns = ['año','total ventas']
# formato de miles
ventas_total_año['total ventas'] = ventas_total_año['total ventas'].apply('{:,.0f}'.format)

# ventas agrupadas por mes
ventas_total_mes = df_fil.groupby(['Year', 'Month'])['Sale Price'].sum().reset_index()
ventas_total_mes.columns = ['año','mes','total ventas']
# formato de miles
ventas_total_mes['total ventas'] = ventas_total_mes['total ventas'].apply('{:,.0f}'.format)

# mostrar registros
print("Total ventas por año:")
print(ventas_total_año)
print("Total ventas por mes:")
print(ventas_total_mes)


# 2. ¿Total de comisiones pagadas por mes y por año? 

# In[540]:


# comisiones pagadas por año
comision_total_año = df_fil.groupby(['Year'])['Commission Earned'].sum().reset_index()
comision_total_año.columns = ['año', 'comision total']

# formato de miles
comision_total_año['comision total'] = comision_total_año['comision total'].apply('{:,.0f}'.format)

# comisiones pagadas por mes 
comision_total_mes = df_fil.groupby(['Year', 'Month'])['Commission Earned'].sum().reset_index()
comision_total_mes.columns =['año','mes','comision total']
# formato de miles
comision_total_mes['comision total'] = comision_total_mes['comision total'].apply('{:,.0f}'.format)


# mostrar registros
print("total comisiones por año:")
print(comision_total_año)
print("total comisiones por mes:")
print(comision_total_mes)


# 3. ¿Top 5 de los vendedores con mayores y menores ventas?

# In[543]:


# Calcular el total de ventas por vendedor
ventas_vendedor = df_fil.groupby('Salesperson')['Sale Price'].sum().reset_index()
ventas_vendedor.columns = ['vendedor', 'total ventas']

# Contar el número de ventas por vendedor
cantidad_ventas_vendedor = df_fil['Salesperson'].value_counts().reset_index()
cantidad_ventas_vendedor.columns = ['vendedor', 'cantidad ventas']

# Unir las dos consultas en una sola tabla
resultados = pd.merge(cantidad_ventas_vendedor,ventas_vendedor, on='vendedor')

# ordenar ventas desc, obtener top5
top_5_mayores_ventas = resultados.sort_values(by='total ventas', ascending=False).head(5)
top_5_mayores_ventas['total ventas'] = top_5_mayores_ventas['total ventas'].apply(lambda x: '{:,.0f}'.format(x))

# ordenar ventas asc, obtener top 5
top_5_menores_ventas = resultados.sort_values(by='total ventas', ascending=True).head(5)
top_5_menores_ventas['total ventas'] = top_5_menores_ventas['total ventas'].apply(lambda x: '{:,.0f}'.format(x))

#mostrar registros
print("Top 5 vendedores con mayores ventas:")
print(top_5_mayores_ventas)

print("Top 5 vendedores con menores ventas:")
print(top_5_menores_ventas)


# 4. ¿ cual es la marca de auto mas vendida?

# In[544]:


# ventas totales por marca de automóvil
ventas_marca = df_fil.groupby('Car Make')['Sale Price'].sum().reset_index()
ventas_marca.columns =['marca carro','total ventas']
# ventas por marca de automóvil
conteo_ventas_marca = df_fil['Car Make'].value_counts().reset_index()
conteo_ventas_marca.columns = ['marca carro','cantidad ventas']

# unir las dos consultas en una sola tabla
resultados = pd.merge(conteo_ventas_marca,ventas_marca,on= 'marca carro')

#aplicar formato de miles
resultados['total ventas'] = resultados['total ventas'].apply('{:,.0f}'.format)
resultados['cantidad ventas'] = resultados['cantidad ventas'].apply('{:,.0f}'.format)

# mostrar registros
print(resultados)


# 5.¿Cuáles son los modelos de autos más vendidos?

# In[548]:


# ventas totales por marca y modelo de automóvil
ventas_modelo = df_fil.groupby(['Car Make', 'Car Model'])['Sale Price'].sum().reset_index()
ventas_modelo.columns = ['marca carro','modelo carro','total ventas']

# cantidad de ventas por marca y modelo de automóvil
cantidad_ventas_modelo = df_fil.groupby(['Car Make', 'Car Model'])['Sale Price'].count().apply(lambda x: '{:,.0f}'.format(x)).reset_index()
cantidad_ventas_modelo.columns = ['marca carro','modelo carro','cantidad ventas']

# unir las dos consultas en una sola tabla
resultados = pd.merge(ventas_modelo,cantidad_ventas_modelo, on = ['marca carro','modelo carro'] )

# ordenar ventas asc, obtener top 5
top_10_modelo = resultados.sort_values(by='total ventas', ascending=False).head(10).reset_index(drop=True)

#formato miles
top_10_modelo['total ventas'] = top_10_modelo['total ventas'].apply(lambda x: '{:,.0f}'.format(x))

#mostrar registros
print("Top 10 de modelos de autos mas vendidos")
print(top_10_modelo)


# 6. Con el fin de realizar campañas de mercadeo y de fidelizacion ¿ cual es el cliente que mas compra y su preferencia en marca de carro?

# In[558]:


# ventas totales por marca de automóvil
ventas_cliente = df_fil.groupby(['Customer Name','Car Make'])['Sale Price'].sum().reset_index()
ventas_cliente.columns = ['cliente','marca carro','total ventas']


top_10_ventas = ventas_cliente.sort_values(by='total ventas', ascending=False).head(10).reset_index()
#formato miles
top_10_ventas['total ventas'] = top_10_ventas['total ventas'].apply(lambda x: '{:,.0f}'.format(x))

# mostrar registros
print("Ventas ordenadas por marca de mayor a menor:")
print(top_10_ventas)


# ###**Incluya una descripción de cómo abordaría el problema de manera diferente en los siguientes escenarios:**
#     
# **Si los datos se incrementaran en 100X**
# 
# - **Capacidad de procesamiento:** se necesitaría contar con un hardware más potente o utilizar servicios en la nube con los que puedan manejar grandes volúmenes de datos, como Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP).
# 
# - **Muestreo aleatorio:** Si el tamaño de los datos se vuelve demasiado grande para trabajar de manera eficiente en un entorno local, se puede considerar realizar un muestreo aleatorio de los datos para obtener una muestra representativa y más manejable para el análisis.
# 
# - **Uso de tecnologías Big Data:** Si el volumen de datos es masivo y supera la capacidad de manejo de una sola máquina, se podría considerar el uso de tecnologías Big Data como Apache Hadoop o Apache Spark, que están diseñadas para procesar y analizar grandes conjuntos de datos distribuidos en clústeres de máquinas.
# 

# In[ ]:




