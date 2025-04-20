# File Seek and Tell operations are used to work with the file objects and their positions within a file

with open("mylines.txt","r") as f:
    # Read from the 10th index character. It simply helps us to move to that index for start reading from.
    f.seek(10)
    
    # Read the next 5 bytes
    data = f.read(5)
    
    # To find our current position in file while reading use tell function.
    print(f.tell())
    
    print(data)
    
with open("newlines.txt","w") as k:
    # This truncates the file to 5 characters
    k.write("Hello Shubham, How are you doing?")
    k.truncate(5)