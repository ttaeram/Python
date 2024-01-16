submit = []

for _ in range(28):
    n = int(input())
    submit.append(n)

submit = sorted(submit)
submit = set(submit)
student = list(range(1, 31))
student = set(student)

n_submit = student - submit
n_submit = sorted(n_submit)

for a in n_submit:
    print(a)