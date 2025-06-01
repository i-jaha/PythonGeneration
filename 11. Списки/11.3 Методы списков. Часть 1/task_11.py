'''
Суммы двух
На вход программе подаётся натуральное число n(n≥2). 
Затем поступают n целых чисел. 
Напишите программу, 
которая создаёт из указанных чисел список, 
состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и так далее).
'''

# option 1
n = int(input())
lst = []
if n >= 2:
    num1 = int(input())
    for i in range(n - 1):
        num2 = int(input())
        lst.append(num1 + num2)
        num1 = num2
print(lst)

# option 2
lst = []
for i in range(int(input())):
    lst.append(int(input()))
res = []
for i in range(len(lst) - 1):
    res.append(lst[i] + lst[i + 1])
print(res)