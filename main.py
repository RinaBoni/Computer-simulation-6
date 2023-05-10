#!/usr/bin/env python3
# Поток простейший. Очередь отсутствует.

import random
import math

def setRo(data):
 data["ro"] = data["lambda"] / data["mu"]

def setP0(data):
 ro = data["ro"]
 if ro == 1:
    result = (1 - ro) / (1 - ro ** (data["m"] + 2))
 else:
    result = 1 / (data["m"] + 2)
 data["p0"] = result

def getP(data, k):
 return k * data["p0"]

def setP(data, k):
 name = "p" + str(k)
 data[name] = getP(data, k)

def setPotkaz(data):
 data["potkaz"] = getP(data, 1)

def setQ(data):
 data["q"] = 1 - data["potkaz"]

def setPsystem(data):
 data["psystem"] = 1 - data["potkaz"]

def setA(data):
 data["A"] = data["lambda"] * data["q"]

def setNochered(data):
 m = data["m"]
 ro = data["ro"]
 p0 = data["p0"]
 if m == 1:
    chislitel = ro * ro * (1 - (ro ** m) * (m + 1 - m * ro))
    znamenatel = (1 - ro ** (m - 2)) * (1 - ro)
    result = p0 * chislitel / znamenatel
 else:
    result = m * (m + 1) / (2 * m + 4)
 data["nochered"] = result

def setNobsl(data):
 data["nobsl"] = data["ro"] * data["q"]

def setNsystem(data):
 data["nsystem"] = data["nochered"] + data["nobsl"]

def setTochered(data):
    data["tochered"] = data["nochered"] / (data["lambda"] * data["psystem"])

def setTsystem(data):
    data["tsystem"] = data["nsystem"] / (data["lambda"] * data["psystem"])

# def setTochered(data):
#     if (data["lambda"] * data["psystem"]>0):
#         data["tochered"] = data["nochered"] / (data["lambda"] * data["psystem"])
#
# def setTsystem(data):
#     if(data["lambda"] * data["psystem"]>0):
#         data["tsystem"] = data["nsystem"] / (data["lambda"] * data["psystem"])

def setAllParams(data):
 setRo(data)
 setP0(data)
 setPotkaz(data)
 setQ(data)
 setPsystem(data)
 setA(data)
 setNochered(data)
 setNobsl(data)
 setNsystem(data)
 setTochered(data)
 setTsystem(data)

def printParam(name, value):
 print("{} \t: {}".format(name, value))

def printAllParams(data):
   printParam("Коэффициент использования объекта ", data["ro"])
   printParam("Вероятность того, что линия свободна ", data["p0"])
   printParam("Вероятность отказа в обслуживании ", data["potkaz"])
   printParam("Вероятность принятия заявки в систему ", data["q"])
   printParam("Относительная пропускная способность ", data["psystem"])
   printParam("Абсолютная пропусная способность ", data["A"])
   printParam("Среднее число заявок в очереди ", 0.0)
   printParam("Среднее число заявок в обслуживании ", data["nobsl"])
   printParam("Среднее число заявок в СМО ", data["nsystem"])
   printParam("Среднее время ожидания заявки в очереди ", 0.0)
   printParam("Среднее время пребывания заявки в системе", data["tsystem"])


# def printAllParams(data):
#  printParam("Коэффициент использования объекта ", data["ro"]/N)
#  printParam("Вероятность того, что линия свободна ", data["p0"]/N)
#  printParam("Вероятность отказа в обслуживании ", data["potkaz"]/N)
#  printParam("Вероятность принятия заявки в систему ", data["q"]/N)
#  printParam("Относительная пропускная способность ", data["psystem"]/N)
#  printParam("Абсолютная пропусная способность ", data["A"]/N)
#  printParam("Среднее число заявок в очереди ", data["nochered"]/N)
#  printParam("Среднее число заявок в обслуживании ", data["nobsl"]/N)
#  printParam("Среднее число заявок в СМО ", data["nsystem"]/N)
#  printParam("Среднее время ожидания заявки в очереди ", data["tochered"]/N)
#  printParam("Среднее время пребывания заявки в системе", data["tsystem"]/N)

# Исполнение


Tn = 100
t  = 0
N  = 0

data = {"lambda": 0.95, "tsred": 1, "mu": 1, "m": 0 ,"ro":0,"p0":0,"potkaz":0,
        "q":0,"psystem":0,"A":0,"nochered":0,"nobsl":0,"nsystem":0,
        "tochered":0,"tsystem":0}


while (t<=Tn):
    r = 0+random.random()*1.0
    temp = 0.2+0.01*math.fabs(t-60)
    data["lambda"]= temp
    if t<30:
        mu=0.7*temp
    else:
        mu=0.95
    data["mu"]= mu
    setAllParams(data)
    t+=data["ro"]
    N+=1
    #printAllParams(data)
    print("")

# setAllParams(data)
printAllParams(data)

