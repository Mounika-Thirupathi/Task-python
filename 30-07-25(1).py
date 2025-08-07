m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
found=False
for row in range(len(m)):
    for col in range(len(m[row])):
        if row==col:
            print(f" {m[row][col]}is number ,{row+1} is row ,{col+1} is column")
            Found=True
            break
    if found==True:
        break