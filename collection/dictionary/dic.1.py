dic={"roll":101,"name":'vinay',"age":26,"marks":30}
print(dic)
print(dic["marks"])
print(dic["name"])

dic["marks"]=40
dic["marks"]+=20
print(dic)
dic["name"]='luminar'

print(dic)
for i in dic:
    print(i,",",dic[i])

# add a key and value
dic["total"]=150
print(dic)

# delete
del dic["marks"]
print(dic)

print("name" in dic)
print("name" not  in dic)
print("total" in dic)

