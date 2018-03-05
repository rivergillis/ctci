# Three types of edits can be performed on strings
# 1. Insert a character
# 2. Remove a character
# 3. Replace a character
#
# Given two strings, write a function to check if they are
# one edit (or zero edits) away


def one_away(before, after):
    if abs(len(before) - len(after)) >= 2:
        return False

    has_mismatched = False
    left_correction = 0
    right_correction = 0

    for index in range(min(len(before), len(after))):
        if index == len(before) - 1:
            left_correction = 0
        if index == len(after) - 1:
            right_correction = 0

        if before[index + left_correction] != after[index + right_correction]:
            if has_mismatched:
                return False
            else:
                has_mismatched = True

            # Letter mismatch, check if we can check the next letter
            if not ((index >= len(before) - 1) or (index >= len(after) - 1)):
                # we can check the next letter
                if before[index+1] == after[index]:
                    left_correction = 1
                elif before[index] == after[index+1]:
                    right_correction = 1
    
    if has_mismatched and left_correction == 0 and right_correction == 0 and len(before) != len(after):
        return False
    
    return True
                

if __name__ == '__main__':
    print(one_away('pale', 'ple')) # true
    print(one_away('pales', 'pale')) # true
    print(one_away('pale', 'bale')) # true
    print(one_away('pale', 'bake')) # false
    print(one_away('p', 'ab')) # false
    print(one_away('a', '')) # true
