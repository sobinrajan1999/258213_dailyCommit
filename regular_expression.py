import re
pattern = r"spam"
print(pattern)
if(re.match(pattern,"spamspamspam")):
    print("match")
else:
    print("no match")

if re.search(pattern,"eggspamsausage"):
    print("match")
else:
    print("not maych")

if re.findall(pattern,"eggspamsausage"):
    print("match")
else:
    print("not match")

match = re.search(pattern,"eggspamsausage")
print(match.group())
print(match.start())
print(match.end())
print(match.span())


str = "My name is Sobin. Hi Sobin"
pattern = r"Sobin"
print(re.sub(pattern,"Rajan",str))


# META CHARACTER
pattern = r"gr.y"
if re.match(pattern,"grey"):
    print("match1")
if re.match(pattern,"gray"):
    print("match2")
if re.match(pattern, "blue"):
    print("match3")

print("metacharacter")
pattern = r"^gr.y$"
if re.match(pattern,"grey"):
    print("match1")
if re.match(pattern,"stinggrays"):
    print("match2")
if re.match(pattern, "stinggrayfil"):
    print("match3")


# CHARACTER CLASSES
print("character classes")
pattern = r"[aeiou]"
if re.search(pattern,"grey"):
    print("mtach1")
if(re.search(pattern,"rhythm")):
    print("match")


pattern = r"[A-Z][a-z][0-9]"
#INVERSION
pattern = r"[^A-Z]"          #all characters other than A-Z

print("*********************")
pattern = r"egg+" # or pattern = r"egg+"
if re.search(pattern,"sausage"):
    print("mtach1")
if(re.search(pattern,"spameggsausageegg")):
    print("match2")



pattern = r"ice(-)?cream"
if re.search(pattern,"ice-cream"):
    print("mtach1")
if(re.search(pattern,"icecream")):
    print("match2")
if (re.search(pattern, "ice--cream")):
    print("match3")

print("more metacharacter")
pattern = r"^9{1,3}$"
if re.search(pattern,"9"):
    print("mtach1")
if(re.search(pattern,"999")):
    print("match2")
if (re.search(pattern, "9999")):
    print("match3")



# GROUP
print("group")
pattern = r"egg(spam)*"
if re.search(pattern,"egg"):
    print("mtach1")
if(re.search(pattern,"eggspamspamegg")):
    print("match2")
if (re.search(pattern, "spam")):
    print("match3")


print("another group")
pattern = r"a(bc)(de)(f(g)h)i"
match = re.search(pattern,'abcdefghijklmn')
print(match.group())
print(match.group(1))
print(match.group(0))
print(match.group(2))
print(match.groups())


print("more more more")
pattern = r"gr(a|e)y"
if re.search(pattern,"grey"):
    print("mtach1")
if(re.search(pattern,"gray")):
    print("match2")
if (re.search(pattern, "griy")):
    print("match3")



# SPECIAL CHARACTERS
print("special characters")
pattern = r"(\D+\d)"
if re.search(pattern," ! ?$"):
    print("mtach1")
if(re.search(pattern,"hi 999")):
    print("match2")
if (re.search(pattern, "1, 24, 46")):
    print("match3")

print("another special characters")
pattern = r"(\b(cat)\b)"
if re.search(pattern,"cat"):
    print("mtach1")
if(re.search(pattern,"hi catthere")):
    print("match2")
if (re.search(pattern, "we s>cat<tered")):
    print("match3")