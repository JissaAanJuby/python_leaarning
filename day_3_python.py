print("learnt about conditional statements and its use")

a= True
if a :
    print("python")

a= False
if a :
    print("python")
else:
    print("module")

#program to check whether  a person is minor or major
a= int (input("enter your age "))
if a< 18:
    print("you are a minor")
else:
    print("you are a major")

#program to check if a number inputted is positive or negative
a= int(input("enter your number"))
if a<0:
    print(a,"is negative")
else:
    print(a, "is positive")

#program to check biggest among two numbers
a= int(input("enter your first number "))
b= int(input("enter your second number"))
if a>b:
    print(a," is bigger ")
else:
    print(b," is bigger")


#program to check the smallest 
a= int(input("enter your first number "))
b= int(input("enter your second number "))
if a >b:
    print(b," is smallest ")
else:
    print(a," is smallest")

#program to check odd or even
a= int(input ("enter your number"))
if a%2 ==0:
    print(a, "is even")
else:
    print(a, "is odd")


#program if its a leap year
a = int(input ("enter the year"))
if a%4==0:
    print ("it is a leap year ")
else:
    print("it isnt a leap year")

#program to check your exam grade
a =int(input("enter your marks :"))
if a>90:
    print("A+")
elif a>80:
    print("A")
elif a>70:
    print("B+")
elif a>60:
    print("B")
elif a>50:
    print("C+")
else:
    print("failed")


#program to check which is largest among three numbers
a= int(input("enter your first number "))
b= int(input ("enter your second number "))
c=int(input("enter your third number"))
if a>b and a>c:
    print(a, "is the largest")
elif b>c:
    print(b, "is the largest")
else:
    print(c,"is the largest")


#examples for nested if
# program to check if largest among three numbers
a = int(input ("enter your first number "))
b= int (input ("enter your second number"))
c= int (input("enter your third number"))
if a>b:
    if a>c:
        print(a,"is the largest")
    else:
        print(c,"is the largest")
else:
    if b>c:
        print(b,"is the largest")
    else:
        print(c, "is the largest")


    


