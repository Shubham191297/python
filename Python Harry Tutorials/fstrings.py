# for string formatting use below
letter="Hey my name is {} and I am from {}"
letter1="Hey my name is {0} and I am from {1}"
name="Shubham"
country="India"

print(letter.format(name,country))

# with fstrings are strings that can store variables in them
print(f"Hey my name is {name} and I am from {country}")

# to specify floating point numbers
cost = 10.9909090
print(f"The cost of milk is {cost:.2f}")

# to give demo how we are using fstrings do  below
print(f"Hey my name is {{name}} and I am from {{country}}")