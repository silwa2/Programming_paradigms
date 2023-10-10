'''
Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
'''


# Сортировка выборкой
def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for number in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = number
        # Этот цикл перебирает несортированные элементы
        for j in range(number + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[number], nums[lowest_value_index] = nums[lowest_value_index], nums[number]

if __name__ == "__main__":
    random_list_of_nums = [12, 8, 67, 34,  3, 20, 11]
    selection_sort(random_list_of_nums)
    random_list_of_nums.reverse()
    print(random_list_of_nums)
