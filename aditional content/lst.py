employee=['vinay','anu']
default={'designation':'bigdata','salary':25000}

# fromkeys: it return a dictionary with specified keys and specified values

res=dict.fromkeys(employee,default)
print(res)

print(res['vinay'])