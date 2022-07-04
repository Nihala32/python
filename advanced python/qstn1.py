# # create a lst from element of range from 1200,2000 with step of 130
#
# # lst=[44,54,64,74,104]
# # create a lst with [50,60,70,80,110]
#
# # lst  1 to 50 print elements if  sqr>50
#
# lst=[i for i in range(1200,2000,130)]
# print(lst)
#
# lst1=[44,54,64,74,104]
# lst=[i+6 for i in lst1]
# print(lst)
#
# lst=[i for i in range(1,16) if i**2>50]
# print(lst)

dic={'sedan':1500,'suv':2000,'pickup':2500,'minivan':1600}

# wgt above 2000 print venicle name

lst=[i.upper() for i in dic if dic[i]>2000]
print(lst)

# print num div by 7
lst=[i for i in range(1,1001) if i%7==0]
print(lst)

# Find all of the numbers from 1-1000 that have a 3 in them
# Count the number of spaces in a string

lst=[i for i in range(1,1001) if '3' in str(i)]
print(lst)

# Count the number of spaces in a string
# Create a list of all the consonants in the string
data="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams "
v="aeiou"
lst=[i for i in data if i not in v]
print(lst)
count=0
for i in data:
    if(i.isspace()):
        count+=1
print(count)




