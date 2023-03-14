#usefulish functions

#returns the number of lines in a block of text input should be encased in triple quotes """
def num_of_lines(text):
    total = int(len(text) != 0)
    for i in range(len(text)):
        if text[i] == "\n":
            total += 1
    return total
