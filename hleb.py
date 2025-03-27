regular_price = 3.49

discounted_price = regular_price * 0.40

quantity = int(input("Введите количество приобретенных вчерашних буханок хлеба: "))

total_cost = discounted_price * quantity

print(f"{'Обычная цена за буханку:':30} {regular_price:10.2f}")
print(f"{'Цена со скидкой:':30} {discounted_price:10.2f}")
print(f"{'Общая стоимость приобретенного хлеба:':30} {total_cost:10.2f}")