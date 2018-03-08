# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
# one call to isSubstring
# e.g. "waterbottle" is a rotation of "erbottlewat"

def is_substring(left, right):
    return left in right

def is_rotation(left, right):
    return len(left) == len(right) and is_substring(left, right + right)

if __name__ == '__main__':
    print(is_rotation('waterbottle', 'erbottlewat'))
    print(is_rotation('five', 'five'))
    print(is_rotation('five', 'efiv'))
    print(is_rotation('five', 'ivef'))
    print(is_rotation('five', 'iefv'))