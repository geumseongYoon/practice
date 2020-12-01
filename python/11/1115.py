
def solution(scoville, K):
    answer = 0
    while(1):
        scovilleSorted = sorted(scoville)
        if len(scovilleSorted) <= 1:
            return -1
        elif scovilleSorted[0] < K:
            firstValue = scovilleSorted.pop(0)
            secondValue = scovilleSorted.pop(0)
            calResult = firstValue + 2*secondValue
            scovilleSorted.append(calResult)
            scoville = scovilleSorted
            print(scoville)

        else:
            return answer
        answer += 1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))