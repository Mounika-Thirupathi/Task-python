# Print all numbers from 1 to N using a loop.
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i)
 
# Print all even numbers from 1 to N.
n=int(input("enter a number:"))
for i in range(2,n+1,2):
    print(i)
 
# Print all odd numbers from 1 to N.
n=int(input("enter a number:"))
for i in range(1,n+1,2):
    print(i)
 
# Calculate the sum of the first N natural numbers.
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=n*(n+1)//2
print(sum)
 
# Print the multiplication table of a given number up to 10
n=int(input("enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
 
 
 
 
 
# Count the number of digits in a given number.
n=int(input("enter a number:"))
count=0
while n>0:
    digit=n%10
    count+=1
    n=n//10
print(count)
   
# Reverse a given integer number.
num=input("enter a number:")
print(num[::-1])
 
# Check whether a number is a palindrome or not
n=input("enter a number:")
if n==n[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
 
# Check whether a number is a prime number.
n=int(input("enter a number:"))
if n<=1:
    print("not a prime:")
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
else:
    print("prime")
 
# Find the factorial of a number using a loop.
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
 
# Calculate the sum of digits of a given number.
n=int(input("enter a number:"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)
 
# Find the largest digit in a given number.
n=int(input("enter a number:"))
list=[]
while n>0:
    digit=n%10
    list.append(digit)
    n=n//10
print(list)
print(max(list))
 
 
 
 
 
 
# Find the smallest digit in a given number.
n=int(input("enter a number:"))
list=[]
while n>0:
    digit=n%10
    list.append(digit)
    n=n//10
print(list)
print("The Smallest Digit is:",min(list))
 
# Count how many times a given digit appears in a number.
n=int(input("enter a number:"))
target=int(input("enter a digit:"))
count=0
while n>0:
    digit=n%10
    if digit==target:
        count+=1
    n=n//10
print(count)
 
# Count the number of vowels in a string using a loop.
str=input("enter a string:")
count=0
for ch in str:
    if ch=="a" or ch=="e" or  ch=="i"  or ch=="o" or ch=="u":
        count+=1
print(count)
   
 
 
# Print characters in a string one by one using a loop.
str=input("enter a string:")
for ch in str:
    print(ch)
 
# Calculate a raised to the power b using a loop (without using **).
a=int(input("enter a value:"))
b=int(input("enter b value:"))
result=1
for _ in range(b):
    result*=a
print(result)
 
# Print the ASCII value of each character in a string.
str=input("enter a string:")
for char in str:
    print(ord(char))
 
#Check whether a number is an Armstrong number or not (3-digit).
num = input("Enter a number: ")
n = len(num)
total = 0
for digit in num:
    total += int(digit) ** n    
if total == int(num):
    print("Armstrong")
else:
    print("Not An Armstrong")
 
 
 
# Convert a lowercase character to uppercase using ASCII values in a loop.
str=input("enter a string:")
str2=""
for char in str:
    if 'a'<=char<='z':
        upper=chr(ord(char)-32)
        str2+=upper
    else:
        str2+=char
print(str2)
 
# Check if a string is a palindrome without using slicing or reversed.
str = input("Enter the string: ")
length = len(str)
for i in range(length // 2):
    if str[i] != str[length - i - 1]:
        print("False")
        break
else:
    print("True")
 
# Print the square of each number from 1 to N using a loop.
import math
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(round(math.sqrt(i),2))
 
# Find the GCD (Greatest Common Divisor) of two numbers using a loop.
a=int(input("enter a value:"))
b=int(input("enter b value:"))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)


















 
