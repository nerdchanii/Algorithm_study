N = int(input()) # 입력 데이터 개수
tops = list(map(int,input().split())) # 공백 기준으로 리스트 만들기
answer = [0]  # 첫 번째 탑은 레이저를 수신받을 탑이 없으므로 0 출력
stack = [[0,tops[0]]]
for i in range(1, N): # 두 번째 탑부터 왼쪽 탑들이 레이저를 수신하는지 판단
    while stack:
        if stack[-1][1] > tops[i]: # stack[-1][1]값이 tops[i]보다 크거나 같으면 레이저를 수신
            answer.append(stack[-1][0]+1) # 레이저를 수신하는 탑의 번호를 answer에 추가하고 break
            break
        else: # stack[-1][1]값이 tops[i]보다 작으면 레이저를 수신하지 못하므로 stack에서 제거
            stack.pop()
        if len(stack) == 0: # stack에 값이 없으면 아무 탑도 레이저를 수신하지 못하므로 0 출력
            answer.append(0)
            break
    stack.append([i,tops[i]])

print(' '.join(map(str,answer))) # 공백을 추가해서 출력
