# find the length of string without length method 
def fun(str):
    count=0
    for ch in str:
        count+=1
    return count
str=input("enter a string:")
print(fun(str))

# find the count of a's in a given input 
def fun(str):
    count=0
    for ch in str:
        if ch in "a":
            count+=1
    return count
str=input("enter a string:")
print(fun(str))

#  reverse a string 
def fun(str):
    return str[::-1]
str=input("enter a string:")
print(fun(str))  
#      or
def fun(str):
    res=""
    for ch in str:
        res=ch+res
    return res
str=input("enter a string:")
print(fun(str))
            
# find no of aeiou in a string
def fun(str):
    count=0
    for ch in str:
        if ch in "aeiou":
            count+=1
    return count
str=input("enter a string:")
print(fun(str))
            