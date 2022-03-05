# pop
a={1:10,2:20,3:30}
a.pop(1)
print(a)

# popitems
a={1:10,2:20,3:30}
a.popitem()
print(a)


# del
a={1:10,2:20,3:30}
del a[2]
print(a)

# a={1:10,2:20,3:30}
# del a
# print(a)

# copy
a={1:10,2:20,3:30}
b=a.copy()
print(b)

# fromkeys
a=('fkey','skey','tkey')
b=0
z=dict.fromkeys(a,b)
print(z)

# setdefaults 
a={1:10,2:20,3:30}
x=a.setdefault(6,60)
print(x)

# update
a={1:10,2:20,3:30}
a.update({3:40})
print(a)

# get
a={1:10,2:20,3:30}
b=a.get(2)
print(b)

