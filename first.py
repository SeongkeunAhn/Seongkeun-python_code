#프로그래머스 해시 전화번호목록

from itertools import combinations as c
def solution(phone_book):
    answer = True
    PB = sorted(phone_book, key = len)
    for (a,b) in c(PB, 2):
        if a == b[:len(a)]:
            answer = False
    return answer

#%% 프로그래머스 해시 완주

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p != c:
            return p
    return participant[-1]

#%%