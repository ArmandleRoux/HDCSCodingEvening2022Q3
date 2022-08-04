def all_about_strings(word):
    if len(word) > 2:
        word_length = len(word)
        first_letter = word[0]
        last_letter = word[-1]
        # Check if word length is even or odd to determine
        # middle
        if len(word) % 2 > 0:
            middle_letter = word[int(len(word)/2)]
        else:
            middle_letter = word[int(len(word)/2)-1:int(len(word)/2)+1]
        # Check if second character is in the rest of the string
        if word[1] in word[2:]:
            index = "@ index " + str(word[2:].index(word[1]) + 2)
        else:
            index = "not found"
        return [word_length, first_letter, last_letter, middle_letter, index]
    return []
