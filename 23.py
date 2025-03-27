import math
def main():
    try:
        n=int(input("Введи кл-во сторон: "))
        s=float(input("Введи длина стороны: "))
    except ValueError:
        print("Ошибка: введи целочисленные значения.")
        return
    area=(n*s*s)/(4*math.tan(math.pi/n))
    print("Площадь правильного многоугольника: ", area)