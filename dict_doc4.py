#32
# Write a Python program to get the key, value and item in a dictionary.
# a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key value count")
# c=0
# for key, val in a.items():
#     c+=1
#     print(key, val, c)
    
# 35
# coutn the items that is in list
a =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for i in a:
    for j in a[i]:
        c+=1
print(c)


# 36
# .Write a Python program to match key values in two dictionaries.

a={'key1':1, 'key2':3, 'key3':2}
b={'key1':1, 'key2':2}
c={}
for i in a:
    for i in b:
        if a[i]==b[i]:
            c[i]=b[i]
            print(c,"is present in both a and b")
            break
        
# 37
# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list 
# from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
for i in a:
    if a[i][4]:
        b=a[i][4]
    print(b)
    
    
# 38
# Write a Python program to drop empty Items from a given Dictionary
a={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={}
for key,value in a.items():
    if value is not None:
        b[key]=a[key]
    else:
        pass
print(b)



# Q39.
# Write a Python program to filter a dictionary based on values. 

a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
b={}
for i in a:
    if a[i]>170:
        b[i]=a[i]
    else:
        pass
print(b)


# 40
# Write a Python program to convert more than one list to nested dictionary. 
d=['S1', 'S2', 'S3', ]
di=['Antra', 'Sayjal', 'Depika']
dic=[6, 7, 8]
a=[]
for i in d:
    b={}
    for j in di:
        c={}
        for k in dic:
            c[j]=k
            b[i]=c
            a.append(b)
            dic.remove(k)
            break
        di.remove(j)
        break
print(a)

# 41
#.Write a Python program to filter the height and width of students, which are stored in a dictionary.
