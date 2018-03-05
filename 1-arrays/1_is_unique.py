# Write a program to determine if a string has all unique characters

# O(n) time
# But O(n) space
def is_unique_map(word):
    letters_map = {}
    for letter in word:
        if letters_map.get(letter, False):
            return False
        else:
            letters_map[letter] = True
    return True

# O(n lg n) time
# Would be O(1) space if used in-place sort
def is_unique(word):
    word = sorted(word)
    for letter_index in range(1, len(word) - 1):
        if word[letter_index] == word[letter_index - 1]:
            return False
        elif word[letter_index] == word[letter_index + 1]:
            return False
    return True

if __name__ == '__main__':
    print(is_unique_map('help'))
    print(is_unique_map(''))
    print(is_unique_map('hell'))
    print(is_unique('help'))
    print(is_unique(''))
    print(is_unique('hell'))