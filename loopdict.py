# PRINT VALUES
car={"brand":"ford","model":"mustang","year":1964}
for i in car.values():
    print(i)

# PRINT VALUES 
car={"brand":"ford","model":"mustang","year":1964}
for i in car:
    print(car[i])

# PRINT KEYS
car={"brand":"ford","model":"mustang","year":1964}
for i in car:
    print(i)
    
# PRINT KEYS 
car={"brand":"ford","model":"mustang","year":1964}
for i in car.keys():
    print(i)
    
# EACH KEYS WITH ITS ITEM/VALUE
car={"brand":"ford","model":"mustang","year":1964}
for i,j in car.items():
    print(i,j)
    
car={"brand":"ford","model":"mustang","year":1964}
print(car["model"])