"""
Create an implementation of the Atbash cipher, an ancient encryption system created in the Middle East.

The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet
such that the resulting alphabet is backwards. The first letter is replaced with the last letter,
the second with the second-last, and so on.

An Atbash cipher for the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: zyxwvutsrqponmlkjihgfedcba

It is a very weak cipher because it only has one possible key, and it is a simple mono-alphabetic substitution cipher.
However, this may not have been an issue in the cipher's time.

cipher_text is written out in groups of fixed length, the traditional group size being 5 letters,
leaving numbers unchanged, and punctuation is excluded.
This is to make it harder to guess things based on word boundaries.
All text will be encoded as lowercase letters.

Examples
Encoding test gives gvhg
Encoding x123 yes gives c123b vh
Decoding gvhg gives test
Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog
"""


def encode(plain_text):
    """Endodes the text using the Atbash cipher."""
    plain_text = plain_text.lower()
    text = ''.join([letter for letter in plain_text if letter.isalnum()])
    current_group = 0
    cipher_text = ''
    for current_letter in text:
        if current_letter.isalpha():
            final_letter = chr(ord('a') + (25 - (ord(current_letter) - ord('a'))))
            cipher_text += final_letter
            current_group += 1
        else:
            cipher_text += current_letter
            current_group += 1

        if current_group == 5 :
            current_group = 0
            cipher_text += ' '
    return cipher_text.strip()



def decode(ciphered_text):
    """Decodes the text using the Atbash cipher."""
    ciphered_text = ciphered_text.lower()
    text = ''.join([letter for letter in ciphered_text if letter.isalnum()])
    decoded_text = ''
    for current_letter in text:
        if current_letter.isalpha():
            final_letter =chr(ord('a') + (25 - (ord(current_letter) - ord('a'))))
            decoded_text += final_letter
        else:
            decoded_text += current_letter
    return decoded_text