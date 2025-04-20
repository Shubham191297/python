def welcome():
    print("Hey nice to meet you my devops guys")

shubham = "An SRE devops guy"

# Now what happens that code inside if only runs when the code is being run directly not imported as package and invoked

# This can be used to determine whether the script is being run directly or being imported as a module into another script 

if __name__ == "__main__":
    welcome()