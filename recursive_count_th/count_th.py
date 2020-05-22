'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of
 ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    # If the word is a single letter
    if len(word) < 2:
        return 0
    # If the word is two letters
    # check to see if they match
    if len(word) == 2:
        if word[0] == 't':
            if word[1] == 'h':
                return 1
            else:
                return 0
        else:
            return 0
    # if it is bigger split it in half
    # check if the halves contain th
    # slide the half over one index and check again
    if len(word) > 2:
        count += count_th(word[:len(word)//2])
        count += count_th(word[len(word)//2:])
        count += count_th(word[len(word)//2-1:len(word)//2+1])
    return count


# print(count_th("abcthxyz"))
