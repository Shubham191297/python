# READING A FILE
# f = open("myfile.txt","r")

# text = f.read()

# print(text)

# f.close()

'''
Different modes to open a file for

r - read mode. throws error if file does not exist
w - write mode. Writes to an existing or non existing file. Does not throw error on file absence. Overwrites content of file
a - Same as write mode. But content is not replaced instead new content is added from last line
x - create the file. Throws error if file already exists
t - to read the file as text type
b - to read the file content in binary
'''

# WRITING TO A FILE
f = open("myfile2.txt","w")
f.write("Hello, Angu!!")
f.close()

# FOR APPEND
f = open("myfile.txt","a")
f.write("Hello, Shubham!!")
f.close()

# WHEN WE DO NOT WANT TO CLOSE THE FILE BELOW IS THE EASIEST WAY
with open("myfile2.txt","a") as f:
    f.write("We have jabariya jodi!")