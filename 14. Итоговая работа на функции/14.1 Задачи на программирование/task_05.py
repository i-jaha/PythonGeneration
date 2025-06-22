'''
Калькулятор доставки 🛵
Интернет-магазин осуществляет экспресс доставку для своих товаров 
по цене 1000 рублей за первый товар и 120 рублей за каждый последующий товар. 
Напишите функцию get_shipping_cost(quantity), 
которая принимает в качестве аргумента натуральное число quantity – 
количество товаров в заказе – 
и возвращает стоимость доставки.
'''

# # example
# # объявление функции
# def get_shipping_cost(quantity):
#     pass
# # считываем данные
# n = int(input())
# # вызываем функцию
# print(get_shipping_cost(n))




# review
def get_shipping_cost(quantity):
    return 1000 + ( quantity - 1 ) * 120
n = int(input())
print(get_shipping_cost(n))