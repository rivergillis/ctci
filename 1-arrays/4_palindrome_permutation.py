def palindrome_permutation(word):
    # Something is a palindrome if every letter occurs an even number
    # of times
    # If the word is of an odd length, then one letter can occur an odd
    # number of times
    letters = {}
    spaces = 0

    for letter in word:
        if letter == ' ':
            spaces += 1
            continue
        letter = letter.upper()
        letters[letter] = letters.get(letter, 0) + 1
    
    is_odd = ((len(word) - spaces) % 2) == 0
    odd_counts = 0

    for letter, count in letters.items():
        if (count % 2) != 0:
            if is_odd and (odd_counts == 0):
                odd_counts += 1
            else:
                return False

    return True

if __name__ == '__main__':
    print(palindrome_permutation("tacsoscat"))