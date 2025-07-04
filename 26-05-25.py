# Take any 20 problems from loops and conditions and solve it in functions

# Print numbers from 1 to n
def fun(n):
    for i in range(1,n+1):
        print(i)
n=int(input("enter a number:"))
fun(n)

# Find the sum of numbers from 1 to n
def fun(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
n=int(input("enter a number:"))
print(fun(n))

# Print even numbers between 1 to n
def fun(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
n=int(input("enter a number:"))
fun(n)

# Check whether a number is positive, negative or zero
def fun(n):
    if n==0:
        print("zero")
    elif n>0:
        print("positive")
    else:
        print("negative")
n=int(input("enter a number:"))
fun(n)

# Find factorial of a number
def fun(n,fact=1):
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter a number:"))
print(fun(n))

# Count the number of digits in a number
def fun(n):
    count=0
    while n>0:
        digit=n%10
        count+=1
        n=n//10
    return count
n=int(input("enter a number:"))
print(fun(n))

# Check whether a number is prime
def fun(n):
    if n<=1:
        return "not prime"
    for i in range(2,n):
        if n%i==0:
            return "not prime"
    return "prime"
n=int(input("enter a number:"))
print(fun(n))

# Find the sum of digits of a number
def fun(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum
n=int(input("enter a number:"))
print(fun(n))

# Reverse a number
def fun(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
n=int(input("enter a number:"))
print(fun(n))

# Find the largest of three numbers
def fun(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
print(fun(a,b,c))

# Check whether a number is a palindrome
def fun(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if rev==n:
        return "palindrome"
n=int(input("enter a number:"))
print(fun(n))

# Print a multiplication table of a number
def fun(n):
    for j in range(1,11):
        print(n,"*",j,"=",n*j)
n=int(input("enter a number:"))
fun(n)



# Count number of vowels in a string

def fun(str):
    count=0
    for ch in str:
        if ch in "a e i o u":
            count+=1
    return count
str=input("enter a string:")
print(fun(str))
            

#  Find sum of even numbers between 1 to n
def fun(num):
    sum=0
    for i in range(num+1):
        if i%2==0:
            sum+=i
    return sum
num=int(input("enter a number:"))
print(fun(num))

# Print all prime numbers between 1 to 50
def fun():
    for num in range(2,51):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            print(num,end='')
fun()
     
# Find the GCD (HCF) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(gcd(a,b))
