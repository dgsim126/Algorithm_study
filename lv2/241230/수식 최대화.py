# 어차피 연산자는 *,+,- 세 개니까 모든 경우의 수 6가지 구하고 비교
# google
def calc(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    return a * b

def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]

    ex = [] # 분리한 수, 연산자 담는 리스트
    tmp = '' # 숫자 누적을 위한 변수(2자리 수 이상일 경우 대비)
    for e in expression:
        if e.isdigit() == False: # 연산자일 경우 (isdigit() : 문자열이 숫자로만 구성되어 있는지 확인)
            ex.append(int(tmp)) # 누적된 수 append
            ex.append(e) # 연산자 append
            tmp = '' # 누적 수 초기화
            continue
        tmp += e # 숫자일 경우, 누적
    ex.append(int(tmp)) # 마지막 수 append

    answer = []
    for operation in operations: # 연산자 우선순위 조회
        tmp = ex[:] # ex 리스트 복사 (x[:] : 얕은 복사)
        p = 0 # 우선순위 연산자의 인덱스

        while len(tmp) > 1: # 리스트 1 될 때까지
            if operation[p] in tmp: # 리스트에 우선순위 연산자 있는 경우
                idx = tmp.index(operation[p]) # 해당 연산자의 위치 찾기

                tmp.insert(idx-1, calc(tmp[idx-1], tmp[idx+1], operation[p])) # 연산 수행, 리스트 가장 왼쪽에 결과 삽입 (연산자의 앞 뒤는 수이므로 +-1)

                # 가장 왼쪽의 연산 결과 빼고 연산에 사용된 좌변, 연산자, 우변 제거
                tmp.pop(idx)
                tmp.pop(idx)
                tmp.pop(idx)
            else:
                p += 1 # 연산자 더 없으면 다음순위 연산자

        answer.append(abs(tmp[0]))

    return max(answer)