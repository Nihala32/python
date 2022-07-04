# a student will not be allowded to sit in exam if his attendence is less than 75%
# take following input from user number of classes held,number of classes attended,and print percentage and
# student is allowded to sit in exam or not

held_clases=int(input("total number of classes: "))
attended_calsses=int(input("number of class attended: "))
percentage=(attended_calsses/held_clases*100)
print(percentage)
if(percentage>75):
    print("eligible for examination")
else:
    print("not eligible for examination")

