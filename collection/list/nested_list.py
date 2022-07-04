
# nested list
lst=[[101,'arun','k',26,'bigdata',1000],
    [102,'amal','k',27,'python',1500],
    [103,'vishnu','e',26,'bigdata',1250],
    [104,'anoop','m',27,'python',2000],
    [105,'hari','r',25,'bigdata',1750],
    [106,'vinay','s',28,'bigdata',2500]]

for i in lst:
    print(i)

for i in lst:
    print(i[1],i[2],i[3],i[4])

# find first name,last name ,age,salary (if  age is above 27)

for i in lst:
    if(i[3]>27):
        print(i[1],i[2],i[3],i[4],i[5])

# find first name,last name ,age,salary (if  profession is bigdata)

for i in lst:
    if(i[4]=='bigdata'):
        print(i[1],i[2],i[3],i[5])

# salary above 1750 & age above 25

for i in lst:
    if(i[5]>1750) and (i[3]>25):
        print(i[1],i[2],i[4])


sum=0
for i in lst:
    sum+=i[5]
print(sum)

