#Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определи размер вклада через год.
#Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год в рублях и
# копейках. Дробная часть копеек отбрасывается.
p = int(input())
x = int(input())
y = int(input())
a = x * 100 + y
b = (a * (p + 100) /100)//100
print(b)