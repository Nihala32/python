
master_string="abbcddeghgggt"
check_word="egg"
res=""
dic={}
for char in master_string:
    if char not in dic:
        dic[char]=1
    else:
        dic[char]+=1
print(dic)
for char in check_word:
    if char in check_word:
        count=dic.get(char)
        if count>0:
            res+=char
            dic[char]-=1
        else:
            break

print(res)

