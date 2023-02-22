
mark  = int(input("Enter Your Mark: "))
if mark >= 80 and mark <= 100:
    print("A+")
elif mark >= 70 and mark <= 79:
    print("A")
elif mark >= 60 and mark <= 69:
    print("A-")
elif mark >= 50 and mark <= 59:
    print("B+")
elif mark >= 40 and mark <= 33:
    print("C+")
else:
    print("F")
