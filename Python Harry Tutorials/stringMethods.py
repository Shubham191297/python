# Strings are immutable

str="Shubham"

print(str.upper())
print(str.lower())

# To strip trailing characters of a string
name="Shradha!!!!!!!"
print(name.rstrip("!"))

# To replace the occurence of string from the main string
firstname="Pareshwar"
print(firstname.replace("a", "i"))
newName="AnguShubhamAngu!!!!!Angu"
print(newName.replace("Angu", "Shradha"))

# To split string into array of strings
stringlist = "My name is Shubham Thapliyal"
print(stringlist.split(" "))

# To convert to capitalize string
capitalString="this Is greaT"
print(capitalString.capitalize())

# To push string to the center
centerString="Angu"
print(centerString.center(50))

# To count the number of characters in string
str2="ShradhaAndShubham"
print(str2.count("h"))

# To check if string starts or ends with specific string
strCheck="###Angu!!!"
print(strCheck.endswith("!!"))
print(strCheck.startswith("##"))

# We can also check the occurence of string with start and end index position
print(strCheck.endswith("!!",3,7))
print(strCheck.endswith("!!",5,10))

# to find index of an occurence of string
str5="My name is Shubham"
print(str5.find("is"))
print(str5.find("ish"))
# print(str5.index("ish"))

# to check if given string is alphanumeric
str0 = "My hobby is 2#$$%"
str6 = "AnguShubham"
print(str0.isalnum())
print(str6.isalnum())
print(str6.isalpha())

# returns true if all the values within given string are printable
print((str6+"\n").isprintable())

# checks for whitespaces
print("  ".isspace())

# To check if given string is a title string
print("Devops Is About Deployment".istitle())
print("Devops Is about Deployment".istitle())

# check if given string is upper or lower
print("shradha".islower())
print("SHUBHAM".isupper())

# Swap case - To convert lower case to upper case and vice versa
print("He Is a niCe Guy".swapcase())
print("the boyS".title())