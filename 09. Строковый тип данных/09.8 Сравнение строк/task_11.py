"""
Строковые минимум и максимум
На вход программе подаётся последовательность строк,
каждая строка на отдельной строке.
Концом последовательности является слово «КОНЕЦ» (без кавычек).
При этом само слово «КОНЕЦ» не входит в последовательность,
лишь символизируя ее окончание.
Напишите программу, которая находит в данной последовательности
максимальную и минимальную строки (в лексикографическом порядке)
и выводит их в следующем формате:
    Минимальная строка ⬇️: <минимальная строка>
    Максимальная строка ⬆️: <максимальная строка>
На вход программе подаётся последовательность строк, каждая на отдельной строке.
Программа должна вывести текст в соответствии с условием задачи.
Не только у чисел мы можем находить максимум и минимум.
"""

text = input()
mn = "яя"
mx = "A"
while text != "КОНЕЦ":
    if text < mn:
        mn = text
    if text > mx:
        mx = text
    text = input()
print(f"Минимальная строка ⬇️: {mn}")
print(f"Максимальная строка ⬆️: {mx}")