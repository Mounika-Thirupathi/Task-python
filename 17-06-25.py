# 1. Reverse the list without using methods 
def fun(l):
    res=""
    for i in l:
        res=i+res
    return res
l=input("enter a list:")
print(fun(l))


# 3. Remove duplicates in the list without using methods 
def fun(l):
    seen=[]
    for i in l:
        if i not in seen:
            seen.append(i)
    return seen
l=list(map(int,input("enter a list:").split()))
print(fun(l))
    


# 4.1) Print the largest value in every list and concate the list 
Ex: [ [2,3,1], [4,5,3], [7,6,8] ] => o/p [3,5,8]
l=[[2,3,1], [4,5,3], [7,6,8] ]
def fun(l):
    for i in l:
        print(max(i))
fun(l)


# 4.2) Sum of Every list
l=[[2,3,1], [4,5,3], [7,6,8] ]
def fun(l):
    for i in l:
        s=0
        for j in i:
            s+=j
        print(s)
(fun(l))

