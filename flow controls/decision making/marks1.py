sub1=int(input("enter your marks: "))
sub2=int(input("enter your marks: "))
sub3=int(input("enter your marks: "))
sub4=int(input("enter your marks: "))
total=sub1+sub2+sub3+sub4
print((total))

if(total>180):
    print("A+")
elif(160<=total<=179):
    print("A")
elif(140<=total<=159):
    print("B+")
elif(120<=total<=139):
    print("B")
elif(100<=total<=119):
    print("c+")
elif(80<=total<=99):
    print("c")
else:
    print("falied")