import os

folders = os.listdir("data")

# print(folders)
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    
os.chdir("/Users")
print(os.getcwd())