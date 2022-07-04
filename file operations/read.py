# read operation-within pycharm
#
# f=open("sample1","r")
#
# for i in f:
#     print(i)

# external source

# f=opem("file_path",

f=open("C:/Users/amina/Downloads/customer","r")
#
# for i in f:
#     data=i.rstrip("\n").split(",")
#     print(data)
    #fname,lmame,age
    # print(data[1],",",data[2],",",data[3])
# age above 50 fname,lname,age,pro
#
# for i in data:
#         if((data[3])>'50'):
#             print(data[1:5])
# # age above 50 & india(fname,lname,age,pro)
#
#         if(data[3]>'50') and data[-1]=='india':
#             print(data[1:5])
# each prof count
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    prof=data[4]
    if prof not  in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)

# each location count









