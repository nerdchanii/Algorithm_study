import sys

n = int(sys.stdin.readline())
d = []
for i in range(n):
    a = sys.stdin.readline()
    d.append(a.rstrip())

for i in d:
    count = 0
    if (i[0] == ')') or (i[-1] == '(') or (i.count('(') != i.count(')')):
        print("NO")
        continue
    h = list(i)
    for j in range(len(i)):
        if h[0] == '(':
            del h[0]
            del h[h.index(')')]
            if len(h) == 0:
                print("YES")
                break
            else:
                continue
        else: 
            print("NO")
            break
