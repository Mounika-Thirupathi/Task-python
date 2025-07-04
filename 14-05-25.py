# Solve problems on operators
# perform addition, subtraction, multiplication, division, and modulus operations.
def fun(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(fun(a,b))

# Take two numbers and check which one is greater, or if they are equal
def fun(a,b):
    if a>b:
        print("a greater than b ")
    elif a==b:
        print("a equal to b")
    else:
        print("a less than b")
a=int(input("enter a value:"))
b=int(input("enter b value:"))
fun(a,b)

# Check if a number is between 1 and 100
def fun(n):
    if n>0 and n<100:
        print("between 1 and 100")
    else:
        print("not present")
n=int(input("enter n value:"))
fun(n)

# Find bitwise AND, OR, and XOR of two numbers.
def fun(a,b):
    print(a&b)
    print(a|b)
    print(a^b)
a=int(input("enter a value:"))
b=int(input("enter b  value:"))
fun(a,b)

# Assign a value to a variable and update it using +=, -=, *=, /=
def fun(x):
    x+=5
    print(x)
    x-=5
    print(x)
    x*=5
    print(x)
    x/=5
    print(x)
x=int(input("enter a value:"))
fun(x)

# Check if a number is even or odd using a one-line ternary operator
def fun(x):
    res="even" if x%2==0 else "odd"
    return res
x=int(input("enter a value:"))
print(fun(x))

