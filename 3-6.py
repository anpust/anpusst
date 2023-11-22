list = [1, -2, 3, 0, 5, -6, 7, 0, 9,4,8]
suma=0
nombers_plus = len([x for x in list if x > 0])
index_of_zero = len(list) - list[::-1].index(0) - 1
for i in list[index_of_zero + 1:]:
    suma+=i


print("Количество положительных элементов:", nombers_plus)
print("Сумма элементов после последнего нуля:", suma)