print("1. Using inbuild function: ")
set_1 = {23,456,567,234,45,679,234,3456,78,234,346,457,12,43456,124,2353,46,234,234}
print("maximum value is: {}\nminimum value is : {}".format(max(set_1),min(set_1)))

print("\n2. Using sort function: ")
result = sorted(set_1)
print("maximum value is: {}\nminimum value is : {}".format(result[-1],result[0]))

print("\nWithout inbuilt function (using loop): ")
min = 99999999
max = 0
for i in set_1:
    if i < min:
        min = i
    if i > max:
        max = i

print("maximum value is: {}\nminimum value is : {}".format(max,min))