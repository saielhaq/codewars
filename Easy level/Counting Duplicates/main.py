def duplicate_count(text):
    s = 0
    text = text.lower()
    for x in text:
        if text.count(x) > 1:
            s += 1
            text = text.replace(x, '')
    return s