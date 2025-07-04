# Calculate the sum of digits of a number using a while loop.
# e.g., 123 → 6

def fun(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num=num//10
    return sum
num=int(input("enter a number:"))
print(fun(num))


# Reverse a number using a while loop.
# e.g., 123 → 321

def fun(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev
num=int(input("enter a number:"))
print(fun(num))


# Intermediate Level
# Check if a number is a palindrome using a while loop.
# e.g., 121 → Palindrome

def fun(num):
    rev=0
    temp=num
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
