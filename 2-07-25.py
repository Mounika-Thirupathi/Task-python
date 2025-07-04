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
        