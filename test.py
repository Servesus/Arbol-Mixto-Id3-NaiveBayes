from arbol_mixto import ArbolMixto as a
from nodo import Nodo



"""
#Experimento 1

res = []
for i in range(1,7):
    t = a()
    t.entrenar(True,"datasets/ejemplo2.csv",i)
    t.clasificar(True,"datasets/evaluacion2.csv")
    rendimiento = t.rendimiento()
    res.append(rendimiento)
print(res)
"""
"""

#Experimento2
res = []
res2 = []
for i in range(1,40,2):
    t = a()
    t.entrenar(False,"datasets/car-data-train.csv",i)
    t.clasificar(False,"datasets/car-data-test.csv")
    rendimiento = t.rendimiento()
    res.append(rendimiento)
    res2.append(i)
print(res2)
print(res)
"""
#Experimento3
res = []
res2 = []
for i in range(1,40,2):
    t = a()
    t.entrenar(False,"datasets/kr-vs-kp-train.csv",i)
    t.clasificar(False,"datasets/kr-vs-kp-test.csv")
    rendimiento = t.rendimiento()
    res.append(rendimiento)
    res2.append(i)
print(res2)
print(res)
