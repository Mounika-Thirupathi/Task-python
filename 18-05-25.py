# print numbers from 1 to 10 using loop
for i in range(1,11):
    print(i)
 
# print  even numbers between 1 to 20
for i in range(2,21,2):
    print(i)
 
# Print the characters of the string "Python" one by one using a loop
v="python"
for i in v:
    print(i)
 
# Print the sum of numbers from 1 to 100.
sum=0
for i in range(1,101):
    sum+=i
print(i)
 
# Print multiplication table of 5 (like 5 x 1 = 5, ... 5 x 10 = 50).
n=5
for i in range(1,11):
    print(n,"*",i,"=",n*i)
 



# Print all elements of a list using a loop.
List=["apple", "banana", "cherry"]
n=len(List)
for i in range(n):
    print(List[i])
   
 
# Print only the vowels from the string "education" using a loop.
str="education"
for ch in str:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        print(ch)
 
# Count how many times the letter 'a' appears in the string "banana" using a loop
str="banana"
count=0
for ch in str:
    if ch=="a":
        count+=1
print(count)
 
# Print numbers from 10 to 1 using a loop (reverse order).
for i in range(10,0,-1):
    print(i)
 


# Ask the user to enter 5 numbers using a loop and print their sum.
sum=0
for i in range(5):
    num=int(input("enter the number:"))
    sum+=num
    i+= 1
print(sum)
 
# print tables up to n
n=int(input("enter a number:"))
i=1
while i<=n:
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    i+=1
 
   
 
 
