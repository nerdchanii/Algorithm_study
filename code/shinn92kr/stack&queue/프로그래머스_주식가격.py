# CODE_01(정확성 pass, 효율성 fail)

def solution(prices):
    answer = []
    price_len = len(prices) - 1
    for idx, i in enumerate(prices):
        cnt = 0
        if idx == price_len:
            answer.append(0)
            break
        for j in prices[idx + 1:]:
            cnt += 1
            if i > j:
                break
        answer.append(cnt)
    return answer
    
# CODE_02(정확성 pass, 효율성 pass)

def solution(prices):
    price_len = len(prices)
    answer = [0] * price_len
    for i in range(price_len - 1):
        for j in range(i, price_len - 1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break
    return answer
