# doc strings are used to give information about the functions
# unlike comments doc strings are not ignored and can be read using
def square(n):
    '''Takes number n and prints square of that number'''
    print(n**2)
square(7)
print(square.__doc__)

# Docstring can either be place just after function definition or just before starting from body

# pep8 - document that provides guidelines and best practices