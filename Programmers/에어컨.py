def solution(temperature, t1, t2, a, b, onboard):
    arr = [[int(1e9)] * 51 for _ in range(1001)]

    arr[0][temperature + 10] = 0
    for t, c in enumerate(onboard[1:], 1):
        if c:
            mintemp = t1
            maxtemp = t2 + 1
        else:
            mintemp = -10
            maxtemp = 41
        
        for temp in range(mintemp, maxtemp):
            if temp == temperature:
                possible = [arr[t - 1][temp + 10]]
                if temp + 10 != 0:
                    possible.append(arr[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    possible.append(arr[t - 1][temp + 1 + 10])
                arr[t][temp + 10] = min(possible)
            
            elif temp > temperature:
                possible = [arr[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    possible.append(arr[t - 1][temp - 1 + 10] + a)
                if temp + 10 != 50:
                    possible.append(arr[t - 1][temp + 1 + 10])
                arr[t][temp + 10] = min(possible)
            
            elif temp < temperature:
                possible = [arr[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    possible.append(arr[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    possible.append(arr[t - 1][temp + 1 + 10] + a)
                arr[t][temp + 10] = min(possible)
    answer = min(arr[len(onboard) - 1])
    return answer

temperature = 28
t1 = 18
t2 = 26
a = 10
b = 8
onboard = [0, 0, 1, 1, 1, 1, 1]
print(solution(temperature, t1, t2, a, b, onboard))