tower_amount = int(input())
tower_lst = [int(a) for a in input() if a.isdigit()]

stack = []
answer = []

for i in range(tower_amount):
    tower = tower_lst[i]

    if stack:
        while stack:
            if stack[-1][0] < tower:
                stack.pop()
                if len(stack) == 0:
                    answer.append(str(0))
                    
            elif stack[-1][0] >= tower:
                answer.append(str(stack[-1][1] + 1))
                break

        stack.append([tower, i])
    
    else:
        stack.append([tower, i])
        answer.append("0")

print(" ".join(answer))
