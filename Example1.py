x = int(input("Nhap x = "))
y = int(input("Nhap y = "))

a = []

for i in range(0, x):
    a.append([])
    for j in range(0, y):
        z = int(input("Nhap phan tu thu a[%d][%d]: " % (i, j)))
        a[i].append(z)

print("Day so vua nhap la: ")
for i in range(0, x):
    for j in range(0, y):
        print("%3d " % a[i][j], end='')
    print()
