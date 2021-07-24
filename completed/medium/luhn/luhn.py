class Luhn:
    def __init__(self, card_num):
        self.is_valid = False

        print(card_num)
        card_num = card_num.replace(' ', '')
        if card_num.isnumeric():
            card_num = list(map(int, card_num))
            if len(card_num) > 1:
                for i in range(len(card_num) - 2, -1, -2):
                    print(f"current num: {card_num[i]}")
                    product = card_num[i] * 2
                    print(product)
                    if product > 9:
                        product -= 9

                    card_num[i] = product
                
                sum = 0

                print(card_num)

                for num in card_num:
                    sum += int(num)
                
                print(sum)

                if sum % 10 == 0:
                    self.is_valid = True

    def valid(self):
        return self.is_valid
