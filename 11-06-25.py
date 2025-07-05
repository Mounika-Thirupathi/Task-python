
# 1.Rotate a string k no.of times from left to right and right to left
def fun(str,k):
    return str[k:]+str[:k]
str=input("enter a string:")
k=int(input("enter a number:"))
print(fun(str,k))   


# right rotate
def fun(str,k):
    return str[-k:]+str[:-k]
str=input("enter a string:")
k=int(input("enter a number:"))
print(fun(str,k))  