import random

def insert_numbers_in_list() -> list:
    quantity = int(input("Ingresa la cantidad de datos aleatorios a ingresar dentro de la lista:"))
    numbers = []
    for number in range(quantity):
        number = random.randint(1,quantity)
        numbers.append(number)
    return numbers