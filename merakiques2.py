# QUESTION NO.8

marks={}
for i in range(10):
    students_name=input("Enter the name of students:")
    students_mark=int(input("Enter the marks of students:"))
    marks[students_name]=students_mark
print(marks)

# QUESTION NO.9  
   
word = 'MISSISSIPPI'
d = {}
for i in word:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(str(d))


# QUESTION NO.10
# COUNT THE TOTVALUES\ 
dict={"Alex":["sub1","sub2","sub3"],"David":["sub1","sub2"]}
c=0
for i in dict.values():
    for j in i:
        c+=1
print(c)

# QUESTION NO.11
# PRINT THE TOP 3 HIGHEST VALUES OF A GIVEN DICTIONARY

# my_dict={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}
# list=[]
# for i in my_dict.values():
#     list.append(i)
# pr   NOT ODNE


# QUESTION NO.12
# WRITE A PROGRAM TO CREATE A DICTIONARY WITH ALL THE NUMBERS FROM 1 TO AS THE KEYS AND  THIER SAQUARE AS THE CORRESPONDING VALUES

a={}
for i in range(1,16):
    d=i**2
    a[i]=d
print(a)

# QUESTION NO.13
# PRINT THE HIGHEST 3 KEYS OF GIVEN DICTIONARY
# my_dict={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}

# QUESTION NO.14
# Write a program to sort a dictionary in ascending or descending according to its values 

a={'bijender':45,'deepak':60,'param':20,'anjil':30,'roshini':50}
# for key,value in a.items():