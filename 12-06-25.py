# 1.Write a program to take a string input and print its length.
def fun(str):
    return len(str)
str=input("enter a string:")
print(fun(str))

# 2.Take a string input and print it in reverse (without using [::-1]).
def fun(str):
    return str[::-1]
str=input("enter a string:")
print(fun(str))

# 3.Write a function to count the number of vowels in a string.
def fun(str):
    count=0
    for ch in str:
        if ch in "aeiou":
            count+=1
    return count
str=input("enter a string:")
print(fun(str))

# 4.Check if a string is a palindrome (reads the same forwards and backwards).
def fun(str):
    if str==str[::-1]:
        return "palindrome"
    return "not palindrome"
str=input("enter a string:")
print(fun(str))

# 5.Concatenate two strings and print the result.
def fun(str1,str2):
    return str1+str2
str1=input("enter a string1:")
str2=input("enter a string2:")
print(fun(str1,str2))

# 6.Print the first three characters of a string.
def fun(str):
    return str[0:4]
str=input("enter a string:")
print(fun(str))

# 7.Print characters from index 2 to index 5 of a string
def fun(str):
    return str[2:6]
str=input("enter a string:")
print(fun(str))

# 8.Print the string excluding the first and last characters.
def fun(str):
    n=len(str)
    return str[1:n-1]
str=input("enter a string:")
print(fun(str))

# 9.Print alternate characters of a string.
def fun(str):
    n=len(str)
    for ch in range(0,n,2):
        print(str[ch])
str=input("enter a string:")
fun(str)

# 10.Count how many times a specific character appears in a string.
def fun(str,target):
    count=0
    for ch in str:
        if ch==target:
            count+=1
    return count
str=input("enter a string:")
target=input("enter a string:")
print(fun(str,target))

# 11.Replace every occurrence of 'is' with 'si' in a string without using replace().
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

# 12.Find if a substring exists in a string or not.
def fun(str,str1):
    for y in range(len(str1)):
        if str1[y] in str:
            return "True"
    return "False"
str=input("enter a string:")
str1=input("enter a substring:")
print(fun(str,str1))

# 13. Remove all spaces from a string
def fun(str):
    result=""
    for ch in str:
        if ch!=" ":
            result+=ch
    return result
str=input("enter a string:")
print(fun(str))

# 14.Convert a string to uppercase without using upper() method.
def fun(str):
    result=""
    for ch in str:
        if 'a'<=ch<='z':
            result+=chr(ord(ch)-32)
        else:
            result+=ch
    return result
str=input("enter a string:")
print(fun(str))


# 15.Print each character of a string on a new line
def fun(str):
    for ch in str:
        print(ch)
str=input("enter a string:")
fun(str)

# 16.Count the number of digits, letters, and special characters in a string
def fun(str):
    letter=0
    digit=0
    special=0
    for ch in str:
        if 'a'<=ch<='z' or 'A'<=ch<='Z':
            letter+=1
        elif '0'<=ch<'9':
            digit+=1
        else:
            special+=1
    return letter,digit,special
str=input("enter a string;")
print(fun(str))


# 17.Swap two string variables without using a third variable.
def fun(s, a, b):
    if a >= len(s) or b >= len(s):
        return "Index out of range"
    s = list(s)  
    s[a], s[b] = s[b], s[a]
    return ''.join(s)
string = input("Enter a string: ")
a = int(input("Enter position a: "))
b = int(input("Enter position b: "))
print(fun(string, a, b))




