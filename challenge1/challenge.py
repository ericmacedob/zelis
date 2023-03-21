def num_parser(textnum):
    units = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
        'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19
    }
    tens = {
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
        'seventy': 70, 'eighty': 80, 'ninety': 90
    }
    multipliers = {
        'hundred': 100, 'thousand': 1000, 'million': 1000000
    }

    sign = 1
    words = textnum.split()
    current = result = 0

    for word in words:
        if word == 'negative':
            sign = -1
        elif word in units:
            current += units[word]
        elif word in tens:
            current += tens[word]
        elif word in multipliers:
            scale = multipliers[word]
            result += current * scale
            current = 0
        elif word == 'and':
            pass
        else:
            raise ValueError("Invalid number: " + textnum)

    return (result + current) * sign

if __name__ == '__main__':
    arr = ['six', 'negative seven hundred twenty nine', 'one million one hundred one']
    answer = []
    for elem in arr:
        num = num_parser(elem)
        answer.append(num)

    print(answer)
