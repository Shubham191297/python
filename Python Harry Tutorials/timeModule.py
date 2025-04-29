import time as tm

def usingWhile():
    i = 0
    while i<50000:
        i = i + 1
        

def usingFor():
    print("Using foorrr")
    for i in range(50000):
        pass

init = tm.time()
usingWhile()
t1 = tm.time() - init
init = tm.time()
print(t1)

usingFor()
t2 = tm.time() - init
print(t2)


tm.sleep(3)
print("This is printed after 3 seconds")

t = tm.localtime()
formatted_time = tm.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)