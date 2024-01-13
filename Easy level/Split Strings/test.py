s = 'abc'
a = []
if len(s) % 2 == 0:
    pass
else:
    s += '_'
s = list(s)
for x in range(len(a)):
    if x % 2 == 0:
        a.append
    elif x % 2 == 1:
        a.append(f"{s[x]},")
print(a)