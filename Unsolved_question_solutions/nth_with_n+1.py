list_1 = [1,2,3,4,5,6,7,8,9]
var = list_1[-1]
index = 8
for i in list_1[7::-1]:
    list_1[index] = i
    index-=1
list_1[0]=var
print(list_1)