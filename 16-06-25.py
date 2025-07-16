# 2. Find the second largest values in a list
l=[2,3,4,5,6,7,8]
def fun(l):
    largest=second=float('-inf')
    for num in l:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num
    return largest,second
print(fun(l))

# 1. Take the list, take the sub list from the list and replace that sublist with sum of the sublist 
l=[1,2,3,4,5,6,7,8]
start=3
end=6
def fun(l,start,end):
    sub=l[start:end]
    return l[:start]+[sum(sub)]+l[end+1:]
print(fun(l,start,end))
