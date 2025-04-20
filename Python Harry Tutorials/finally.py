# EVen if function has returned then also finally will be executed

def func1():
    try:
        a = [6,3]
        num = int(input("Enter an integer:"))
        print(a[num])
        return 1
    except IndexError:
        print("Index error")
        return 0
    finally:
        print("I am always executed!")

x = func1()
print(x)