# Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}

# QUESTION2

a={"name":"Prena","marks":55}
# for i in a:
if "name" in a:
    print("exist")
else:
    print("not exust")

# QUESTION 3 SUM OF VALUES

a={"data1":100,"data2":-54,"data3":247}
sum=0
for i in a.values():
    sum=sum+i
    print(sum)
    
# QUESTION4
# Write a program to remove the first key value pair from a nested dictionary

a={1:"NAVGURUKUL",2:"IN",3:{"A":"WELCOME","B":"TO","C":"DHARMASALA"}}
del a[3]["A"]
print(a)

# QUESTION 5
a=["one","two","three","four","five"]
b=[1,2,3,4,5]
d={}
for key in a:
    for value in b:
        d[key] =  value
        b.remove(value)
        break
print(str(d))


# QUESTION6
dic={"ball":"red","bat":4,"wicket":8,"ball":"black","bat":3}
list=[]
d=dict()
for key,value in dic.items():
    if dic[key] not in list:
        list.append(key)
        d[key]=value
print(d)

# QUESTION 7
# PRINT UNIQUE VALUE IN LIST FROM DICTIONARY
 
a=[{"first":1},{"second": 2},{"third": 1}, {"four": 5}, {"five":5}, {"six":9},{"seven":7}]
b=[]
for i in a:
    for j in i.values():
        if j not in b:
            b.append(j)
print(b)