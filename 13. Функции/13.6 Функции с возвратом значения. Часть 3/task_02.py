'''
Середина отрезка
Напишите функцию get_middle_point(x1, y1, x2, y2), 
которая принимает в качестве аргументов координаты концов отрезка 
(x1;y1) и (x2;y2)
и возвращает координаты точки являющейся серединой данного отрезка.
Примечание 1. 
Координаты середины отрезка с концами в точках (x1;y1) и (x2;y2) вычисляются по формуле:
((x1+x2)/2; (y1+y2)/2)
Примечание 2. 
Приведённый ниже код:
    print(get_middle_point(0, 0, 10, 0))
    print(get_middle_point(1, 5, 8, 3))
должен выводить:
    5.0 0.0
    4.5 4.0
'''

# # example
# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     pass

# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)




# review
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)