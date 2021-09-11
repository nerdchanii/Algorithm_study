how_many = int(input())

for _ in range(how_many):
    brackets = input()
    counter = 0
    for bracket in brackets:
        if bracket == "(": counter += 1
        elif bracket == ")": counter -= 1

        if counter == -1: 
            print("NO")
            break

    if counter == 0:
        print("YES")
    elif counter > 0:
        print("NO")
