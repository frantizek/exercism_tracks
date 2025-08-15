def translate(original_text):

    def apply_rules(text):
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                      'k', 'l', 'm', 'n', 'p', 'q', 'r',
                      's', 't', 'v', 'w', 'x', 'y', 'z']

        first_vowel = 0
        found_first_vowel = False
        first_consonant = 0
        found_first_consonant = False

        for i in range(len(text)):
            if i != 0 and text[i] == "y" and not found_first_vowel:
                first_vowel = i
                found_first_vowel = True
            if text[i] in VOWELS and not found_first_vowel:
                first_vowel = i
                found_first_vowel = True
            if text[i] in CONSONANTS and not found_first_consonant:
                first_consonant = i
                found_first_consonant = True
            if found_first_consonant and found_first_vowel:
                break

        # print(f"Text : {text} with first vowel at {first_vowel} and first consonant at {first_consonant}")

        copy_of_text = text[:]

        # Rule 4
        # If a word starts with one or more consonants followed by "y",
        # first move the consonants preceding the "y" to the end of the word,
        # and then add an "ay" sound to the end of the word.

        if "y" in text and text[0] != "y" and text.index("y") <= first_vowel:
            location_of_y = text.index("y")
            initial_letters = text[0:location_of_y]
            only_consonants = all([c in CONSONANTS for c in initial_letters])
            if only_consonants:
                copy_of_text = copy_of_text[location_of_y:] + copy_of_text[0:location_of_y] + "ay"

        # Rule 3
        # If a word starts with zero or more consonants followed by "qu",
        # first move those consonants (if any) and the "qu" part to the end of the word,
        # and then add an "ay" sound to the end of the word.

        elif first_vowel > 0 and text[first_vowel] == "u" and text[first_vowel - 1] == "q":
            copy_of_text = copy_of_text[first_vowel + 1:] + copy_of_text[0:first_vowel + 1] + "ay"

        # Rule 1
        # If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

        elif first_vowel == 0 or text[0:2] == "xr" or text[0:2] == "yt":
            copy_of_text += "ay"

        # Rule 2
        # If a word begins with one or more consonants,
        # first move those consonants to the end of the word
        # and then add an "ay" sound to the end of the word.

        elif first_vowel > 0:
            copy_of_text = copy_of_text[first_vowel:] + copy_of_text[0:first_vowel] + "ay"

        return copy_of_text

    if " " in original_text:
        words = original_text.split(" ")
        new_words = []
        for word in words:
            new_words.append(apply_rules(word))
        return " ".join(new_words)
    else:
        return apply_rules(original_text)
