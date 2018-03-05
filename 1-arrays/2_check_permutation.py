# O(j lg j + k lg k)
def check_permutation_slow(left, right):
    return sorted(left) == sorted(right)

# O(j + k + (j + k)) = #O(2j + 2k) = #O(j + k)
def check_permutation(left, right):
    left_letters = {}
    right_letters = {}
    
    for letter in left:
        left_letters[letter] = left_letters.get(letter, 0) + 1
    for letter in right:
        right_letters[letter] = right_letters.get(letter, 0) + 1
    
    return left_letters == right_letters

if __name__ == '__main__':
    print(check_permutation_slow('abcdef', 'bacfed'))
    print(check_permutation('abcdef', 'bacfed'))
