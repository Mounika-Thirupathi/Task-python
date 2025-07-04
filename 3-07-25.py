# 1.What is an Automorphic Number? Give examples.
#  An Automorphic Number is a number whose square ends with the number itself.
#  Example: 5 (5² = 25), 6 (6² = 36), 76 (76² = 5776)


# 2.Count Vowels in String with Dict Comprehension.
# s = "welcome to python programming"
s = "welcome to python programming"
v="aeiou"
c={v:s.count(v) for v in "aeiou"}
print(c)

# 3.What is the difference between Shallow Copy and Deep Copy in Python? Explain with examples.
# Shallow copy :if changes are made in one object change reflects in reference object also
# Example 
list1:[[1,2],[3,4]]
list2=copy.copy(list1)
list2[0][0]=100
print(list1)
print(list2)

# Deep  copy :if changes are made in one object change do not reflects in reference object 
list1:[[1,2],[3,4]]
list2=copy.deepcopy(list1)
list2[0][0]=100
print(list1)
print(list2)

#  5.Explain about setdefault function in dictionary data type ?
# Setdefault function returns the value for the key if present other wise if the key is not present it will assign none value or we can declare a key and we can assign a default value to it
# Example
d={'a':1,'b':2,'c':3,'d':4}
print(d.setdefault('a'))
print(d.setdefault('e'))
print(d.setdefault('f',100))
print(d)
                                                                           
# 6.Create a dictionary using dictionary comprehension for the given list of numbers, where:
# Each number is a key.
#  The value is "prime" if the number is prime.
# The value is "notprime" if the number is not prime.
# Output:   {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
d = {i: 'prime' if is_prime(i) else 'not prime' for i in range(2, 7)}
print(d)

# 7.Find Max and Min Value in Dictionary
# Input:
# d = {'a': 10, 'b': 5, 'c': 15}
# Output:
# Max Value → 15
# Min Value → 5
d = {'a': 10, 'b': 5, 'c': 15}
print(max(d.values()))
print(min(d.values()))

# 8. Invert a dictionary with list values (group keys by their values)
# Input:
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# Output:
# {1: ['a', 'c'], 2: ['b'], 3: ['d']}
#  (Hint: Use setdefault method)
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
s={}
for x,y in d.items():
    s.setdefault(y,[]).append(x)
print(s)

