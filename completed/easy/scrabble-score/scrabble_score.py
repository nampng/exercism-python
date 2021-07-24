score_dict = {
        'aeioulnrst' : 1,
        'dg' : 2,
        'bcmp' : 3,
        'fhvwy' : 4,
        'k': 5,
        'jx' : 8,
        'qz' : 10
    }

def score(word):
    word = word.lower()

    score = 0

    for c in word:
        for lis in score_dict:
            if c in lis:
                print(f'{c}: Adding {score_dict[lis]}')
                score += score_dict[lis]
    
    return score
