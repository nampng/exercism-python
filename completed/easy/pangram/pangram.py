def is_pangram(sentence):
    alpha_dict = {}
    sentence = sentence.lower()

    for c in sentence:
        if c.isalpha():
            alpha_dict[c] = 1
    
    if len(alpha_dict) == 26:
        return True
    else:
        return False
