# 5 operations on set  
# union
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))

# Intersection
A = {1, 2, 3}
B = {3, 4, 5}
print(A.intersection(B))  

# Difference
A = {1, 2, 3}
B = {3, 4, 5}
print(A.intersection(B))   

# Symmetric difference
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))  

# Add
A = {1, 2, 3}
A.add(4)
print(A)               

# update
A.update([5, 6])
print(A)               

# remove
A.remove(3)
print(A)                

# discard
A.discard(10)       
print(A)


# 5 Operations on tuples

t = (10, 20, 30, 40)
print(t[0])       
print(t[-1])   

t = (10, 20, 30, 40, 50)
print(t[1:4])    
t1 = (1, 2, 3)
t2 = (4, 5)
result = t1 + t2
print(result)          


t = (1, 2)
result = t * 3
print(result)          

t = (10, 20, 30)
a, b, c = t
print(a)    
print(b)    
print(c)    

# len,min,max,sum
t = (5, 10, 15)
print(len(t))     
print(max(t))   
print(min(t))    
print(sum(t))   

