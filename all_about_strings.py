def all_about_strings(word):
    if len(word) > 2:
        # Add length of word, first and last letter to list.
        answers_list = [len(word), word[0], word[-1]]
        # Check if word length is even or odd to determine
        # middle letter/s
        if len(word) % 2 > 0:
            answers_list.append(word[int(len(word)/2)])
        else:
            answers_list.append(word[int(len(word)/2)-1:int(len(word)/2)+1])
        # Check if second character is in the rest of the string
        if word[1] in word[2:]:
            answers_list.append("@ index " + str(word[2:].index(word[1]) + 2))
        else:
            answers_list.append("not found")
        return answers_list
    return []
