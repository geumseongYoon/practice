import collections

def unique_element(S):
    sum = 0
    for i in range(len(S)):
        if S.count(S[i]) == 1:
            sum += 1
    return sum

def solution(S):
    result = 0
    prev_result = 0
    element = collections.defaultdict(int)

    for i in range(len(S)):
        sub_i = S[i:]
        for j in range(len(S)-i):
            sub_S = sub_i[:j+1]
            S_value = element.get(sub_S[j])
            if S_value == None:
                S_value = 0

            if S_value > 2:
                result += prev_result
            else:
                S_value += 1
                element[sub_S[j]] += 1
                prev_result = (unique_element(sub_S))
                result += prev_result
        prev_result = 0
        element = collections.defaultdict(int)
    return result

S = 'ACAXA'
print(solution(S))