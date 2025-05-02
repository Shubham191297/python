import shutil

# This command is used to copy the file
shutil.copy("secretcode.py","secretcode2.py")

# Below command is used to copy the directory
shutil.copytree(".tutorial","my-tutorial")


shutil.move(".tutorial/file.file","file.file")

shutil.rmtree("my-tutorial")