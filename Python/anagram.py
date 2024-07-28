def divide_and_conquer(word: str) -> str:
    word_with_order = []
    for letter in word.lower():
        word_with_order.append(letter)
    return ''.join(sorted(word_with_order))


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    valid_anagrams = []
    for candidate in candidates:
        if candidate.upper() == word.upper():
            # The exact word cannot be an anagram of itself.
            continue
        elif divide_and_conquer(candidate.upper()) == divide_and_conquer(word.upper()):
            valid_anagrams.append(candidate)
    return valid_anagrams
