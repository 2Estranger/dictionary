# 40


a=['S1', 'S2', 'S3', ]
b=['Antra', 'Sayjal', 'Depika']
c=[6, 7, 8]
d=[]
for i in a:
    x={}
    for j in b:
        y={}
        for k in c:
            y[j]=k
            x[i]=y
            d.append(x)
            c.remove(k)
            break
        b.remove(j)
        break
print(d)


# 35
# coutn the items that is in list
a =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for i in a:
    for j in a[i]:
        c+=1
print("counting the items:",c)


# 30  
# .Write a Python program to remove spaces from dictionary keys
# {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 

# a= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# b={}
# for i,j in a.items():
#     for k in " ":
#         i=i.replace(k,"")
#         b[i]=j
# print(b)


#  Q19
# Write a Python program to remove dublicates
# a = {'id1':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']},
#  'id2':{'name': ['David'],'class': ['V'],'subject_integration': ['english, math, science']},
#  'id3':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']},
#  'id4':{'name': ['Surya'],'class': ['V'], 'subject_integration': ['english, math, science']},}

# b={}
# for i,j in a.items():
#     if i not in b.values():
#         b[i]=j
# print(b)



# # Q33.Python: Print a dictionary line by line
# a= {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for i in a:
#     print(i)
#     for j,k in a[i].items():
#         print(j,":",k)
        
        
# Q16
# Map two list in a dictionary

# a=["a","b","c","d"]
# b=[1,2,3,4]
# d={}
# for i in a:
#     for j in b:
#         d[i]=j
#         b.remove(j)
#         break
# print(d)
        
        
 


# EVEN AND ODD >>                <<     OUTPUT>>              {"a":[2,10],"b":[4],"c":[6]}            <<
e={"a":[2,3,7,10],"b":[4,1],"c":[3,9,6]}
b=dict()
c=[]
for i in e:
    for j in e[i]:
        if j%2==0:
            c.append(j)
            b[i]=c
            break
        else:
            pass
            break
print(b)


# NOT DONE