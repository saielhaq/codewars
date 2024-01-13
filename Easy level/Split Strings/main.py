def solution(s):
    dae = ""
    if len(s) % 2 == 0:
        pass
    else:
        s += '_'
    
    for x in range(len(s)):
        if x % 2 == 0:
            dae += s[x]
        elif x % 2 == 1:
            dae += f"{s[x]},"
    
    s = dae.split(',')
    s.remove(s[len(s)-1])
    return s