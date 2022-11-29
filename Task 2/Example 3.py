n = int(input("Введите число "))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'{lst} | {sum(lst)}')