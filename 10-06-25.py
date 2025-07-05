# 1. Print a specific part of a string without using slicing1. Print a specific part of a string without using slicing
def fun(str):
    str1=""
    for x in range(0,4):
        str1+=str[x]
    return str1
str=input("enter a string:")
print(fun(str))


# 2. Print the string to replace "is" with "si" without using replace method
def fun(str):
    result=""
    i=0
    while i<len(str):
        if str[i:i+2]=="is":
            result+="si"
            i+=2
        else:
            result+=str[i]
            i+=1
    return result
str=input("enter a string:")
print(fun(str))