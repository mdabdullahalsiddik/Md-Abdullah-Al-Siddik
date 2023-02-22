#1
a = "Md Abdullah Al Siddik"
print(a)

#2
a = "Md Abdullah "
b = "Al Siddik"
print(a+b)

#3
print("Md \n Abdullah \n Al \n Siddik")

#4
print("Md \nAbdullah \nAl \nSiddik")

#5
a = 3
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#6
Name = "Md Abdullah Al Siddik"
Age = 20
Deparment = "Computer Engeering"
GPA = 4.72
CGPA = 3.92
print("My name is "+Name)
print(Name+" is a ",Age," year old")
print(Name+" read in "+Deparment)
print(Name+" "+Deparment+" fist semester CGPA ",CGPA)

print("My name is ",Name)
print(Name," is a ",Age," year old")
print(Name," read in ",Deparment)
print(Name+" ",Deparment," fist semester CGPA ",CGPA)

#7
number1 = 20
number2 = 30
print(number1+number2)

Name1 = input("Enter Your Fist Name : ")
Name2 = input("Enter Your Secend Name : ")
Age = input("Enter Your Age : ")
print(Name1)
print(Name2)
print(Age)

Name3 = input("Enter Your Fist Name : ")
Name4 = input("Enter Your Secend Name : ")
Full_Name= Name3+Name4
print(Full_Name)

Number1 = input("Enter Your Fist Number : ")
Number2 = input("Enter Your Secend Number : ")
Sum = Number1+Number2
print(Sum)

Number3 = input("Enter Your Fist Number : ")
Number4 = input("Enter Your Secend Number : ")
Sum1 = int(Number3)+int( Number4)
print(Sum1)


Number5 = int(input("Enter Your Fist Number : "))
Number6 = int(input("Enter Your Secend Number : "))
Sum2 = Number5+Number6
print(Sum2)

#8
a = 2
b = 3
area1 =1/2*a*b
print(area1)

Base = float(input("Enter Your Base : "))
Height = float(input("Enter Your Height : "))
Area = 1/2*Base*Height
print(Area)

#9
from math import *
print(max(2,1))
print(min(4,3))
print(abs(+4))
print(abs(-4))
print(sqrt(25))
print(pow(2,3))
print(round(3.2))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))


#10
Number7 = 2
Number8 = 3
print(f"{Number7}+{Number8}={Number7+Number8}")

#11
print("Md Abdullah Al",end = " ")
print("Siddik")

#12
print(30>20)
print(30<20)
print(30>20)
print(30>=20)
#print(30=<20)
print(20<=30)
print(30==30)
print(30!=20)
print("Siddik"=="sid")
print("siddik"=="siddik")

#13
Mark = 90
if Mark >= 36:
    print("Pass")
if Mark <= 36:
    print("Fail")

mark = 20
if mark >=36:
    print("Pass")
else:
    print("Fall")

Number = 4
if Number/2 -- 0:
    print("Even")
else:
    print("Odd")


Mark2 = 35
if Mark2 >= 80:
    print("A+")
elif Mark2 >= 70:
    print("A")
elif Mark2 >= 60:
    print("A-")
elif Mark2 >= 50:
    print("B")
elif Mark2 >= 40:
    print("C")
elif Mark2 >= 36:
    print("D")
else:
    print("Fail")


Number11 = 45
Number12 = 12
Number13 = 13
if Number11 > Number12:
    if Number12 < Number13:
        print("Hi")
    else:
        print("Hello")
if Number11 > Number12:
    if Number12 > Number13:
        print("Hii")
    else :
        print("Helloo")

if Number11 < Number12:
    if Number12 > Number13:
        print("Hiii")
    else:
        print("Hellooo")
else:
    print("Welcome")
if Number11 < Number12:
    if Number12 > Number13:
        print("Yes")
else:
    print("Not")

if Number11 < Number12:
    if Number12 > Number13:
        print("YES")
else:
    if Number11 > Number12:
        print("YESS")
    if Number12 < Number13:
        print("YESSS")

if Number11 < Number12:
    if Number12 > Number13:
        print("YES")
else:
    if Number11 > Number12:
        print("YEeSS")
    elif Number12 < Number13:
        print("YEeSSS")


print(Number11 if Number11 > Number12 else Number13)
print(Number11 if Number11 < Number12 else Number13)

if Number11 > Number12 and Number12 > Number13:
    print(Number11)
elif Number11 > Number12 and Number12 < Number13:
    print(Number12)

x = 'i'
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    print("Vowel")
else:
    print("Consonant")

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

x = 1
while x <= 100:
    print(x)
    x = x + 2

n = int(input("Enter Your Lest Number : "))
Sum = 0
x = 1
while x <= n :
    Sum = Sum + x
    x = x + 1
print(Sum)
x = 1
while x <= 100:
    print(x)
    if x == 50:
        break
    x = x + 1


x = 1
while x <= 100:
    print(x)
    x = x + 1
    if x == 50:
        break

x = 1
while x <= 100:
    print(x)
    if x == 10:
        break
    x = x + 1


#x = 1
#while x <= 100:

    if x == 10:
        continue
    print(x)
    x = x + 1
#13
a = ["appal","banana","bol","bat"]
print(a)
print(a[2])
print(a[1:2])
print(a[1:3])
print(a[-1])
print("appal"in a)
print("doll"in a)
print(a + ["doll"])
print(a * 2)
print(len(a))
a.append("cat")
print(a)
a.insert(3,"c++")
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.pop()
print(a)
#a.clear()
print(a)
a2 = a.copy()
print(a2)
a3 = a.index("c++")
print(a3)
a.count("bol")
print(a)
a4 = a.count(b)
print(a4)
        
#14
Number14 = range(10)
print(Number14)
Number15 =list(range(10))
print(Number15)
Number16 = list(range(10))
print(Number16[9])
Number17 = list(range(2,9))
print(Number17)
Number18 = list(range(2,20,2))
print(Number18)


#15

"""Number19 = [10,20,30,40,50]
x = 0
while x <= 5:
    print(Number19[x])
    x = x + 1"""
Number20 = [1,5,10,15,20]
for x in Number20:
    print(x)

#16
# 1 + 2 + 3 +......+ n
Number21 = int(input("Enter Your Last Number : "))
sum = 0
for x in range(1,Number21+1,1):
    sum = sum + x
print(sum)

#2 + 4 + 6 +....+n
Number22 = int(input("Enter Your Last Number : "))
sum1 = 0
for x in range(2,Number22+1,2):
    sum1 = sum1 + x
print(sum1)

#1**2 + 2**2 + 3**2 +....+n**2
Number23 = int(input("Enter Your Last Number : "))
sum3 = 0
for x in range(1,Number23+1,1):
    sum3 = sum3 + x**2 #(sum3 = sum3 + x*x)
print(sum3)

#1 + 1/2 + 1/3 + 1/4 +.....+ 1/n
Number24 =int(input("Enter Your Last Number : "))
sum4 = 0
for x in range(1,Number24+1,1):
    sum4 = sum4 + x/2
print(sum4)

#16
Number25 = 5
for x in range(Number25):
    print(x * "*")
Number26 = 5
for x in range(Number26 + 1):
    print(x * "*")

Number27 = 5
for x in range( Number27 + 1):
    x = 2 * x - 1
    print(x * "*")

#17
from random import randint
for x in range(1,4):
    GustNumber = int(input("Enter Your Gust Number 1 to 10 : "))
    RandomNmuber = randint(1,10)
    if GustNumber == RandomNmuber:
       print("Win")
    else:
       print("Lost")
       print("Random Number : ",RandomNmuber)

