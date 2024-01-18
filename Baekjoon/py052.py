alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

inp = input()
call_time = 0

for ind, alpha in enumerate(alphabet):
    for a in inp:
        if a in alpha:
            call_time += ind + 3

print(call_time)