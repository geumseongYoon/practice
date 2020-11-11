# class Queue:
#     def __init__(self):
#         self.queue = list()
#
#     def enqueue(self, data):
#         self.queue.append(data)
#
#     def dequeue(self):
#         self.queue.pop(0)

def functionDevelop(progresses, speeds):
    answer = list()
    answerIncludeDay = list()
    answerIncludeDay.append(0)

    idx = 0
    while(len(progresses)):

        firstNum = progresses[0]
        if firstNum >= 100:
            answerIncludeDay[idx] += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            answerIncludeDay.append(0)
            idx += 1
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

    for i in range(len(answerIncludeDay)):
        if answerIncludeDay[i] != 0:
            answer.append(answerIncludeDay[i])

    return answer

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(functionDevelop(progresses, speeds))