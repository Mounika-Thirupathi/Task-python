# write 1 to 10 sum of odd
sum=0
for i in range(1,11,2):
    print(i)
    sum+=i
print("sum is:",sum)
 
#write 1 to 10 sum of even
sum=0
for i in range(2,11,2):
    print(i)
    sum+=i
print("sum is:",sum)
 
#write 1 to 10 sum of digits
sum=0
for i in range(1,11):
    sum+=i
print("sum is:",sum)
 
#greater value of 3 numbers
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
 
#greater value of 2 numbers
a=int(input("enter a value:"))
b=int(input("enter b value:"))
if a>b:
    print(a)
else:
    print(b)
 
#find leap year or not
year=int(input("enter a year:"))
if year%400==0 or year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not leap year")
 

