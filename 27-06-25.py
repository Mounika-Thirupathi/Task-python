# 1.Find the highest frequency character in the string
s="chaitanya"
v={x:s.count(x) for x in s }
print(max(v,key=v.get))

# 2.Find it is anagram or not using dictionary
def fun(str1,str2):
    if sorted(str1)==sorted(str2):
        return "anagram"
    else:
        return "not anagram"
str1=input("enter a string1:")
str2=input("enter a string2:")
print(fun(str1,str2))


