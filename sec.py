### 프로그래머스_스택/큐_기능개발
import math
def solution(progresses, speeds):
    q=[]
    answer=[]
    count=1
    for i in range(progresses):
        q.append(math.ceil((100-progresses[i]) / speeds[i]))
    
    for j in range(1,len(q)):
        if q[i-1] >= q[i]:
            q[i] = q[i-1]
            count += 1
        else:
            answer.append(count)
            count = 1
    answer.append(count)
    return answer
