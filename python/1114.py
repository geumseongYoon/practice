def solution(priorities, location):
    answer = 0
    currentQueue = list()
    for i in range(len(priorities)):
        currentQueue.append(i)
    while(len(priorities)):
        count = 0
        firstPriority = priorities[0]
        for j in range(len(priorities)):
            if j == 0:
                count += 1
                continue
            if firstPriority < priorities[j]:
                priorities.pop(0)
                firstIdx = currentQueue.pop(0)
                priorities.append(firstPriority)
                currentQueue.append(firstIdx)
                break
            else:
                count += 1
        if count == len(priorities):
            answer += 1
            if location == currentQueue[0]:
                break
            priorities.pop(0)
            currentQueue.pop(0)
    return answer

# priorities = [2, 1, 3, 2]
# location = 2

priorities = [1, 1, 9, 1, 1, 1]
location = 0


print(solution(priorities, location))