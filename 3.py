def checkio(words):
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False
