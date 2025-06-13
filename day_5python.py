#learnt about looping conditional statements problems

#find biggest number among any 10 numbers
a=int(input("enter the first number:"))
big =a
for i in range(1,10):
    print("number:",i+1)
    a= int(input("enter your number:"))
    if a>big:
        big = a
print("the biggest number is : ",big)

#find the smallest among any 10 unmbers
a=int(input("enter your first number"))
small=a
for i in range (1,10):
    print("numbers:",i+1)
    a= int(input("enter your number:"))
    if small>a:
        small=a
print("the smallest number is ", small)

#find the smallest among any n numbers
n =int(input("enter the numbers to be compared : "))
a= int(input("enter the first number :"))
small= a
for i in range (1,n):
    print("numbers ",i+1)
    a=int(input("enter the next number :"))
    if small>a:
        small=a
print("the smallest number is ",small)

#find the biggest among any n numbers
n=int(input("enter the numbers to be compared:"))
a=int(input("enter the first number:"))
big = a 
for i in range(1,n):
    print("number:",i+1)
    a=int(input("enter your number: "))
    if big<a:
        big=a
print("the biggest number is : ", big)

#program to check the number of items purchased and then the same discount question as before
a=int(input("enter your number of items purchased:"))
sum =0
for i in range (1,a+1):
    print("item",i)
    p=int(input("enter the price: "))
    sum= sum+p
print("*********purchase details***********")
print("you purchased ",a,"number of items")
if sum>5000:
    print("you have a discount of 30%")
    c=sum*30/100
elif sum>3000:
    print("you have a discount of 20%")
    c=sum*20/100
elif sum>2000:
    print("you have a discount of 10%")
    c=sum*10/100
else:
    print("you have no discount ")
    c=0
print("you saved:",c)
print("amou tp be paid:",sum-c)


#program to calculate sum of odd or even numbers inputted
n=int(input("enter the numbers to be compared:"))
sum2=0
sum1=0
for i in range (1,n+1):
    print("number:",i)
    a=int(input("enter your number"))
    if a%2==0:
        sum2=sum2+a
    else:
        sum1=sum1+a
print("sum of the even numbers is ",sum2)
print("the sum of odd numbers is ",sum1)

#program to find the numbers even digits and odd digits in a numbers
n=int(input("enter the nunbers to be checked:"))
even=0
odd=0
for i in range (1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("the number of even digits:",even)
print("the number of odd digits:",odd)