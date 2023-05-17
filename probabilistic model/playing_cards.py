import random

# Создаем колоду из 36 карт
suits = ['черви', 'бубны', 'трефы', 'пики']
values = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
deck = []
for suit in suits:
    for value in values:
        deck.append(value + ' ' + suit)

# Выводим кол-во карт каждой масти
suit_counts = {suit:0 for suit in suits}
for card in deck:
    suit = card.split()[-1]
    suit_counts[suit] += 1
print(suit_counts)

# Моделируем выбор карты наугад
n = 1000  # количество карт, которые будут выбраны
suit_frequencies = {suit:0 for suit in suits}
for i in range(n):
    card = random.choice(deck)
    suit = card.split()[-1]
    suit_frequencies[suit] += 1

# Выводим относительную частоту выпадения каждой масти
for suit in suits:
    frequency = suit_frequencies[suit] / n
    print(f'Масть {suit}: {frequency:.2f}')

# Разделяем интервал на равные части
interval = [0, 0.25, 0.5, 0.75, 1]
interval_counts = [0] * (len(interval) - 1)
for i in range(n):
    r = random.random()
    for j in range(len(interval) - 1):
        if interval[j] <= r < interval[j+1]:
            interval_counts[j] += 1
            break

# Выводим количество карт в каждом интервале
for j in range(len(interval) - 1):
    count = interval_counts[j]
    print(f'Интервал [{interval[j]:.2f}, {interval[j+1]:.2f}): {count}')