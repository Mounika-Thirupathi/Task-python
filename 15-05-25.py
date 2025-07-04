# Print Numbers from 1 to 10
def fun(n):
    for i in range(n+1):
        print(i)
n=int(input("enter a value:"))
fun(n)

# Using while loop
def fun(n):
    i=1
    while i<=n:
        print(i)
        i+=1
n=int(input("enter a value:"))
fun(n)


# Sum of First N Natural Numbers
def fun(n):
    return n*(n+1)//2
n=int(input("enter a value:"))
print(fun(n))
      
    #    Or
def fun(n,sum=0):
    for i in range(n+1):
        sum+=i
    return sum
n=int(input("enter a value:"))
print(fun(n))

# Factorial of a Number
def fun(n,fact=1):
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter n value:"))
print(fun(n))

# Reverse a Number
def fun(n):
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
n=int(input("enter n value:"))
print(fun(n))

# Print Even Numbers between 1 to 50
def fun():
    for i in range(2,51,2):
        if i%2==0:
            print(i)
fun()

# Check if a Number is Prime
def fun(n):
    if n<=1:
        return "not prime"
    for i in range(2,n):
        if n%i==0:
            return "not a prime"
    return "prime"
n=int(input("enter a number:"))
print(fun(n))

# Find Sum of Digits in a Number
def fun(n):
    sum=0
    while n!=0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum
n=int(input("enter a number:"))
print(fun(n))

# List all Multiples of a Number up to 100
def fun(n):
    for i in range(n, 101, n):
        print(i, end=" ")
n=int(input("enter a number:"))
fun(n)


# Print Fibonacci Series up to N terms
def fun(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b=b,a+b
n=int(input("enter n number:"))
fun(n)


# Print a Patter
# *
# * *
# * * *
# * * * *
def fun(n):
    for i in range(1,n+1):
        print("* "*i)
n=int(input("enter n number:"))
fun(n)
