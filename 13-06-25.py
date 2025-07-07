# 1.Even or Odd Checker:
# Take an integer as input and print whether it's even or odd.
def fun(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=int(input("enter a number:"))
print(fun(num))

# 2.Sum of Digits:
# Given a number, find the sum of its digits (e.g., 123 ➝ 6).
def fun(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num=num//10
    return sum
num=int(input("enter a number:"))
print(fun(num))

# 3.Count Vowels in a String:
# Input a string and count how many vowels it contains.
def fun(str):
    count=0
    for ch in str:
        if ch in "aeiou":
            count+=1
    return count
str=input("enter a string:")
print(fun(str))

# 4.Check Palindrome:
# Check if a given string or number is a palindrome (same forward and backward).
def fun(num):
    temp=num
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if rev==num:
        return "palindrome"
    else:
        return "not palindrome"
num=int(input("enter a number:"))
print(fun(num))

# 5.Find Maximum in a List:
# Given a list of numbers, find and print the maximum number.
def fun(l):
    max_num=l[0]
    for i in l:
        if i>max_num:
            max_num=i
    return max_num
l=list(map(int,input("enter a list:").split()))
print(fun(l))

