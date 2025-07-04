# Solve the given programs
# chaitanya-> input 
# o/p -> aiaa

def fun(str):
    res=""
    for ch in str:
        if ch in 'aeiou':
            res+=ch
    return res
str=input("enter a string:")
print(fun(str))
 

# concat even positions in string chaitanya
def fun(str):
    res=""
    for i in range(len(str)):
        if i%2==0:
            res+=str[i]
    return res
str=input("enter a string:")
print(fun(str))

# # take two indexes and concat that part of indexes 
# # ex-> 1,4 -> chaitanya -> hai 
# 4  means -> 3
def fun(str):
    res=""
    for ch in range(1,4):
        res+=str[ch]
    return res
str=input("enter a string:")
print(fun(str))