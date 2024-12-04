alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nones    = [  0,   1,   3,  5,    7,   9,  11,  13,  15,  17,  19,  21,  23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]


def rows(letter:str):

    space = " "


    if len(letter) == 1 and letter.isalpha():     
        letter = letter.upper()
        
        size_of_diamond = alfabeto.index(letter)

        if size_of_diamond == 0:
            print(alfabeto[0])

        else:
            custom_diamond = []
            for index_current_letter in range(size_of_diamond):
                if index_current_letter==0:
                    custom_diamond.append(space*(nones[size_of_diamond+1-index_current_letter]//2) + alfabeto[index_current_letter] + space*(nones[size_of_diamond+1-index_current_letter]//2))
                else:    
                    custom_diamond.append(space*(nones[size_of_diamond+1-index_current_letter]//2) + alfabeto[index_current_letter] + space*nones[index_current_letter] + alfabeto[index_current_letter] + space*(nones[size_of_diamond+1-index_current_letter]//2))
            custom_diamond.append(alfabeto[size_of_diamond] + space * (nones[size_of_diamond+1]-2) + alfabeto[size_of_diamond])
            for reverse_index_current_letter in range(size_of_diamond-1, -1, -1):
                if reverse_index_current_letter==0:
                    custom_diamond.append(space*(nones[size_of_diamond+1-reverse_index_current_letter]//2) + alfabeto[reverse_index_current_letter] + space*(nones[size_of_diamond+1-reverse_index_current_letter]//2))
                else:
                    custom_diamond.append(space*(nones[size_of_diamond+1-reverse_index_current_letter]//2) + alfabeto[reverse_index_current_letter] + space*nones[reverse_index_current_letter] + alfabeto[reverse_index_current_letter] + space*(nones[size_of_diamond+1-reverse_index_current_letter]//2))

            return custom_diamond
