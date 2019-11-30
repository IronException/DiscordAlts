
def is_in(word, msg):
    if not (word in msg):
        return False
    ind = msg.find(word)

    left = ind - 1 < 0 or not msg[ind - 1].isalpha()
    right = ind + len(word) >= len(msg) or not msg[ind + len(word)].isalpha()
    return left and right
