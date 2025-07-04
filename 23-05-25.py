# Count Prime Numbers between 1 and 100 (using nested loops)

def fun():
    count=0
    for num in range(2,101):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
        if is_prime:
            count+=1
    return count
print(fun())


# Print Multiplication Table (1 to 5)
def fun(n):
    for i in range(1,n+1):
        for j in range(1,11):
            print(i,"*",j,"=",i*j)
n=int(input("enter a number:"))
fun(n)


# Print Number Pattern

def fun(n):
    for num in range(n+1):
        for i in range(1,num+1):
            print(i,end=" ")
        print()
n=int(input("enter a number:"))
fun(n)


# Print a Right-Angled Triangle

def fun(n):
    for i in range(n+1):
        print("*"*i)
    print()
n=int(input("enter a number:"))
fun(n)



# Print a Rectangle Pattern
def fun(r,c):
    for i in range(r):
        for j in range(c):
              print("*",end="")
        print()
r=int(input("enter a number:"))
c=int(input("enter a number:"))
fun(r,c)
