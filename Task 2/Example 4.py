a = int(input("Введите размер списка: "))
b = int(input("Введите номер первого элемента "))
c = int(input("Введите номер второго элемента "))
lst = list(range(-a, a+1))
mult = lst[b] * lst[c]
print(f'{lst} произведение элементов = {mult}')