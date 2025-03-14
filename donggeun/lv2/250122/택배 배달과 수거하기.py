# 무조건 먼 집부터 가는 것이 바람직

def solution(cap, n, deliveries, pickups):
    distance= 0

    while(deliveries and pickups):
        if(len(deliveries)==0): # 배달만 완료
            pickups += len(pickups) - 1
            pickups[-1] -= cap
            temp = pickups[-1]
            while (pickups[-1] <= 0):
                pickups.pop()
            pickups[-1] += cap

        elif(len(pickups)==0): # 수거만 완료
            distance += len(deliveries) - 1
            deliveries[-1] -= cap
            temp = deliveries[-1]
            while (deliveries[-1] <= 0):
                deliveries.pop()
            deliveries[-1] += cap

        else: # 배달, 수거 모두 미완료
            distance+=len(deliveries)-1
            deliveries[-1]-= cap
            temp= deliveries[-1]
            while(deliveries[-1]<=0):
                deliveries.pop()
            deliveries[-1]+= cap

            pickups[-1] -= cap
            temp = pickups[-1]
            while (pickups[-1] <= 0):
                pickups.pop()
            pickups[-1] += cap

    return distance

def solution_gpt(cap, n, deliveries, pickups):
    distance = 0

    # deliveries와 pickups 리스트가 비어있지 않은 동안 반복
    while deliveries or pickups:
        # 가장 먼 거리 계산
        max_distance = max(
            len(deliveries) if deliveries else 0,
            len(pickups) if pickups else 0
        )
        distance += max_distance * 2  # 왕복 거리 추가

        # 배달 작업
        carry = cap
        while deliveries and carry > 0:
            if deliveries[-1] <= carry:
                carry -= deliveries.pop()
            else:
                deliveries[-1] -= carry
                carry = 0

        # 수거 작업
        carry = cap
        while pickups and carry > 0:
            if pickups[-1] <= carry:
                carry -= pickups.pop()
            else:
                pickups[-1] -= carry
                carry = 0

    return distance



## main ##
cap= 4 # 트럭에 실을 수 있는 택배 상자 최대 개수
n= 5 # 배달할 집의 개수
deliveries= [1, 0, 3, 1, 2]
pickups= [0, 3, 0, 4, 0]
print(solution(cap, n, deliveries, pickups))