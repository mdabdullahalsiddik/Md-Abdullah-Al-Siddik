#1
i = int(input("Enter Any Number : "))
for i in range(2,i + 1):
    for j in range(2, i - 1 ):
        if i%j == 0:
            break
    else:
         print(i)
#2
i = int(input("Enter Any Number : "))
for i in range(2,i + 1):
    for j in range(2, i ):
        if i%j == 0:
            break
    else:
         print(i)
i = int(input("Enter Any Number : "))
for j in range(2, i  ):
    print(j)
i = int(input("Enter Any Number : "))
for j in range(2, i - 1 ):
    print(j)

i = int(input("Enter Any Number : "))
for i in range(2,i + 1):
    for j in range(2, i - 1 ):
        print(j)

i = int(input("Enter Any Number : "))
for i in range(2,i + 1):
    for j in range(2, i ):
        print(j)

n = int(input("Enter Any Number: "))
for i in range(n,n+1):
    for j in range(1,11):
        y="*"
        z="="
        print(i,y,j,z,i*j)