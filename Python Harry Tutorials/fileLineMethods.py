'''
f = open("mylines.txt","r")

while(True):
    line = f.readline()
    if not line:
        break
    print(line)

    
i = 0
k = open("marks.txt","r")
while(True):
    line = k.readline()
    
    if not line:
        break
    
    i = i + 1
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    
    print(f"Marks of student {i} in Maths is {m1}")
    print(f"Marks of student {i} in Maths is {m2}")
    print(f"Marks of student {i} in Maths is {m3}")
    
'''

f = open("writelines.txt","a")
lines = ["I am Kubernetes I am used for container orchestration","\nI am Jenkins I am used for CICD pipeline","\nHey guys you miss me I am prometheus. I am used for UI"]

f.writelines(lines)
f.close()