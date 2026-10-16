# Лабораторная работа №1
# Вариант 7. Результаты спортивных соревнований

# функция находит лучший результат
def find_best(results):
    return min(results)

# функция находит худший результат
def find_worst(results):
    return max(results)

# функция считает среднее арифметическое
def find_average(results):
    return sum(results) / len(results)

# функция возвращает трёх призёров
def find_prizers(results):
    sorted_list = sorted(results)
    return sorted_list[:3]

# ------------- основная часть программы -------------

print("Анализ результатов спортивных соревнований")

n = int(input("Введите количество спортсменов: "))

# проверка количества
while n <= 0:
    print("Ошибка! Количество не может быть отрицательным")
    n = int(input("Введите количество спортсменов: "))

results = []

# вводим результаты спортсменов
for i in range(n):
    r = float(input("Результат спортсмена " + str(i + 1) + ": "))
    # проверка результата
    while r <= 0:
        print("Ошибка! Результат должен быть положительным")
        r = float(input("Результат спортсмена " + str(i + 1) + ": "))
    results.append(r)

# считаем основные показатели
best = find_best(results)
worst = find_worst(results)
average = find_average(results)

# считаем сколько спортсменов лучше среднего
better = 0
for r in results:
    if r < average:
        better = better + 1

# призёры
prizers = find_prizers(results)

# ------------- вывод результатов -------------

print()
print("----------- Результаты -----------")
print("Всего спортсменов:", n)
print("Лучший результат:", best, "сек")
print("Худший результат:", worst, "сек")
print("Средний результат:", round(average, 2), "сек")
print("Выступили лучше среднего:", better, "чел.")

print()
print("Призёры соревнований:")
for i in range(len(prizers)):
    print("  " + str(i + 1) + " место:", prizers[i], "сек")

# текстовая характеристика группы
print()
if better == 0:
    print("Никто не показал результат лучше среднего")
elif better <= n / 2:
    print("Результат группы - средний")
else:
    print("Отличный результат! Большинство спортсменов выступили лучше среднего")