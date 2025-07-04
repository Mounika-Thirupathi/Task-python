# Do practice of functions
# Write a function that takes two numbers and returns their sum.

def fun(a,b):
    return a+b
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(fun(a,b))

# Write a function that checks if a number is even or odd.
def fun(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=int(input("enter a number:"))
print(fun(num))

# Factorial of a number
def fun(num,fact=1):
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("enter a number:"))
print(fun(num))

# Find maximum of three numbers
def fun(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
print(fun(a,b,c))

#  Count number of vowels in a string
def fun(str):
    count=0
    for ch in str:
        if ch in 'a e i o u':
            count+=1
    return count
str=input("enter a string:")
print(fun(str))

# Check if number is prime
def fun(num):
    if num<=1:
        return "not prime"
    for i in range(2,num):
        if num%i==0:
            return "not prime"
    return "prime"
num=int(input("enter a number:"))
print(fun(num))
   
# Write a function to reverse a string without using built-in functions.
def fun(str):
    rev=""
    for ch in str:
        rev=ch+rev
    return rev
str=input("enter a string:")
print(fun(str))
    
# Write a function that takes a list as input and returns the sum of its elements.
def fun(l):
    sum=0
    for i in l:
        sum+=i
    return sum
l=list(map(int,input("enter a string:").split()))
print(fun(l))

# Write a function to print the first n numbers in the Fibonacci series.    
def fun(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b=b,a+b
 
n=int(input("enter a number:"))
fun(n)
