
import re
a="cdfggfcdfcgdgfcdffdccddggfcd"
count=0
res=re.finditer("cd",a)
for i in res:
    count+=1
    print(i.group())
    print(i.start())
print(count)


master_string="abbcddeghgggt"
# chk wrd="egg"
