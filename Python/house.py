def recite(start_verse, end_verse):
    verses = [
        ("the house", "that Jack built"), # 1
        ("the malt", "that lay"),
        ("the rat", "that ate"),
        ("the cat", "that killed"),
        ("the dog", "that worried"),
        ("the cow with the crumpled horn", "that tossed"),
        ("the maiden all forlorn", "that milked"),
        ("the man all tattered and torn", "that kissed"),
        ("the priest all shaven and shorn", "that married"),
        ("the rooster that crowed in the morn", "that woke"),
        ("the farmer sowing his corn", "that kept"),
        ("the horse and the hound and the horn", "that belonged to") # 12
    ]
    result = []
    for i in range(start_verse, end_verse+1):
        verse = "This is " + str(verses[i-1][0])
        for j in range(i, 0, -1):
            if j == i:
                verse += " " + verses[j-1][1]
            elif j == 1 and i > 1:
                verse += " " + "in the house " + verses[j-1][1]
            else:
                verse += " " + verses[j-1][0] + " " + verses[j-1][1]
        verse += "."
        result.append(verse)
    return result