car={"brand":"ford","model":"mustang","year":1964}
print(car["model"])

students=dict(name="prena",age=20)
print(students)

my_dict={1:"apple",2:"ball"}
print(my_dict)

my_dict={"name":"john",1:[2,3,4]}
print(my_dict)

Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To', 'C' : 'DHARAMSALA'}}
print(Dic[3])

# ACCESS_ELEMENTS_IN_DICTIONARY

person={"name":"Prena","age":20,"gender":"female",4:"organisation"}
result=person["age"]
x=person.get("gender")
print(person[4])
print(x)
print(result)

# get()

person1={'name':"jack","age":20,'gender':'female',4:{"organisation":"navgurukul",'place':'dharmasala'}}
print(person1['gender'])
print(person1[4])
result1=person1[4]['place']
print(result1)

dic= {'Name': 'RAM','Age': 17,}
dic['student']={'id':22, 'place':'dharamsala'}
print(dic)