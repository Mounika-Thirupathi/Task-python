# 2. p = ["Python", "java", "c++"]   
p = ["Python", "java", "c++"]
v=tuple(x for x in p if x.lower()=="python")
print(v)

# 3.print prime numbers between 10 to 20 using tuple comprehension
v=tuple(x for x in range(10,21) if all(x%y!=0 for y in range(2,x)))
print(v)

# 4.given a string "abcd" create a tuple of ASCII value of each character
s="abcd"
v=tuple(ord(x) for x in s )
print(v)

