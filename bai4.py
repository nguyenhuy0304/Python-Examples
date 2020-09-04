a = int(input("Nhập vào n = "))
f = 0                                         
s = 1  
                                       
if a<=0:
    print("Danh sách dãy fibonacci là:",f)
else:
    print("Danh sách dãy fibonacci là:", f, s, end=" ")
    for x in range(2, a):
        next_num = f + s                           
        print(next_num, end=" ")
        f = s
        s = next_num