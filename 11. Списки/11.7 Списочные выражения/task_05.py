'''
Используя списочное выражение, дополните приведённый ниже код так, 
чтобы получить список всех чисел-палиндромов от 100 до 1000 (включительно).
Результирующий список должен состоять из целых чисел.
'''

# example
palindromes = ...
print(palindromes)

# review 1
palindromes = [i for i in range(100, 1001) if i % 10 == i // 100]
print(palindromes)

# review 2
palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
print(palindromes)