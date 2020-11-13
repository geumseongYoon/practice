def solution(bridge_length, weight, truck_weights):
    answer = 0
    currentQueue = list()
    currentValue = list()

    while(len(truck_weights) or len(currentQueue)):
        popCheck = 0
        currentSum = 0
        whileBreak = 0
        for i in range(len(currentQueue)):
            if currentQueue[0] == bridge_length-1:
                currentQueue.pop(0)
                currentValue.pop(0)
                popCheck = 1
                if len(currentQueue) == 0:
                    whileBreak = 1
            else:
                currentQueue[i-popCheck] += 1
                currentSum += currentValue[i-popCheck]

        if len(truck_weights) > 0:
            if (truck_weights[0] + currentSum) <= weight:
                currentQueue.append(0)
                currentValue.append(truck_weights.pop(0))

        if whileBreak == 1:
            continue

        # if len(truck_weights) or len(currentQueue):
        #     answer += 1
        answer += 1
        # print("currentQueue")
        # print(currentQueue)
        # print("currentValue")
        # print(currentValue)
    return answer

bridge_length = 5
weight = 10
truck_weights = [7, 4, 5, 6]

# bridge_length = 100
# weight = 100
# truck_weights = [10, 10]

# bridge_length = 100
# weight = 100
# truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(bridge_length, weight, truck_weights))