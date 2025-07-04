# Print the first 5 characters of a string
def fun(str):
    return str[:5]
str=input("enter a string:")
print(fun(str))

# 2.Print the last 3 characters of a string using negative indexing
def fun(str):
    return str[-3:]
str=input("enter a string:")
print(fun(str))

# 3.Print characters from index 2 to 7
def fun(str):
    return str[2:7]
str=input("enter a string:")
print(fun(str))


# 4.Print the string in reverse
def fun(str):
    return str[::-1]
str=input("enter a string:")
print(fun(str))

# 5.Print every second character of a string
def fun(str):
    return str[::2]
str=input("enter a string:")
print(fun(str))

# 6.Print characters from index 1 to second last character
def fun(str,n):
    return str[0:n-1]
str=input("enter a string:")
n=len(str)
print(fun(str,n))

# 7.Print characters from -8 to -3
def fun(str,n):
    return str[-8:-2]
str=input("enter a string:")
n=len(str)
print(fun(str,n))

# 8.Get substring from start till 4th index
def fun(str,n):
    return str[0:4]
str=input("enter a string:")
n=len(str)
print(fun(str,n))

# 9.Get substring from 3rd index till end
def fun(str,n):
    return str[3:n]
str=input("enter a string:")
n=len(str)
print(fun(str,n))

# 10.Access the character at index -5
def fun(str):
    for ch in range(len(str)):
        return str[5]
str=input("enter a string:")
print(fun(str))

# 11.Extract substring with step value 3
def fun(str):
        return str[::3]
str=input("enter a string:")
print(fun(str))

# 12.Print substring from -7 to end with step 2
def fun(str):
    return str[-7::2]
str=input("enter a string:")
print(fun(str))

# 13.Exclude first and last character and print the rest
def fun(str,n):
    return str[1:n-1]
str=input("enter a string:")
n=len(str)
print(fun(str,n))

# 14.Print string skipping first 3 and last 3 characters
def fun(str,n):
    return str[3:n-3]
str=input("enter a string:")
n=len(str)
print(fun(str,n))

# 15.Print the middle character of an odd-length string
def fun(str,n):
    middle=n//2
    return str[middle]
str=input("enter a string:")
n=len(str)
print(fun(str,n))


