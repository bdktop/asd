number = input("Введите целое четырехзначное число: ")
if len(number) != 4 or not number.isdigit():
    print("Ошибка: Введите корректное четырехзначное число.")
else:
    digits = [int(d) for d in number]
    total = sum(digits)
    expression = " + ".join(number)
    print(f"{expression} = {total}")