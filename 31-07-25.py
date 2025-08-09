# Module os is used to communicate with os in the system used for working with files and directories
import os
print(os)

# Methods in os module
os.getcwd
# -->To get current working directory or folder
import os
print(os.getcwd())

os.chdir()
# -->used to change directory 
print(os.getcwd())
os.chdir("sample")
print(os.getcwd())

# creating a file in sample directory 
file=open("hello.txt","w")
print(file.write("hello"))

# another method
with open("hello.txt","w") as file:
file.write("This is from another file")

os.listdir()
# -->returns files and folders in a directory
print(os.listdir())

# to find number of files in a directory
file=0
folders=0
for content in os.listdir():
    if "." in content:
        file+=1
    else:
        folders+=1
print(f"there are {file} files")
print(f"there are {folders} folders")

os.mkdir("sample2")
# -->used to create a folder

os.makedirs("sample4/nested")
# -->creates a folder inside folder

# creates folder inside folder and file
file=open("sample4/nested/demo.txt","w")
print(file.write("hello"))

os.remove("sample2")
# -->do not remove folders because python has no permissions

os.rmdir("sample2")
# -->do not remove folders because python has no permissions
os.rename("sample2","hi")
# -->used to rename source file name with destination file name

print(os.path.exists("hello"))
# -->check whether the file or folder exist or not if exist return true else return false

# checks if a file exist or not else creates a file
if os.path.exists("hello.txt"):
    print("already exist")
else:
    open("hello.txt","w")

# to check whether it is file or folder using os.path.is folder() method -->it returns boolean values true if file else false
print(os.path.isfile("hello.txt"))
print(os.path.isdir("sample"))

print(os.environ)
# -->return all the environments used to run the os

# --->returns environment keys
for env in os.environ:
    print(env)

# -->used to return the statics of a file or folder
print(os.stat("hello.txt")) 

# -->returns the contents in a list present in the folder
print(list(os.walk(top="./python core")))
