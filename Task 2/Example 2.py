num = int(input("Введите число "))
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)
    
list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"{list}")