pizza = int(input("Enter pizza slices you want: "))
if pizza %2==0:
    print("your price is : {}".format(pizza*120.00))
else:
    print("your price is : {}".format(pizza * 123.00))