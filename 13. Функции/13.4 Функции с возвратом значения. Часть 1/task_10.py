'''
Найти всех
Напомним, что 
строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. 
Проблема заключается в том, что данный метод не находит местоположение всех символов а.
Напишите функцию с именем find_all(target, symbol), 
которая принимает два аргумента: 
строку target и символ symbol 
и возвращает список, содержащий все местоположения этого символа в строке.
Примечание 1. 
Если указанный символ не встречается в строке, то следует вернуть пустой список.
Примечание 2. 
Приведённый ниже код:
    print(find_all('abcdabcaaa', 'a'))
    print(find_all('abcadbcaaa', 'e'))
    print(find_all('abcadbcaaa', 'd'))
должен выводить:
    [0, 4, 7, 8, 9]
    []
    [4]
'''

# example
# объявление функции
def find_all(target, symbol):
    pass

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))



# review
def find_all(target, symbol):
    symbol = symbol.lower()
    target = target.lower()
    result = []
    for i in range(len(target)):
            if target[i] == symbol:
                result.append(i)
    return result

s = input()
char = input()

print(find_all(s, char))