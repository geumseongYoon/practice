answer = 0
def solution(scoville, K):
    scovilleSorted = sorted(scoville)
    # if len(scoville) <= 1:
    #     return -1
    # for i in range(len(scoville)):
    #     if scoville[i] < K:
            
    return scovilleSorted

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))