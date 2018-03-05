# O(n)
def urlify(spaced_string, true_length):
    url = []
    length_left = true_length

    for letter in spaced_string:
        if letter != ' ':
            url.append(letter)
        else:
            url.append('%20')
        
        length_left -= 1
        if length_left <= 0:
            break
    
    return ''.join(url)

if __name__ == '__main__':
    print(urlify("Mr John Smith      ", 13))