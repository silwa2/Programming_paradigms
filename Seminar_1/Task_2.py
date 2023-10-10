'''
Задача №2
Написать точно такую же процедуру, но в декларативном стиле
'''

random_list_of_nums = [12, 8, 67, 34,  3, 20, 11]
print(f'Before sorting: {random_list_of_nums}')
random_list_of_nums.sort()

if __name__ == "__main__":
    random_list_of_nums.reverse()
    print(random_list_of_nums)