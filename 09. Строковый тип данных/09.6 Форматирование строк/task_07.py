'''
Используя метод format(), дополните приведённый ниже код так, чтобы он вывел текст:
In 2010, someone paid 10k Bitcoin for two pizzas.
'''

# example
s = 'In {0}, someone paid {1} {2} for two pizzas.'
print()

# solution
print(s.format(2010, '10k', 'Bitcoin'))