# read a string from console
# apple
# remove vowels and add remaining letters to a string
# n=""
# print(type(n))
#
# str=""
# str1=input("enter a string: ")
# v="aeiouAEIOU"
# for i in str1:
#     if i not in v:
#         str+=i
# print(str)

# create a file file1
str=""
spl="#$%^&@*{}"
f=open("file1","r")
for i in f:
    data=i.rstrip("/n")
    str+=i
str1=""
for i in str:
    if i not in spl:
        str1+=i
print(str1)








