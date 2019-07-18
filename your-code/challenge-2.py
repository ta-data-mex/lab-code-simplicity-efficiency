def many(minlen, maxlen, many):
    todas = []
    for x in range(many):
        y = randomString(minlen, maxlen)
        todas.append(y)
    return todas

def randomString(minlen, maxlen):
    import random
    import string
    letterr = list(string.ascii_lowercase)
    for x in range(0,10):
        letterr.append(x) 
    rand = [str(random.choice(letterr)) for i in range(maxlen+1)]        
    return "".join(rand)
    
a = input('Enter minimum string length (between 1 and 12): ')
b = input('Enter maximum string length (between 1 and 12): ')
n = input('How many random strings to generate? ')

print(many(int(a), int(b), int(n)))