mas =input().split(' ')
min_x = int(mas[0])
for i in mas:
    if int(i)<min_x:
        min_x = int(i)
print(min_x)