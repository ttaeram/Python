class stack_commands():
    def push(self, x, stack):
        stack.append(x)

        return stack
    

    def pop(self, stack):
        if stack:
            n = stack.pop()
        
        else:
            n = -1

        return n, stack
    

    def size(self, stack):
        n = len(stack)

        return n
    

    def empty(self, stack):
        if stack:
            return 0
        
        else:
            return 1
        
    
    def top(self, stack):
        if stack:
            n = stack[-1]

            return n
        
        else:
            return -1


def init():
    stk_cmd = stack_commands()

    commands = {
        "push": stk_cmd.push,
        "pop": stk_cmd.pop,
        "size": stk_cmd.size,
        "empty": stk_cmd.empty,
        "top": stk_cmd.top
    }

    stack = []

    N = input_orders()

    for _ in range(N):
        command = input().strip()

        if "push" in command:
            command, x = map(str, command.split())
            stack = commands.get(command)(int(x), stack)
        
        elif "pop" in command:
            n, stack = commands.get(command)(stack)

            print(n)
        
        else:
            n = commands.get(command)(stack)

            print(n)


def input_orders():
    print("명령의 수 :", end = " ")

    N = int(input())

    return N


init()