# Q1 : Multiplication Table (1 to 10)
# Write a Python program using nested loops to print the multiplication tables from 1 to 10.
# Example Output (partially shown)
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 10 x 10 = 100

def fun(n):
    for i in range(1,n+1):
        for j in range(1,11):
            print(i,"*",j,"=",i*j)
n=int(input("enter n number:"))
fun(n)


# Print All Pairs of Numbers (1 to n) Where Sum is Even
# Ask the user to enter a number n. Using nested loops, print all pairs (i, j) from 1 to n where the sum i + j is even.
# Example for n = 3:
# (1,1)
# (1,3)
# (2,2)
# (3,1)
# (3,3)

def fun(n):
    for i in range(1,n):
        for j in range(i+1,n):
            if (i+j)%2==0:
                print(i,j)
n=int(input("enter n number:"))
fun(n)


# Count Total Factors of All Numbers from 1 to n
# Ask the user to enter a number n. Use nested loops to find how many total factors (divisors) exist for all numbers from 1 to n.
# Example for n = 4
# 1 → 1
#  2 → 1, 2
#  3 → 1, 3
# 4 → 1, 2, 4
# Total = 8 factors

def fun(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j==0:
                print(j)
n=int(input("enter n number:"))
fun(n)


# Count Prime Numbers in a Range (1 to 100)
# Using nested loops, count how many prime numbers exist between 1 and 100.
# Hint : A number is prime if it’s only divisible by 1 and itself.

def fun():
    count=0
    for num in range(2,101):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            count+=1
    print(count)
print(fun())
