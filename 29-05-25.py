# sum of prime numbers using functions 

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def sum_of_primes(n):
    total = 0
    for i in range(2, n+1):
        if is_prime(i):
            total += i
    return total
n = int(input("Enter a number: "))
result = sum_of_primes(n)
print(result)


# sum of odd num using functions
def fun(l):
    sum=0
    for i in l:
        if i%2!=0:
            sum+=i
    return sum
l=list(map(int,input("enter a list:").split()))
print(fun(l))

