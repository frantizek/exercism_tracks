def rotate(text: str, key:int) -> str:
    letters_rotated = []
    if len(text) <= 0:
        return ""
    else:
        for letter in text:
            if 65 <= ord(letter) <= 90:
                if ord(letter) + key > 90:
                    letters_rotated.append(chr(ord(letter) + key - (90-64) ))
                else:
                    letters_rotated.append(chr(ord(letter) + key))
            elif 97 <= ord(letter) <= 122:
                if ord(letter) + key > 122:
                    letters_rotated.append(chr(ord(letter) + key - (122-96)))                
                else:
                    letters_rotated.append(chr(ord(letter) + key))
            else:
                letters_rotated.append(letter)  

    return "".join(letter for letter in letters_rotated)
