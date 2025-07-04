# 9.Write a program to sum all the values in a dictionary.
d={'1':1,'2':4,'3':9,'4':16}
def fun(d):
    sum=0
    for values in d.values():
        sum+=values
    return sum
print(fun(d))

# 8.Create Reverse Word Dictionary
# Given list of words:
# words = ["cat", "dog", "bat"]
# Create a dictionary with words as keys and their reversed strings as values
# Expected Output:
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}
words = ["cat", "dog", "bat"]
def fun(words):
    res={}
    for x in words:
        res[x]=x[::-1]
    return res
print(fun(words))

# 7.Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd
# Expected Output:
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

def fun():
    res={}
    for x in range(1,6):
        if x%2==0:
            res[x]='even'
        else:
            res[x]='odd'
    return res
print(fun())

# 6.Write a program to store names as keys and their lengths as values.
def fun(n):
    res={}
    for i in range(n):
        keys=input(f"enter a key {i+1}:")
        res[keys]=len(keys)
    return res
n=int(input("enter a number:"))
print(fun(n))
        
# 5.Convert a dictionary to a list of tuples.
s= {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
d=list(s.items())
print(d)

# 4.What is the difference between dict.get() and direct key access?
# dict.get() will return value and direct access of key will also return value
# but direct method will not return error if key not found but direct accessing of key will through key error

# 3.Write a Python program to create a dictionary with two keys:
# "even" → containing all even numbers from the list
# "odd" → containing all odd numbers from the list
# Expected Output:
# {'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}
res={"even":[x for x in range(1,11) if x%2==0],
    "odd":[x for x in range(1,11) if x%2!=0]
}
print(res)

# 2.Count the frequency of each character in a given string using a dictionary.
def fun(str):
    ref={}
    for ch in str:
        if ch not in ref:
            ref[ch]=1
        else:
            ref[ch]+=1
    return ref
str=input("enter a string:")
print(fun(str))

# 1.Delete a list of keys from a dictionary
# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# # Keys to remove
# keys = ["name", "salary"]
d = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
for keys in ['name','salary']:
    d.pop(keys)
print(d)