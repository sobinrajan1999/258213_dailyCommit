tuple_1 = (1,1,1,2,2,2,3,3,4,5,7,8,9,3,4,5,3,4,7,8,4,2,5)
tuple_1 = sorted(tuple_1)

result = []
repeated = set()
for i in tuple_1:
    if i not in result:
        result.append(i)
    else:
        repeated.add(i)
print("Repeated items are: {}".format(repeated))