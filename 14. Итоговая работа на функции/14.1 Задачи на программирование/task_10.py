'''
Панграммы 🌶️
Панграмма – это фраза, содержащая в себе все буквы алфавита. 
Обычно панграммы используют для презентации шрифтов, 
чтобы можно было в одной фразе рассмотреть все глифы.
Напишите функцию is_pangram(text), 
которая принимает в качестве аргумента строку текста на английском языке 
и возвращает значение True, если текст является панграммой, 
или False в противном случае.
Примечание 1. 
Гарантируется, что введённая строка содержит только буквы английского алфавита и пробелы.
'''

# # example
# # объявление функции
# def is_pangram(text):
#     pass
# # считываем данные
# text = input()
# # вызываем функцию
# print(is_pangram(text))




# review
def is_pangram(text):
    text = text.lower()
    text = text.replace(' ', '')
    chars = set(text)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    if len(chars) == len(alphabet):
        return True
    else:
        return False
text = input()
print(is_pangram(text))