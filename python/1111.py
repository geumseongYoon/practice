class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

def solution(prices):
    ansStack = Stack()
    for i in range(len(prices)):
        ansStack.push(0)
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                ansStack.stack[i] += 1
            else:
                ansStack.stack[i] += 1
                break

    answer = ansStack.stack
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))