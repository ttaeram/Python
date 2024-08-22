import sys
input = sys.stdin.readline

N = int(input())
arr = {}
for _ in range(N):
    a, b, c = map(str, input().split())
    arr[a] = (b, c)

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(arr[root][0])
        preorder(arr[root][1])

def inorder(root):
    if root != '.':
        inorder(arr[root][0])
        print(root, end='')
        inorder(arr[root][1])

def postorder(root):
    if root != '.':
        postorder(arr[root][0])
        postorder(arr[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')