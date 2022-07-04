# word count prgm

line='cat rat cat rat rat cat bus car bus car'
data=line.split(' ')
print(data)
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
       dic[i]+=1
print(dic)

