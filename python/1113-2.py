


def solution(bridge_length, weight, truck_weights):
    answer = 0
    currentQueue = list()
    currentValue = list()
    while(len(truck_weights) or len(currentQueue)):
        currentSum = 0
        if len(currentQueue) > 0:
            if currentQueue[0] == (bridge_length-1):
                currentQueue.pop(0)
                currentValue.pop(0)
                continue

            for i in range(len(currentQueue)):
                currentQueue[i] += 1
                currentSum += currentValue[i]

        if len(truck_weights) > 0 and truck_weights[0] + currentSum <= weight:
            currentQueue.append(0)
            popWeight = truck_weights.pop(0)
            currentValue.append(popWeight)

        answer += 1
    answer += 1
    return answer


# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(bridge_length, weight, truck_weights))