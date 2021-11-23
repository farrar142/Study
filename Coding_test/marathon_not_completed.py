participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    dict_1 = {}
    for i in participant:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1
    for i in completion:
        if i in dict_1:
            dict_1[i] -= 1
    for key in dict_1:
        if dict_1[key] != 0:
            return key

solution(participant,completion)