# print tables from 1 to 5 using loops 
n=int(input("enter a number:"))
i=1
while i<=n:
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    i+=1

# Task2:#print this pattern
# """
# 1
# 2
# 2
# 3
# 4
# 4
# 4
# 4
# 5
# 6
# 6
# 6
# 6
# 6
# 6
# """ 
for i in range(1,7):
    if i%2==0:
        for j in range(i):
            print(i)
    else:
        print(i)



