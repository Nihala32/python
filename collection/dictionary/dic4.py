pattern='abcdbcdef'
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        # dic[i]+=1
        print("first recursive char is",i)
        break
