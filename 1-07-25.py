# 1.What is a Python Dictionary?

# Dictionary is a mutable datatype which contains key and value pairs keys must be unique and values can be duplicate and values are immutable data types

# 2.How can you access a value from a dictionary?
# By using values method
d={'a':1,'b':2,'c':3}
for values in d.values():
    print(values)

# 3.What will happen if you access a non-existent key  Give an example?
# If we try to access non existent key we will get key error and it can be done in 2 ways
# 1.by direct accessing of key
# 2.by get method
d={'a':1,'b':2,'c':3}
print(d.get('d'))

d={'a':1,'b':2,'c':3}
print(d['d'])

# 6.How do you get all the keys, values, or items in a dictionary?
d={'a':1,'b':2,'c':3}
print(d.items())

d={'a':1,'b':2,'c':3}
print(d.values())

d={'a':1,'b':2,'c':3}
print(d.keys())

# 5.How do you remove a key-value pair from a dictionary?
# Using pop method
d={'a':1,'b':2,'c':3}
n=d.pop('a')
print(d)

# 4.How do you add or update a key-value pair in a dictionary?
d={'a':1,'b':2,'c':3}
n=d.update({'d':4})
print(d)

