'''
Good password
Напишите функцию is_password_good(password), 
которая принимает в качестве аргумента строковое значение пароля password 
и возвращает значение True, если пароль является надёжным, 
или False в противном случае.
Пароль является надёжным, если:
    его длина не менее 8 символов; 
    он содержит как минимум одну заглавную букву (верхний регистр); 
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.
Примечание. 
Приведённый ниже код:
    print(is_password_good('aabbCC11OP'))
    print(is_password_good('abC1pu'))
должен выводить:
    True
    False
'''

# # example
# # объявление функции
# def is_password_good(password):
#     pass

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))



# review
def is_password_good(password):
    if len(password) < 8:
        return False
    if not password.isalnum():
        return False
    if password.isupper() or password.islower() or password.isalpha() or password.isdigit():
        return False
    return True

txt = input()

print(is_password_good(txt))