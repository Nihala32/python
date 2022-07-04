str=""
spl="@#$%^&*(){}"
dic={}
f=open("file1","r")
for i in f:
    data=i.rstrip("/n")
    str+=i
str1=""
for i in str:
    if i not in spl:
        str1+=i
print(str1)
if i not in dic:
        dic[i]=1
else:
        dic[i]+=1
print(dic)

