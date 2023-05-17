import random
import matplotlib.pyplot as plt
import numpy as np

# Функция интенсивности потока заявок
def lambda_func(t):
    if t <= 50:
        return 0.2 * t
    else:
        return 0.5

# Функция интенсивности обслуживания
def mu_func(t):
    return (t - 100)**2/1000

# Определяем список моментов изменения состояния системы
time_points = []
t = 0
while t < 100:
    # Определяем момент изменения состояния по экспоненциальному распределению
    t += random.expovariate(lambda_func(t) + mu_func(t))
    # Добавляем момент в список
    time_points.append(t)

# Определяем количество заявок в накопителе на каждом моменте изменения состояния
queue_sizes = []
for t in time_points:
    # Определяем количество заявок в накопителе по геометрическому распределению
    p = lambda_func(t) / (lambda_func(t) + mu_func(t))
    k = np.random.geometric(p) - 1
    queue_sizes.append(k)


plt.plot(time_points, queue_sizes, 'bo-')
plt.xlabel('Время')
plt.ylabel('Количество заявок в накопителе')
plt.title('График изменения количества заявок в накопителе')
plt.show()
