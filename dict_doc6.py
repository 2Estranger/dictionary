#Q50
# Write a Python program to convert a given dictionary into a list of lists.
# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=[b]




# Q51
# Write a Python program to filter even numbers from a given dictionary values.
a={'V': [1, 4, 6, 10], 'VI': [1, 2, 12], 'VII': [1, 3, 8]}
b=[]
c={}
for i in a:
    for j in a[i]:
        if j%2==0:
            c[i]=j
b.append(c)
print(b)
            

# Q53
# Write a Python program to convert a given list of lists to a dictionary. 
a=[[1,'Jean Castro','V'],[2,'Lula Powell','V'],[3,'Brian Howell','VI'],[4,'Lynne Foster','VI'],[5,'Zachary Simon','VII']]


# a=['a', 1, 'b', 2, 'c', 3]






    
    
# Q54.
#  Write a Python program to create a key-value list pairings in a given dictionary. 
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
b=[]
s={}
for i in a:
    for j in a[i]:
        s[i]=j
b.append(s)        
print(b)