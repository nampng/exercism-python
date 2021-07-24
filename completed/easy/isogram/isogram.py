def is_isogram(string):
    char_dict = {}
    for c in string.lower():
        if c.isalnum():
            if c in char_dict:
                return False
            else:
                char_dict[c] = 1
    return True
