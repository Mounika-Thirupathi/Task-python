# 1.Write a program to print the sum of all even numbers between 1 and 100.
def fun():
    sum=0
    for i in range(1,101):
        if i%2==0:
            sum+=i
    return sum
print(fun())

# 2. Write a program that prints the first 10 powers of 2 using a loop.
def fun():
    for i in range(1,11):
        print(i**2)
fun()

# 3.Calculate the factorial of a number entered by the user.
def fun(n,fact=1):
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter a number:"))
print(fun(n))

# 4.Print the reverse of a given number (e.g., input 1234 → output 4321).
def fun(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
n=int(input("enter a number:"))
print(fun(n))

# 5. Count the number of digits in a given integer using a loop.
def fun(n):
    count=0
    while n>0:
        digit=n%10
        count+=1
        n=n//10
    return count
n=int(input("enter a number:"))
print(fun(n))

# 6. Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5.
def fun():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(i)
fun()

# 7. Without using multiplication, calculate a * b using addition and a loop.
def fun(a,b):
    result=0
    for i in range(b):
        result+=a
    return result
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(fun(a,b))

# 8.Print the sum of digits of a number entered by the user (e.g., 123 → 1+2+3 = 6).
def fun(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum
n=int(input("enter a value:"))
print(fun(n))

# 9. Write a loop to check if a number is a palindrome (number reads the same forwards and backwards).
def fun(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if rev==n:
        return "palindrome"
    else:
        return "not palindrome"
n=int(input("enter a value:"))
print(fun(n))

# 10.Write a program to find the highest digit in a given number.
def fun(n):
    count=[]
    while n>0:
        digit=n%10
        count.append(digit)
        n=n//10
    return max(count)
n=int(input("enter a number:"))
print(fun(n))

# 11. Write a program to check if a number is positive, negative, or zero.
def fun(n):
    if n==0:
        print("zero")
    elif n>0:
        print("positive")
    else:
        print("negative")
n=int(input("enter a number:"))
fun(n)

# 12.Write a program that takes a number and prints whether it is divisible by 2, 3, both, or neither.
def fun(n):
    if n%2==0 and n%3==0:
        print("both")
    elif n%2==0:
        print("divisible by 2")
    elif n%3==0:
        print("divisible by 3")
    else:
        print("neither")
n=int(input("enter a number:"))
fun(n)
        
# 13.Check if a number is a three-digit number using conditionals.
def fun(n):
    count=[]
    while n>0:
        digit=n%10
        count.append(digit)
        n=n//10
    if len(count)==3:
        return "yes"
    else:
        return "no"
n=int(input("enter a number:"))
print(fun(n))

# 14. Write a program to check whether a given number is a prime number.
def fun(n):
    if n<=1:
        return "not prime"
    for i in range(2,n):
        if n%i==0:
            return "not prime"
            break
    return "prime"
n=int(input("enter a number:"))
print(fun(n))

# 15.Write a program to find the largest of three numbers entered by the user using nested if-else.
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
            
# 16. Check if a year is a leap year or not.
def fun(year):
    if year%400==0 or year%4==0 and year%100!=0:
        return "leap"
    else:
        return "not leap"
year=int(input("enter a value:"))
print(fun(year))
            
# 17. Take an integer input and determine if it is even and greater than 50.
def fun(n):
    if n%2==0 and n>50:
        return "yes"
    return "no"
n=int(input("enter a value:"))
print(fun(n))

# 18. Write a program to classify a number as:
#  Less than 0: "Negative"
# * 0 to 9: "Single Digit"
# * 10 to 99: "Two Digits"
# * 100 and above: "Three or More Digits"
def fun(n):
    if n<0:
        print("negative")
    elif 0<n<=9:
        print("single digit")
    elif 10<n<=99:
        print("double digit")
    else:
        print("three or more digits")
n=int(input("enter a value:"))
fun(n)
        

# 19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square.
def fun(n):
    if n**2 >1000:
        print(n**2)
    else:
        print("no")
n=int(input("enter a value:"))
fun(n)

# 20. Take two integers as input and determine if one is a factor of the other.
def fun(a,b):
    if a%b==0:
        print("b is factor a")
    elif b%a==0:
         print("a is factor b")
a=int(input("enter a value:"))
b=int(input("enter b value:"))
fun(a,b)