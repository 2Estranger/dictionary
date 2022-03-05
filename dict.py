thisdict={"brand":"Ford","Model":"Mustang","Year":1964}
print(thisdict)

dict={"Brand":"Ford","Model":"Mustang","Year":1964}
print(len(dict))


dict1={"brand":"ford","model":"mustang","year":1964}
x=dict1["model"]
print(x)

                    #OR

dict2={"brand":"ford","model":"mustang","year":1964}
x=dict2.get("year")
print(x)

# get keys

# car={"brand":"Ford","Model":"Mustang","Year":1964}
# if "Model" in car: 
#     print("yes,'model' is one of keys in car dictionary ")
    
car={"brand":"ford","model":"mustang","year":1964}
car.update({"color":"Black"})
print(car)    
    

# car={"Brand":"Ford","Model":"Mustang","Year":1964}
# car.clear()
# print(car)

# remove function
car_details={'brand':'ford','model':'mustang','year':1964}
car_details.pop("year")
print(car_details)