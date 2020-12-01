def solution(scoville, K):
    answer = 0
    flag = 0
    popCount = 0
    scovilleSorted = sorted(scoville)
    for i in range(len(scovilleSorted)):
        if scovilleSorted[i-popCount] > K:
            if flag >= 1:
                scovilleSorted.pop(i-popCount)
                popCount += 1
                continue
            else:
                flag += 1

    while(1):
        if len(scovilleSorted) <= 1:
            break
        for j in range(len(scovilleSorted)):
            if scovilleSorted[j] < K:
                firstValue = scovilleSorted.pop(0)
                secondValue = scovilleSorted.pop(0)
                calResult = firstValue + 2*secondValue
                if calResult < K:
                    scovilleSorted.append(calResult)
                    scovilleSorted = sorted(scovilleSorted)
                break

        answer += 1
    return answer

# scoville = [1, 2, 3, 9, 10, 12]
# K = 7
# print(solution(scoville, K))