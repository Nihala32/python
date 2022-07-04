# a company decided to give bonus of 5% to employee is his year of service is more than 5 years
# ask user for their salary and yos and print the net bonus amount

salary=int(input("enter your salary: "))
yos=int(input("enter ur year of service: "))
bonus=salary*(5/100)
if(yos>5):
    print("your bonus is",bonus)
else:
    print("not eligible")