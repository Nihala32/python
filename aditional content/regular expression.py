# regular expression
# .................
# python package
# for pattern matching
# string
# it is used for string validation (rule)


# finditer
# .........
# finditer(argmnt1,argmnt2)
# argmnt1:find_pattern
# argmnt2:string_name

import re
s="ababbaaababaaab"
count=0
# ab
matcher=re.finditer('ab',s)
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())   #i.start=print index of the pattern
print(count)

# hacker rank








