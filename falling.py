#Промоделировать падения тела с заданными характеристиками (масса, форма) в различных плотных 
# средах. Изучитьвлияние плотности среды на характер движения. Скорость движения должна быть 
# достаточно велика, чтобы линейной составляющей силы сопротивления можно было пренебрегать 
# (на большей части пути). 

import math as m

m = float (input("Введите массу тела: "))
h = float (input("Введите высоту, с которой падает тело: "))

g = 9.8     #ускорение свободного падения
ro = 1.29   #плотность среды, в которой падает тело
c = 0.4     #коэффициент лобового сопротивления тела
S = 1       #площадь поперечного сечения тела
tau = 0.2   #шаг во времени

k2 = 0.5 * c * S *ro #коэффициент лобового сопротивления тела

x=[]    #расстояние
a=[]    #ускорение
t=[]    #время
v=[]    #скорость

x.append(0)
t.append(0)
v.append(0)
a.append(g)

i = 0   #счетчик для вычислений

# while x[i] != h:
#     t[i] = t[0] + i * tau
#     x[i] = x[i-1] + v[i-1] + a [i-1] * tau**2 / 2
#     v[i] = v[i-1] + a[i-1] * tau
#     a[i] = (m*g - k2 * v[i]) / 2
#     i += 1


i += 1
t.append(t[0] + i * tau)
v.append(x[i] / t[i])




x.append(x[i-1] + v[i-1] + a [i-1] * tau**2 / 2)
v.append(v[i-1] + a[i-1] * tau)
a.append((m*g - k2 * v[i]**2) / m)
print(x[i])
print(i)
        




#import math as m

#c = float (input("Введите коэффициент лобового сопротивления тела: "))
#S = float (input("Введите площадь поперечного сечения тела: "))
#m = float (input("Введите массу тела: "))
#h = float (input("Введите высоту, с которой падает тело: "))
#ro = float (input("Введите плотность среды, в которую падает тело: "))
#tau = float (input("Введите шаг во времени: "))

#k2 = 0.5 * c * S *ro #коэффициент лобового сопротивления тела
#g = 9.8 #ускорение свободного падения
#i = 0 #счетчик для вычислений

#while()