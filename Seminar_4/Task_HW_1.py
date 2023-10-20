'''
Корреляция: Контекст Корреляция - статистическая мера,
используемая для оценки связи между двумя случайными величинами.
● Ваша задача Написать скрипт для расчета корреляции Пирсона
между двумя случайными величинами (двумя массивами).
Можете использовать любую парадигму, но рекомендую использовать функциональную,
т.к. в этом примере она значительно упростит вам жизнь.
● Формула корреляции Пирсона:
'''

import math


def pearson_correlation(array_1, array_2):
    """
    Расчет корреляции Пирсона между двумя массивами.

    Args:
     - array_1: первый массив значений
     - array_2: второй массив значений

    Return:
     - Корреляция Пирсона между массивами array_1 и array_2
    """

    # Проверка на то, что массивы одинаковой длины
    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    # Расчет среднего значения
    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array_1]) / float(len(array_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1, array_2)]) / float(len(array_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [30, 21, 3, 24, 45, 35, 70]
array_2 = [15, 45, 33, 119, 250, 6, 7]

correlation = round(pearson_correlation(array_1, array_2), 3)
print(f"Корреляция Пирсона: {correlation}")
