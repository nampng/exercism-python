def CleanWord(word):
    word = word.strip("'")
    word = word.lower()
    return word

def CleanSentence(sentence):
    print(sentence)
    for char in sentence:
        if not (char.isalnum() or char == "'"):
            sentence = sentence.replace(char, ' ')
            
    sentence = sentence.split()
    print(sentence)
    return sentence

def count_words(sentence):
    word_dict = {}

    sentence = CleanSentence(sentence)
    
    for word in sentence:
        word = CleanWord(word)
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict
