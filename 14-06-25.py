# 1.Reverse a String Without Using [::-1]:
# Reverse a string using a loop or recursion.
def fun(str):
    rev=""
    for ch in str:
        rev=ch+rev
    return rev
str=input("enter a string:")
print(fun(str))

# 2.Count Frequency of an Element in a List:
# Input a list and an element; count how many times the element appears.
def fun(l,e):
    count=0
    for i in l:
        if i==e:
            count+=1
    return count
l=list(map(int,input("enter a list:").split()))
e=int(input("enter a element:"))
print(fun(l,e))

# 3.Remove Duplicates from a List:
# Given a list, return a new list without duplicates (maintain order).
def fun(l):
    seen=[]
    for i in l:
        if i not in seen:
            seen.append(i)
    return seen
l=list(map(int,input("enter a list:").split()))
print(fun(l))


# 4.FizzBuzz:
# For numbers from 1 to N, print:

# “Fizz” if divisible by 3

# “Buzz” if divisible by 5

# “FizzBuzz” if divisible by both

# Else print the number itself.


def fun(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            return "FizzBuzz"
        elif i%3==0:
            return "fizz"
        elif i%5==0:
            return "buzz"
n=int(input("enter a number:"))
print(fun(n))
