string = input()
bomb = input()
stack = ''

while True:
    if bomb in string:
        arr = string.split(bomb)
        string = ''
        for n in arr:
            string += n
    else:
        if len(string) > 0:
            print(string)
            break
        else:
            print('FRULA')
            break