# a41
# Write a Python program to filter the height and width of students, which are stored in a dictionary. 

dic={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}
s={}
for i,j in dic.items():
    if j[0]>=6.0 and j[1]>=70: 
        s[i]=j
print(s)




# 42
# Write a Python program to check all values are same in a dictionary. Go to the editor
# a={"Cerial":20,"Butter":20,"Sandwich":20,"Rainbow":20}
# for i in a:
#     if a[i]==20:
#         print(True)
#         break
#     else:
#         print(False)
#         break
    
    
    
    
# Q43
# Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
# a=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',6)]
# b={}
# cd=[]
# for i,j in a:
#     b[i]=i
#     c=0
#     if c==
    
    
    # RRRRRRRRRRREEEEEEEEEEEEEEEEEEDDDDDDDDDDDDDDDOOOOOOOOOOOOOOO           IIIIIIIIIIIIIIIITTTTTTTTTTTTTTT
    
    
# Q44
# Write a Python program to split a given dictionary of lists into list of dictionaries.
# > Dictionary of List into List of dictionary <
# a={'Science':[88,89,23,54],'Language':[77,45,84,80]}








# Q45
# Write a Python program to remove a specified dictionary from a given list.
a=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
  {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
for i in range(len(a)):
    if a[i]['color']=='Maroon':
        del a[i]
        break
print(a)


# Q46
# .Write a Python program to convert string values of a given dictionary, into integer/float datatypes
# a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# b=dict()
# for i in a:
#     a[i]=break
# print(b)

# Q47
# A Python Dictionary contains List as value. Write a Python program to clear the list
# values in the said dictionary
a={'C1':[1,2,3],'C2':[3,4,5],'C3':[5,6,7]}
for i in a:
    a[i]=[]
print(a)

# Q48
# Write a Python program to find the length of a given dictionary values.
a={1:'red',2:'orange',3:'black',4:'blue',5:'black'}
b={}
for i,j in a.items():
    b[j]=i
print(b)
# rerdoddodoodpfuvpkl


# Q49
# Python: Access dictionary key’s element by index
a={'physics':40,'chemistry':30,'math':50}
for i in a:
    print(i)
    
 