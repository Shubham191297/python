# a = input("Enter the number:")
# print(f"Multiplication table of {a} is:")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#         print("Invalid input!!")
        
# print("End of Code")

try:
    a = [6,3]
    num = int(input("Enter an integer:"))
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index error")
finally:
    print("I am always executed!")

