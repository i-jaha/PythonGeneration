'''
Искомый месяц 📅
Напишите функцию get_month(language, number), 
которая принимает на вход два аргумента language – язык ru или en 
и number – номер месяца (от 1 до 12 включительно) 
и возвращает название месяца на русском или английском языке.
'''

# # example
# # объявление функции
# def get_month(language, number):
#     pass
# # считываем данные
# lan = input()
# num = int(input())
# # вызываем функцию
# print(get_month(lan, num))




# review
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return lng_ru[number - 1]
    elif language == 'en':
        return lng_en[number - 1]
lan = input()
num = int(input())
print(get_month(lan, num))