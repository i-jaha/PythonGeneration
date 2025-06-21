'''
Конвертер километров
Напишите функцию convert_to_miles(km), 
которая принимает в качестве аргумента расстояние в километрах 
и возвращает расстояние в милях. 
Формула для преобразования: мили = километры * 0.6214.

print(convert_to_miles(1))
print(convert_to_miles(5))
print(convert_to_miles(10))
'''

# example
# объявление функции
def convert_to_miles(km):
    pass

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))



# review
def convert_to_miles(km):
    ml = km * 0.6214
    return ml

num = int(input())

print(convert_to_miles(num))