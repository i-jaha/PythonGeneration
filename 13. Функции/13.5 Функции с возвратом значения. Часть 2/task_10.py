'''
Змеиный регистр
Напишите функцию convert_to_python_case(text), 
которая принимает в качестве аргумента строку в «верблюжьем регистре» 
и преобразует его в «змеиный регистр».
Примечание 1. 
Почитать подробнее о стилях именования можно по ссылке.
Примечание 2. 
Приведённый ниже код:
    print(convert_to_python_case('ThisIsCamelCased'))
    print(convert_to_python_case('IsPrimeNumber'))
должен выводить:
    this_is_camel_cased
    is_prime_number
'''

# example
# объявление функции
def convert_to_python_case(text):
    pass
# считываем данные
txt = input()
# вызываем функцию
print(convert_to_python_case(txt))




# review
def convert_to_python_case(text):
    for i in text:
        if i.isupper():
            text = text.replace(i, '_' + i.lower())
            text = text.lstrip('_')
    return text
txt = input()
print(convert_to_python_case(txt))