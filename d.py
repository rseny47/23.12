a = 4**2020 + 2**2017 - 15
n = 0
while a!=0:
    z = a % 2
    a = a//2
    if z == 1:
        n += 1
print(n)
