'''
ФИО
Напишите функцию print_fio(name, surname, patronymic), 
которая принимает три параметра:
    name – имя человека;
    surname – фамилия человека;
    patronymic – отчество человека;
а затем выводит на печать ФИО человека.
Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
'''

# example
# объявление функции
def print_fio(name, surname, patronymic):
    pass
# считываем данные
name, surname, patronymic = input(), input(), input()
# вызываем функцию
print_fio(name, surname, patronymic)


# review
def print_fio(name, surname, patronymic):
    print(surname.title()[0], name.title()[0], patronymic.title()[0], sep='')
name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)