# Conditional statements

# Check if a number is positive, negative, or zero
def fun(n):
    if n==0:
        return "zero"
    elif n>0:
        return "positive"
    else:
        return "negative"
n=int(input("enter a number:"))
print(fun(n))

# Check if a number is even or odd
def fun(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
n=int(input("enter a number:"))
print(fun(n))

# Find the greatest of 3 numbers
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

# Check if a year is a leap year
def fun(year):
    if year%400==0 or year%4==0 and year%100!=0:
        return "leap"
    else:
        return "not leap"
year=int(input("enter a year:"))
print(fun(year))

# Grading system
def fun(grade):
    if grade>=80:
        return "A"
    elif grade>=70:
        return "B"
    elif grade>=60:
        return "c"
    else:
        return "F" 
grade=int(input("enter a grade:"))
print(fun(grade))

# Check whether a character is a vowel or consonant
def fun(str):
    for ch in str:
        if ch in "a e i o u A E I O  u":
            print("vowel")
        else:
            print("consonant")
str=input("enter a str:")
fun(str)

# Check eligibility to vote
def fun(age):
    if age>=18:
        return "eligible"
    else:
        return "not eligible"
age=int(input("enter a age:"))
print(fun(age))
