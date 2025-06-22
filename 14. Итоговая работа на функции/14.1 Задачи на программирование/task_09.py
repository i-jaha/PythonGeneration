'''
Магические даты ✨
Магическая дата – это дата, когда день, умноженный на месяц, 
равен числу, образованному последними двумя цифрами года.
Напишите функцию is_magic(date), 
которая принимает в качестве аргумента строковое представление корректной даты 
и возвращает значение True, если дата является магической, или False в противном случае.
'''

# # example
# # объявление функции
# def is_magic(date):
#     pass
# # считываем данные
# date = input()
# # вызываем функцию
# print(is_magic(date))




# review
def is_magic(date):
    date = date.split('.')
    if int(date[0]) * int(date[1]) == int(date[2]) % 100:
        return True
    else:
        return False
date = input()
print(is_magic(date))