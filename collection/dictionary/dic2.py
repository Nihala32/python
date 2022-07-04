# name
# age
# prof
# salary
#
# name to first name
# print prof value
# check company present
# add company
# add salary 5000
# print key value seperatly

dic={"name":'vinay',"age":25,"prof":'bigdata',"salary":2500}
dic["first_name"]=dic["name"]
del dic["name"]
print(dic)
print(dic["prof"])
if("company " in dic):
    pass
else:
    dic["company"]='luminar'
dic["salary"]+=5000
for i in dic:
    print(i,dic[i])
