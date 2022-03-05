# Q1 Write a program to combine two dictionary adding values for common keys.
# Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

a={'a':100,'b':200,'c':300}
b={'a':300,'b':200,'d':400}
for i in b:
    if i in a:
        a[i]=a[i]+b[i]
    else:
        a[i]=b[i]
print(a)

# Q2
# Write a python program to create a dictionay from a string
a='W3resource'
b={}
c=0
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)

# Q3
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

a={}
for i in range(1,6):
    b=i**2
    a[i]=b
print(a)

# Q4
# Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are square of keys

a={}
for i in range(1,16):
    b=i**2
    a[i]=b
print(a)

# Q5
# ???










# Q6
#add a key to dictionary

a={0:10,1:20}
d={2:30}
a.update(d)
print(a)

# Q7
# Write a Python script to concatenate the following dictionaries to create a new one

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for i in (dic1,dic2,dic3):
    i.update(dic4)
    print(i)
    

#Write a Python program to check whether a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
	    print('Key is not present in the dictionary')
is_key_present(7)