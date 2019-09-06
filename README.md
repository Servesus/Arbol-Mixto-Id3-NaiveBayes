# Arbol-Mixto-Id3-NaiveBayes
## Versiones utilizadas:
python3
pandas 0.25.0
anytree 2.6.0

Los experimentos documentados en el paper se encuentran en el archivo test.py
Para usar los comandos que se indican a continuación basta con escribir en el terminal 
from arbol_mixto import ArbolMixto as a una vez se esta ejecutando python.

## Creación de un árbol
t = a()
## Entrenar un árbol
t.entrenar(False,"datasets/car-data-train.csv",5)
### Los parametros que recibe son:
	1º Boolean indicando si el csv tiene en la primera línea los nombres de los atributos
	2º Ruta del archivo, en caso de usar nuevos archivos se recomienda meterlos en la carpeta datasets
	3º Valor del quórum

## Visualizar el árbol creado
t.dibuja_arbol()
## Clasificar nuevos ejemplos
t.clasificar(False,"datasets/car-data-test.csv")
### Los parámetros que recibe son:
	1º Boolean indicando si el csv tiene en la primera línea los nombres de los atributos
	2º Ruta del archivo, en caso de usar nuevos archivos se recomienda meterlos en la carpeta datasets

## Calcular rendimiento
print(t.rendimiento())
