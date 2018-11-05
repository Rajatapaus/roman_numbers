pairs = [   ('I', 'V'),
            ('X', 'L'),
            ('C', 'D'),
            ('M',)
        ]

#variations is a list of (variation, value, level) tuples
variations = []
increment = 1
for idx, pair in enumerate(pairs):
    second_value = increment * 5

    for n in range(1, 3 +1):
        variations.append((pair[0] * n, increment * n, idx))

    if pair[0] != 'M':
        variations.append((pair[0] + pair[1], second_value - increment, idx))

        variations.append((pair[1], second_value, idx))

        for n in range(1, 3+1):
            variations.append((pair[1] + pair[0] * n, (increment * n) + second_value, idx))

        variations.append((pair[0] + pairs[idx+1][0], increment * 9, idx))

    increment *= 10

variations_first_items = list(map(lambda x: x[0], variations))

def roman_numeral_encode(number):
    '''number must be int and it's value under 4000 and above 0.
    returns string'''

    assert type(number) == int, 'number must be int'
    #symbol M works only for numbers under 4000
    assert number > 0 and number < 4000, 'number must be greater than 0 and smaller than 4000'

    result = []
    for idx, zipped in enumerate(zip(pairs, list(str(number))[::-1])):
        pair, n = zipped
        n = int(n)
        if n in range(1,3 +1):
            result.insert(0, pair[0] * n)
        elif n == 4:
            result += pair[0] + pair[1]
        elif n in range(5,8 +1):
            result.insert(0, pair[1] + pair[0] * (n-5))
        elif n == 9:
            #get the sumbol of the next pair
            result.insert(0, pair[0] + pairs[idx + 1][0])

    return ''.join(result)

def roman_numeral_decode(s):
    assert type(s) == str, 'input needs to be string'
    if not s:
        return None

    s = s.upper()

    number = 0
    itr = 0
    while len(s) >= 1:
        #itr is also level
        print('ccc')
        for n in range(1,4 +1)[::-1]:
            break_loop = False

            while itr < 4 or break_loop:
                try:
                    print('bb')
                    #look one letter further
                    current_variation = s[-n:]
                    for variation in variations:
                        if current_variation == variation[0] and itr == variation[2]:
                            number += variation[1]
                            break_loop = True
                            print('true')
                            break
                    else:
                        print('aa')
                        itr += 1

                except:
                    pass
                if break_loop:
                    break
            if break_loop:
                break
        else:
            return None

        s = s[:-len(current_variation):]
        itr += 1

    return number


def encode_decode_test():
    for n in range(1,4000):
        print(n)
        encoded = roman_numeral_encode(n)
        print(encoded)
        decoded = roman_numeral_decode(encoded)
        print(decoded)
        if n != decoded:
            print('ERROR')
            break
        




if __name__ == '__main__':
    number = 4018
    s = 'XI'
    result = roman_numeral_decode(s)
    print(result)
    #encode_decode_test()
    #print(variations)