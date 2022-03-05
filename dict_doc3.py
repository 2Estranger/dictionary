# 20
# Write a program to Check if a dictionary si empty or not
a={}
b=len(a)
if b==0:
    print('I am Empty')
else:
    print('I am Not Empty')
    
    
# 
# Write a Python program to combine two dictionary adding values for common keys
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d2:
    if key in d1:
        d2[key]=d2[key] + d1[key]
    else:
        d1=d2[key]
print(d2)

# 21
# Print all the unique value in a dictionary
a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_value=set(val for dic in a for val in dic.values())
print('uniques value:',unique_value)
# Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# This line s = set( val for dic in lis for val in dic.values()) is roughly equivalent to:
s = set()
for dic in a:
   for val in dic.values():
      s.add(val)
      
# 22
# display all combinations of letters, selecting each letter from a different key in a dictionary. 

e={1:['a','b'], 2:['c','d']}
for x in e[1]:
    for y in e[2]:
        print(x+y)
        

# 23
my_dict={'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
max1=0
max2=0
max3=0
for i in my_dict:
    if my_dict[i]>max1:
        max3==max2
        max2=max1
        max1=my_dict[i]     
    elif my_dict[i]>max2:
        max3=max2
        max2=my_dict[i]
    elif my_dict[i]>max3:
        max1=my_dict[i]
print(max1)
print(max2)
print(max3)

# 25
# Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.
a="W3resource"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)


# 26
# Write a Python program to print a dictionary in table format.
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
    


# Q27.Write a Python program to count the values associated with key in a dictionary
a = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['id'] for d in a))
print(sum(d['success'] for d in a))


# 28
# Write a Python program to convert a list into a nested dictionary of keys.

a = [1, 2, 3, 4]
new_dict = b = {}
for i in a:
    b[i] = {}
    b= b[i]
print(new_dict)

# 29
# Write a Python program to sort a list alphabetically in a dictionary.
  
a ={"L1":["Geeks", "for", "Geeks"],"L2":["A", "computer", "science"],"L3":["portal", "for", "geeks"],}

for i,j in a.items():
    s={i:sorted(j)}
    print(s)
  
# 30  
# .Write a Python program to remove spaces from dictionary keys
#  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 

a= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
b={}
for i,j in a.items():
    for k in " ":
        i=i.replace(k,'')
        b[i]=j
print(b)