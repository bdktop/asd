def main():
    try:
        days = int(input("Введите количество дней: "))
        hours = int(input("Введите количество часов: "))
        minutes = int(input("Введите количество минут: "))
        seconds = int(input("Введите количество секунд: "))
    except ValueError:
        print("Ошибка: введите целочисленные значения.")
        return
    total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
    print("Общее количество секунд:", total_seconds)

if __name__ == "__main__":
    main()