a={(1,2):1,(2,3):4}
print(a[2,3])

# Q.2
a={'a':1,'b':2,'c':3}
print(a['a''b'])

# Q.3
fruit={}
def addon(index):
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
addon("Apple")
addon('Banana')
addon("Apple")
print(len(fruit))
print(fruit)

# Q.4
Student={}
Age={}
Details={}
Student['name']='Bella'
Age['student_age']=14
Details['student']=Student
Details["age"]=Age
print(len(Details["student"]))

# Q.5
a = {}
a[(1,2,4)] = 8
a[(4,2,1)] = 10
a[(1,2)] = 12
sum = 0
for i in a:
    sum += a[i]
print(sum)
print(a)

# Q.6
box={}
jars={}
crates={}
box['biscuit']=1
box['cake']=3
jars['jam']=4
crates['box']=box
crates['jars']=jars
print(crates)


# Q.7
rec={'name':'python','age':20,'addr':'NJ','country':'USA'}
id1=id(rec)
del rec
rec={'name':'python','age':20,'addr':'NJ','country':'USA'}
id2=id(rec)
print(id1==id2)