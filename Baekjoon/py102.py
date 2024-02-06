T = int(input())
for t in range(T):
    result = str(input())

    score = 0
    total = 0
    for n in range(len(result)):
        
        if result[n] == 'O':
            score += 1
            total += score

        elif result[n] == 'X':
            score = 0
    print(total)