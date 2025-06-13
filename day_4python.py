#learnt about for loops and the way its use
print("jissa")

for i in range(11):
    print("jissa")


for i in range (11):
    print(i,"jissa")

#start wuth index value 1
for i in range(1,11):
    print(i,"jissa")


#odd index values
for i in range (1,11,2):
    print(i,"jissa")


#even index values
for i in range (2,11,2):
    print(i,"jissa")


#program to print the values upto n
n=int(input("enter your input"))
for i in range (1,n+1):
    print(i)


#print odd n values
n= int(input("enter your input"))
for i in range (1,n+1):
    if i%2==1:
        print(i)
    



#print n even values
n= int(input ("enter your input"))
for i in range (1,n+1):
    if i%2==0:
        print(i)


#print odd numbers upto 20
for i in range (20):
    if i%2==1:
        print(i)


#print squares of numbers from 1 to 10
for i in range (1,11):
    print(i*i)


#program to write fibbonacci series
#0,1,1,2,3,5.....233
a=0
b=1
print(a)
print(b)
#for c in range (233): (cant use this coz it will get repeated 233 times)
c=0
while c<233:
    c=a+b
    print(c)
    a=b
    b=c


#program to print values from 1 to 10
i=1
while i<11:
    print(i)
    i=i+1


#program to print n odd numbers
n = int(input("enter your input"))
i=0
while i<n+1:
    if i%2==1:
        print(i)
    i=i+1

#program odd nos till 0 to 20
i=0
while i<20:
    if i%2==0:
        print(i)
    i= i+1



#find the sum of n natural numbers
n=int(input("enter your input"))
i=1
s=0
while i<n+1:
    s=s+i
    i=i+1
print("sum of ",n, "natural numbers is",s)

#using for loop
n=int(input("enter your input"))
s=0
for i in range (1,n+1):
    s=s+1
print(s)

#program to find the factorial of a number
n=int(input("enter your number"))
s=1
for i in range(1,n+1):
    s=s*i
print(s)


#using while loop to find factorial
n=int(input("enter your number"))
i-1
s=1
while i<n+1:
    s=s*i
    i=i+1
print(s)


# find factors of a number
n=int(input("enter your number :"))
for i in range (1,n+1):
    if n%i==0:
        print(i,"is a factor of ",n)



