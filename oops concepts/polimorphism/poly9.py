lst=[('vinay',45),('arjun',25),('amal',24)]
# print fname with highest mark
marks=[]
for i in lst:
    marks.append(i[1])
marks.sort()
print(marks)
max=max(marks)
for j in lst:
    if j[1]==max:
        print(j[0])

