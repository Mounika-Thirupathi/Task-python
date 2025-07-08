# Practice problem solving on  list comprehension
# Rotate a list by k positions to the right.
# Example:
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def fun(l,k):
    return l[-k:]+l[:-k]
l=list(map(int,input("enter a list:").split()))
k=int(input("enter a number:"))
print(fun(l,k))

# using list comprehension
l=[1,2,3,4,5]
k=2
s=l[-k:]+l[:-k]
print(s)

# Remove all duplicates from a list without using set().
# Input: [1, 2, 3, 2, 1, 4, 5]
# Output: [1, 2, 3, 4, 5]
def fun(l):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s
l=list(map(int,input("enter a list:").split()))
print(fun(l))
            
# using list comprehension
s=[1, 2, 3, 2, 1, 4, 5]
b=[]
v=[b.append(x) for x in s if x not in b]
print(b)
            
# Find all pairs in a list that sum up to a target.
# Input: lst = [2, 4, 3, 5, 7], target = 7
# Output: [(2, 5), (4, 3)]            
def fun(v, target):
    result = []
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            if v[i] + v[j] == target:
                result.append((v[i], v[j]))
    return result
v = list(map(int, input("enter a list: ").split()))
target = int(input("enter a target: "))
print(fun(v,target))

# using complement
def fun(v, target):
    seen = set()
    result = []
    for num in v:
        complement = target - num
        if complement in seen:
            result.append((complement, num))
        seen.add(num)
    return result
v = list(map(int, input("enter a list: ").split()))
target = int(input("enter a target: "))
print(fun(v,target))

# using list comprehension
v=[2,4,3,5,7]
target=7
b=[ (v[i],v[j]) for i in range(len(v)) for j in range(i+1,len(v)) if v[i]+v[j]==target]
print(b)

# Flatten a 2D list without using built-in flatten functions.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]
v=[[1, 2], [3, 4], [5]]
def fun(v):
    result=[]
    for i in v:
        for j in i:
            result.append(j)
    return result
print(fun(v))

# using list comprehension
v=[[1, 2], [3, 4], [5]]
result=[]
s=[result.append(j) for i in v for j in i ]
print(result)


# Count the frequency of each element in a list and return a dictionary.
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}
def fun(v):
    s={}
    for i in v:
        if i in s:
            s[i]+=1
        else:
            s[i]=1
    return s
v=list(map(int,input("enter a list:").split()))
print(fun(v))

#using list comprehension
v = [1, 2, 2, 3, 1, 4, 2]
s = {i: v.count(i) for i in set(v)}
print(s)


# Part B: Strings (5 Questions)
# Check if a string is a palindrome (ignoring spaces and case).
# Input: "A man a plan a canal Panama"
# Output: True

# using slicing
def fun(str):
    for ch in str:
        if str==str[::-1]:
            return "palindrome"
        else:
            return "not palindrome"
str=input("enter a string:")
print(fun(str))

# using another string
def fun(str):
    rev=""
    for ch in str:
        rev=ch+rev
        if str==rev:
            return "palindrome"
    return "not palindrome"
str=input("enter a string:")
print(fun(str))

# using list 
str= "A man a plan a canal Panama"
s={"True" for ch in str if str==str[::-1]}
print(s)

# Remove all vowels from a string.
# Input: "Hello World"
# Output: "Hll Wrld"
def fun(str):
    rev=""
    for ch in str:
        if ch not in "aeiou":
            rev+=ch
    return rev
str=input("enter a string:")
print(fun(str))

# using list comprehension
str="Hello World"
v=[x for x in str if x not in "a e i o u"]
print(v)


# Count the number of words in a string without using .split().
# Input: "Python is great"
# Output: 3

def count_words(s):
    count = 0
    for i in range(len(s)):
        if (i == 0 and s[i] != ' ') or (s[i] != ' ' and s[i-1] == ' '):
            count += 1
    return count
text = "Python is great"
print(count_words(text))



# Find the longest word in a sentence.
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"
w=str.split()
l=[]
for i in w:
    l.append(len(i))
print(max(l))