from simplex import Simplex
import random



p = random.randint(-50, 50)
l = random.randint(-50, 50)
v = random.randint(-50, 50)
t = random.randint(-50, 50)

table = [[16, 19, 13, 17],
         [22, 27, 28, 24],
         [20, 29, 25, 21],
         [14, 18, 19, 15],
         [-3, -56, -50, 16]]

result = [0, 0]
S = Simplex(table)
table_result, result = S.calculate(result)

print("Решенная симплекс-таблица:")
for i in range(len(table_result)):
    for j in range(len(table_result[0])):
        print(f'{table_result[i][j]:.3f}', end=' ')
    print('\n')

print('Решение:')
print(f'X[1] = {result[0]:.3f}')
print(f'X[2] = {result[1]:.3f}')

print('Значение функции:')
print(10 * result[0] - 2 * result[1])