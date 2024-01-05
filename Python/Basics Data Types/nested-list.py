if __name__ == '__main__':
    records = []
    names = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    find_score = sorted(set(score for name, score in records))
    find_score = find_score[1]
    
    for name, score in records:
        if score == find_score:
            names.append(name)
        else: continue
        
    names.sort()
    print("\n".join(names))
