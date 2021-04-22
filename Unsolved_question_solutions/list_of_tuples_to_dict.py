# One way
print("1. One Way")
list_1 = [(1,2,3,4),('S','o','b','i','n'),(6,7,8,9,23),('sobin','rajan')]
dict_1 = {}
index = 1
for i in list_1:
    dict_1[index]=i
    index+=1
print(dict_1)

# Way two
print("\n2. Way two simple method")
list_2 = [("Ravi",93), ("Umang",45), ("Sid",65),("Yash",88), ("Vidisha",70), ("Bansal",52)]
dict_2 = {}
for i in list_2:
    dict_2[i[0]] = i[1]
print(dict_2)

# Way three
print("\n3. Way three (using dict() method)")
dict_3 = dict(list_2)
print(dict_3)


# WAY THREE
print("\n4. Way four (using setdefault() method)")
dict_4 = {}
for a,b in list_2:
    dict_4.setdefault(a,[]).append(b)
print(dict_4)