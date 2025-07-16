# Print given patterns 
# Z
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
# Y
rows = 7
for i in range(rows):
    for j in range(rows):
        if (i == j and i < rows // 2) or (i + j == rows - 1 and i < rows // 2) or (i >= rows // 2 and j == rows // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# M
rows = 5
for i in range(rows):
    for j in range(rows):
        if j == 0 or j == rows - 1 or (i == j and i <= rows // 2) or (i + j == rows - 1 and i <= rows // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


