if __name__ == '__main__':
    records = []
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    find_score = sorted({score for name, score in records})
    find_score = find_score[1]

    names.extend(name for name, score in records if score == find_score)
    names.sort()
    print("\n".join(names))
