popu1 = 80000
popu2 = 200000
t = 0


while popu1 < popu2:
    popu1 *= 1.03**t
    popu2 *= 1.015**t
    t += 1    

print(f'Em {t} anos as populações serão iguais')
print(popu1)
print(popu2)