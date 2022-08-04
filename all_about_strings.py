def all_about_strings(word):
    if len(word) > 2:
        length = len(word)
        first = word[0]
        last = word[-1]
        if len(word) % 2 > 0:
            middle = word[int(len(word)/2)]
        else:
            middle = word[int(len(word)/2)-1:int(len(word)/2)+1]
        if word[1] in word[2:]:
            index = "@ index " + str(word[2:].index(word[1]) + 2)
        else:
            index = "not found"
        return [length, first, last, middle, index]
    return []
