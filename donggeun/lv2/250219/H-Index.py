'''
무슨 말인지부터 이해가 안된다.
-- 대충 이해 했다.
h를 증가시키며 찾기?
'''


def solution(citations):
    n = len(citations)  # 논문 개수
    h = n

    can_miss = 0
    for i in range(h, -1, -1):
        # print(f"h={h}일때, {can_miss}번 조건에 안 맞아도 됨")
        cnt = 0  # miss 의 개수
        flag = 1
        for j in range(len(citations)):
            if (i > citations[j]):
                # print(f"{j}번째 값은 {citations[j]}, h={h}보다 작음")
                cnt += 1

            if (cnt > can_miss):  # 이거 부호 반대로 해서 틀렸음
                flag = 0
                break

        if (flag == 1):
            return i

        can_miss += 1