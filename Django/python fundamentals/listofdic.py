result= [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]

# win % of tvm
# for results in results:
#     if results['district']=="tvm":
#         print(results['win'])
tvm=[result["win"] for result in result if result["district"]=="tvm"]
print(tvm)

# district with highest win %
# map,filter,reduce
result.sort(key=lambda fw:fw["win"],reverse=True)
print(result)

print(max(result,key=lambda res:res["win"]))

print(max(result,key=lambda res:res["A+"]))
print(max(result,key=lambda res:res["win"]))

# total A+
aplus=sum([result["A+"] for result in result])
print(aplus)




