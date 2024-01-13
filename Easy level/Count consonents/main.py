import string
def ilyass(m):
    m = m.lower()
    s = "zrtypqsdfghjklmwxcvbn"
    c = 0
    for x in m:
        if x in s:
            c += 1
    return c

print(ilyass("h)=##llo w@orld"))           