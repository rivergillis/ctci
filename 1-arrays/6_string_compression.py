# Implement a method to perform basic string compression using the counts of repeated chars.
# Ex: 'aabcccccaaa' -> 'a2b1c5a3'
# If the compressed string would not become smaller than the original string,
# return the original string. Assume has only uppercase and lowercase letters (a-z)

# O(n)
def compress(word):
    if not word:
        return ''

    compressed = []
    current_letter = word[0]
    current_count = 0

    # O(n)
    for letter in word:
        if letter != current_letter:
            compressed.append(current_letter + str(current_count))
            current_letter = letter
            current_count = 1
        else:
            current_count += 1
    
    compressed.append(current_letter + str(current_count))
    
    compressed_string = ''.join(compressed)

    if len(compressed_string) < len(word):
        return compressed_string
    else:
        return word
    

if __name__ == '__main__':
    print(compress('aabcccccaaa'))