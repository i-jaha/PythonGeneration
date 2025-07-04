'''
Is the Triangle Valid?
Напишите функцию is_valid_triangle(side1, side2, side3), 
которая принимает в качестве аргументов три натуральных числа, 
и возвращает значение True, 
если существует невырожденный треугольник со сторонами side1, side2, side3, 
или False в противном случае.
Примечание 1. 
С данной задачей мы уже сталкивались при изучении условного оператора.
Примечание 2. 
Приведённый ниже код:
    print(is_valid_triangle(2, 2, 2))
    print(is_valid_triangle(2, 3, 10))
    print(is_valid_triangle(3, 4, 5))
должен выводить:
    True
    False
    True
'''

# # example
# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     pass

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))



# review 1
def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False
a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))



# review 2
def is_valid_triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    return sides[0] + sides[1] > sides[2]
a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))