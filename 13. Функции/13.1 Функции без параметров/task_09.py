'''
Звёздный треугольник 1
Напишите функцию draw_triangle(), 
которая выводит звёздный прямоугольный треугольник с катетами, 
равными 10, в соответствии с образцом:
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
Для вывода треугольника используйте цикл for.
'''

# example
# объявление функции
def draw_triangle():
    pass
# основная программа
draw_triangle()  # вызов функции

# review
def draw_triangle():
    for i in range(1, 11):
        print('*' * i)
draw_triangle()