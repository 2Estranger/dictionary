# Q9
#Write a Python program to iterate over dictionaries using for loops.
d = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
for i in d:
    print(d)


# Q10
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

a={}
for i in range(1,16):
    b=i**2
    a[i]=b
print(a)

# Q11
# Merge two Dicitionary

a={1:10,2:20,3:30,4:40}
b={5:50,6:60}
for i in b:
    a.update(b)
print(a)

# Q12
# Iterate 
a={1:10,2:20,3:30}
for i in a:
    print(a)
    
# Q13
# Sum all the items in a dictionary
a={1:10,2:20,3:30}
sum=0
for i in a.values():
    sum+=i
print(sum)

# Q14
# Multiply all the items in a dictionary
a={1:10,2:3,3:2}
m=1
for i in a:
    m=m*a[i]
print(m)

# Q15
# Remove a key form a dictionary
a={1:10,2:20,3:30}
del a[1]
print(a)

# Q16
# Map two list in a dictionary

a=["a","b","c","d"]
b=[1,2,3,4]
d={}
for i in a:
    for j in b:
        d[i]=j
        b.remove(j)
        break
print(d)

# Q17
# Write a python programn to sort a dictionary by key
a={"c":'cat',"a":"apple",'b':"bone"}
b={}
for key in sorted(a):
    print(key,":",a[key])
    
# Q18
# Write a Python program to get the maximum and minimum value in a dictionary.

a = {"a": 1, "b": 2, "c": 3}
max_key = max(a, key=a.get)
print(max_key)

# Q19
# Write a Python program to remove dublicates
a = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

b={}
for i,j in a.items():
    if i not in b.values():
        b[i]=j
print(b)


def sum(a=3,b=4):
    c=a+b
    print(c)
sum(a,b)