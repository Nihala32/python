f=("C:/Users/amina/Downloads/temper","r")
dic={}
for i in f:
    data=i.rstrip("/n").split(",")
    dist=data[0]
    temp=data[1]
    if dist not in dic:
         dic[dist]=temp
    else:
          old_temp=dic[dist]



