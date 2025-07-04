# Arthimetic operator
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Assignment operator
a=20
b=30
c=a+b
print(c)
a=10
b=20
a+=b
print(a)   
a=5
b=10
a=a+b
print(a)

# comparision operator
a=10
b=20
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)

# chining operator
a=10
b=20
c=30
d=40
max1=a<b<c<d
print(max1)

# ternary operator
h=20
res1= 'even' if h%2==0 else 'odd'
print(res1)

# Membership operator

v=[1,2,3,4,5,6]
if 10 in v:
    print(True)
else:
    print(False)

v=[1,2,3,4,5,6]
if 10  not in v:
    print(True)
else:
    print(False)

# bitwise operator

a=10101
b=10110
print(a&b)
print(a|b)
print(a^b)
a=10101
b=2
print(a>>b)
print(a<<b)

# identity operator
a=10
b=20
print(id(a),id(b))
print(a is b)

# logical operators
a=True
b=False
print(a or b)
a=True
b=True
print(a and b)
a=True
print( not(a))
  