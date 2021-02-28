#프로그래머스 해시 전화번호목록
from itertools import combinations as c
def solution(phone_book):
    answer = True
    PB = sorted(phone_book, key = len)
    for (a,b) in c(PB, 2):
        if a == b[:len(a)]:
            answer = False
    return answer