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




#checking a if a num is positive , negative or zero
a= int(input("enter your number"))
if a!=0:
    if a<0:
        print("the number is negative")
    else:
        print("the number is positive")
else:
    print("thr number is zero")



#checking if a letter is vowel or consonant
a= input("enter your letter")
if a=="A" or a=="a":
    print("your letter is a vowel ")
elif a=="E" or a== "e":
    print("your letter is a vowel")
elif a=="I" or a=="i":
    print("your letter is a vowel")
elif a=="o" or a=="O":
    print("your letter is a vowel")
elif a=="u" or "U":
    print("your letter is a vowel")
else:
    print("your letter is a consonant")


#program to give a discount for purchased amount
#less than 5k then 30%
# less than 3k then 20%
# less than 1k then 10%
# else no discounts

a= int(input("enter your purchased amount"))
if a<5000:
    print("you have a discount of 30%")
    c= a*30/100
elif a<3000:
    print("you have discount of 20%")
    c= a*20/100
elif a<1000:
    print("you have a discount of 10%")
    c=a*10/100
else:
    print("you have no discounts ")
    c=0
print("**********purchased details************")
print("your purchased amount is", a)
print("your saved",c)
print("your payment is",a-c)


#write  a program to menu driven option for a mathematical operation 

a= int(input("enter your first number "))
b= int(input("enter your second number "))
c= int(input("1)sum\n2)difference\n3)product\n4)division\nenter your choice"))
if c==1:
    print("your sum is ",a+b)
elif c==2:
    print("your difference is ",a-b)
elif c==3:
    print("your product is", a*b)
elif c==4:
    print("your quotient is", a/b)
else:
    print("invalid choice")



#program to check area if radius is greater than 20 else take perimeter perimeter 
a= int(input("enter radius "))
if a>20:
    print("area is ",3.14*a*a)
else:
    print("perimeter is ",2*3.14*a)


#example of identity operator 
a=2
b=3
d=2
print(a is b)
print(a is not d)


#example of membership operator
a="jissa"
if "j" in a:
    print("j in jissa")
else:
    print("j is not in jissa")
