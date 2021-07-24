import re

def abbreviate(words):
    words = re.sub(r'[^a-zA-Z0-9\']', ' ', words)
    words = words.split()
    output = ''

    return output.join([word[0].upper() for word in words])
