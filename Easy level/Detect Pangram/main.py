def is_pangram(s):
    letters = ""
    ascii = 0
    target = 2847
    sentence = s.lower()
    
    for element in sentence:
        if element.isalpha() and element not in letters:
            letters += element
            ascii += ord(element) 
            print(ord(element)) 

    print(letters)
    print(ascii)
            
    return ascii == target

is_pangram("The quick brown fox jumps over the lazy dog.")