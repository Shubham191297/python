tup =(1,4,8,0)

print(tup,type(tup))

tup2 = (1)
print(type(tup2))
# need to provide , if tuple consists of a single value
tup2 = (1,)
print(type(tup2))

# We cannot change the tuple they are immutable
# tup2[2] = 0
# this will throw error

if 8 in tup:
    print("Yes 8 is present in the tuple")

tup3 = tup[1:4]
print(tup3)