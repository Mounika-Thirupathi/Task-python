# 1. Create a dictionary without using {} curly brackets.The dictionary should store the following information:
# Result = {‘name’:’kumar’,’pin’:101}

result=dict(name='kumar',pin=101)
print(result)

# 2.Sort Dictionary by Values (Descending Order) 
# EX: Input: {'apple': 50, 'banana': 20, 'mango': 80}

for key, value in sorted(d.items(), key=lambda item: item[1]):
    print(key, value)

# 3. Count Frequency of Each Word in a Sentence?
# EX:  "hello world hello python"

def fun(str):
    s={}
    word=str.split()
    for ch in word:
        if ch in s:
            s[ch]+=1
        else:
            s[ch]=1
    return s
str=input("enter a sentence:")
print(fun(str))

# 4. Merge Two Dictionaries with out using update method? 
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}

m = {k: v for d in (d1, d2) for k, v in d.items()}
print(m)


# 5.Invert a Dictionary (Swap keys and values)
#    Input: {'a': 1, 'b': 2, 'c': 3}
#    Output: {1: 'a', 2: 'b', 3: 'c'}

# d={'a': 1, 'b': 2, 'c': 3}
s={}
for key,values in d.items():
    s[values]=key
print(s)

#  6.Find Sum of All Values in a Dictionary
#  Input: {'a': 10, 'b': 20, 'c': 30}
# d={'a': 10, 'b': 20, 'c': 30}
sum=0
for values in d.values():
    sum+=values
print(sum)
