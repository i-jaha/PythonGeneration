'''
Звёздный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
    fill – символ заполнитель;
    base – величина основания равнобедренного треугольника;
а затем выводит его.
Гарантируется, что основание треугольника – нечётное число.
'''

# example
# объявление функции
def draw_triangle(fill, base):
    pass
# считываем данные
fill = input()
base = int(input())
# вызываем функцию
draw_triangle(fill, base)

# review
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        if i <= (base // 2 + 1):
            print(fill * i)
        else:
            print(fill * (base - i + 1))
fill = input()
base = int(input())
draw_triangle(fill, base)