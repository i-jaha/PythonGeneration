'''
Используя f-строку, дополните приведённый ниже код так, чтобы он вывел текст:
In 2010, someone paid 10K Bitcoin for two pizzas.
'''

# example
s = 'In {}, someone paid {} {} for two pizzas.'
print()

# solution
print(s.format(2010, '10K', 'Bitcoin'))