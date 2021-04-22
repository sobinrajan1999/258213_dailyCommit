
dict_1 = {'one':1 , 'three':3 , 'two':2 , "four":4}
dict_2 = {'five':5 , 'six':6 , 'seven':7}

# Using |
merge_dict_1 = dict_1 | dict_2
print(merge_dict_1)

# Using ** method
merge_dict_2 = {**dict_1,**dict_2}
print(merge_dict_2)

#Using update method
dict_2.update(dict_1)
print(dict_2)

