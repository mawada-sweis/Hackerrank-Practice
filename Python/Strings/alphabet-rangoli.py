def print_rangoli(size):
    letter = 97 + size - 1
    output = []
    for i in range(1, size+1):
        sub_letter = letter
        line = []
        for j in range(1, i+1):
            line.append(chr(sub_letter))
            if j != i:
                sub_letter -= 1

        for _ in range(1, i):
            sub_letter += 1
            line.append(chr(sub_letter))

        output.append(line)
    for i in range(size-1, 0, -1):
        sub_letter = letter
        line = []
        for j in range(1, i+1):
            line.append(chr(sub_letter))
            if j != i:
                sub_letter -= 1

        for _ in range(1, i):
            sub_letter += 1
            line.append(chr(sub_letter))

        output.append(line)


    taller = len(output[size-1])

    for item in output:
        print('-'.join(item).center(size * 4 - 3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)