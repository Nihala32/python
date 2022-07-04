# basic rules
# 1)
import re
count=0
rule='[0-9]'  #[^abc] = except abc [A-Z],[A-Za-z]
matcher=re.finditer(rule,'abc sabir@123')

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)

