import string
import random

def generate_random_string(length):
  characters = string.ascii_letters + string.digits
  return ''.join(random.choice(characters) for i in range(length))

plainString = input("Enter the text/string you want to encode: ")
randomString = generate_random_string(3)

if(len(plainString)>3):
    stringTexts = plainString.split(" ")
    
    encodedString = ""
    
    for p in stringTexts:
        encodedString = encodedString + " " + randomString+p[1::]+p[0]+randomString

    print(encodedString)
else:
    print(plainString[::-1])