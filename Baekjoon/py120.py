switch_N = int(input())
switch = list(map(int, input().split()))
student_N = int(input())
for n in range(student_N):
    student, button = map(int, input().split())
    button_idx = button - 1

    if student == 1:
        for sw in range(switch_N):
            if (sw + 1) % (button) == 0:
                if switch[sw] == 0:
                    switch[sw] = 1
                else:
                    switch[sw] = 0
    
    elif student == 2:
        if switch[button_idx] == 0:
            switch[button_idx] = 1
        else:
            switch[button_idx] = 0
        i = 1
        while button_idx - i >= 0 and button_idx + i < switch_N:
            # if button_idx != 0 or button_idx != (switch_N - 1):
            if switch[button_idx - i] == switch[button_idx + i]:
                if switch[button_idx - i] == 0:
                    switch[button_idx - i] = 1
                    switch[button_idx + i] = 1
                else:
                    switch[button_idx - i] = 0
                    switch[button_idx + i] = 0
            else:
                break
            i += 1

cnt = 0
for j in range(switch_N):
    if j != 0 and cnt % 20 == 0:
        print()
    print(switch[j], end = ' ')
    cnt += 1