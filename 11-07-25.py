# 1.print H pattern
def fun(rows):
    for i in range(1,rows+1):
        res=""
        for j in range(1,rows+1):
            if i==3 or j==1 or j==5:
                res+="*"+" "
            else:
                res+=" "+" "
        print(res)
rows=int(input("enter a number:"))
fun(rows)

# 2.print E pattern
def fun(rows):
    for i in range(1,rows+1):
        res=""
        for j in range(1,rows+1):
            if i==1 or i==(rows//2)+1 or i==5 or j==1:
                res+="*"+" "
            else:
                res+=" "+" "
        print(res)
rows=int(input("enter a number:"))
fun(rows)

# 3.print N pattern
def fun(rows):
    for i in range(1,rows+1):
        res=""
        for j in range(1,rows+1):
            if j==1 or j==5 or i==j:
                res+="*"+" "
            else:
                res+=" "+" "
        print(res)
rows=int(input("enter a number:"))
fun(rows)

