class Luhn:
    def __init__(self, card_num:str):
        self.card_num = card_num

    def valid(self):
        clean_spaces_from_card_num = self.card_num.replace(" ", "")
        if len(clean_spaces_from_card_num) <= 1:
            return False
        else:
            try:
                list_of_numbers = [int(x) for x in clean_spaces_from_card_num]
            except ValueError:
                return False

            reversed_list = list_of_numbers[::-1]

            for number in range(1, len(reversed_list), 2):

                the_digit = reversed_list[number]
                double_the_number = the_digit * 2

                if double_the_number > 9:
                    double_the_number -= 9
                reversed_list[number] = double_the_number

            reverse_the_reversed_list_but_doubled = reversed_list[::-1]

            luhn_total = 0
            for luhn_number in reverse_the_reversed_list_but_doubled:
                luhn_total += luhn_number

            if luhn_total % 10 != 0:
                return False
            return True
