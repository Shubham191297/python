import os

def fileFilter(x):
    return not x.endswith(".py")

listFiles = list(filter(fileFilter,os.listdir()))

for index, file in enumerate(listFiles):
    extension = file.split(".")[1]
    newFile = str(index+1)+ "." +extension
    os.rename(file, newFile)