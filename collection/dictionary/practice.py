# lst1=['name','age','profession','salary']
# lst2=['nihala',21,'python',5000]
#
# dic=dict(zip(lst1,lst2))   #zip function is used to aggregate two lists
# print(dic)

# dic1={'name':'nihala','age':21}
# dic2={'location':'kozhikode'}
# dic3={**dic1,**dic2}
# print(dic3)
#
# dic1={'maths':20,'english':25,'social':58}
#
# print(min(dic1,key=dic1.get))

dic={
    'e1':{"name":'lll','age':25},
    'e2':{"name":"kkk","age":41},
    'e3':{"name":"ppp","age":10}
}
dic['e2']['age']=21
print(dic)

dic1={'maths':20,'english':25,'social':58}