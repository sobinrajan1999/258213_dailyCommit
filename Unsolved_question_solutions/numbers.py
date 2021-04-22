num = "2 + 3i"
if num == 0:
    print("Zero")
elif type(num) == int:
    print("Real number")
elif type(num) == float:
    print("Float number")
elif '+' in num and 'i' in num:
    print("complex number")
else:
    print("string")
