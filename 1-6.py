S = input("Введите строчку: ")
count = 0
sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м','н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш','щ']
ln = len(S)
for i in range(len(S)):
    if S[i] in sogl:
        count += 1

print(round((count/ln)*100,1),'%')



