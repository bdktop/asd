import re

pattern_old = r'^[А-Я]{3}[0-9]{3}$'
pattern_new = r'^[0-9]{4}[А-Я]{3}$'

def check_plate(plate):
    if re.match(pattern_old, plate):
        return "Старый формат"
    elif re.match(pattern_new, plate):
        return "Новый формат"
    else:
        return "Неверный формат"

def main():
    plate = input("Введите номерной знак машины: ").strip()
    result = check_plate(plate)
    print("Номерной знак соответствует:", result)
if __name__ == '__main__':
    main()