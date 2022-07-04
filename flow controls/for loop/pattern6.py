# 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range(5,0,-1): #5 4 3
    for j in range(i,0,-1): #5 4 3 2 1   5432
        print(i,end="")
    print()