'''
Only even numbers
Напишите программу, которая считывает последовательность из 10 целых чисел 
и определяет, является ли каждое из них чётным или нет.
'''

count = 0
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        count += 1
if count == 10:
    print("YES")
else:
    print("NO")