
# dictionary

# 1.how to define

dic={}
print(type(dic))

# key value pairs
# roll:101
# name:vinay
# age:26
# depr:bigdata
# salary:1000

# key : roll,name,age,depr,salary
# values: 101,vinay,28,bigdata,1000

dic={"roll":101,"name":'vinay',"age":26,"depr":'bigdata',"salary":1000}
print(dic)
# 2.hetrogenous data supported
# 3.check duplicate
dic={"roll":101,"name":'vinay',"age":26,"marks":26}    #duplicate value support
print(dic)

dic={"roll":101,"name":'vinay',"age":26,"age":25}    #duplicate key does not support
print(dic)

# 4.insertion order presereved

# 5.dictionary mutable

