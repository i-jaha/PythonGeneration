'''
Три города
Даны названия трёх городов. 
Напишите программу, которая определяет самое короткое и самое длинное название города.
'''

city1 = input()
city2 = input()
city3 = input()
min_city = min(len(city1), len(city2), len(city3))
max_city = max(len(city1), len(city2), len(city3))
if len(city1) == min_city:
    print(city1)
elif len(city2) == min_city:
    print(city2)
else:
    print(city3)
if len(city1) == max_city:
    print(city1)
elif len(city2) == max_city:
    print(city2)
else:
    print(city3)