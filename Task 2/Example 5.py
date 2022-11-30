import random
lst = list(range(1, 6))
lst_2 = []
while len(lst_2) != len(lst):
    randitem = random.choice(lst)
    if randitem not in lst_2:
        lst_2.append(randitem)
print(f'{lst} \n{lst_2}')