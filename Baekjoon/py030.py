N = int(input())                #N에 입력받은 값 지정

for i in range(1, N+1):         #i 를 (1 ~ N)까지 해당
    print(" "*(N-i) + "*"*i)    #공백을 N-1만큼 출력한 후 *을 N만큼 출력