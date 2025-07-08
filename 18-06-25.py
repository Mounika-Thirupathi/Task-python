# 1. Take two dimensional array (square matrix) print diagnol values in list
l=[[1,2],[3,4]]
def fun(l):
    s=[]
    for i in range(len(l)):
        s.append(l[i][i])
    return s
print(fun(l))


# 2. Print anti diagonal values in list 
# V= [
# [1,3,6],
# [4,7,5],
# [6,4,9]
# ]

def fun(v):
    s=[]
    for i in range(len(v)):
        s.append(v[i][len(v)-i-1])
    return s
print(fun(v))

