'''
Ревью кода-1
На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке). 
Нужно написать программу, которая выводит на экран 
количество неотрицательных чисел последовательности и их произведение. 
Если неотрицательных чисел нет, требуется вывести на экран «NO» (без кавычек). 
Программист торопился и написал программу неправильно.
'''

# example
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')

# review
count = 0
product = 1
for i in range(10):
    x = int(input())
    if x >= 0:
        product *= x
        count += 1
if count > 0:
    print(count)
    print(product)
else:
    print('NO')