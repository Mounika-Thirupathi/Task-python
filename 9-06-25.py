# 1.Take a string print all upper case letters at first and lower case letters at last  without using method
def fun(str):
    str1=""
    str2=""
    for ch in str:
        if ch==ch.upper():
            str1+=ch
        else:
            str2+=ch
    return str1+str2
str=input("enter a string:")
print(fun(str))