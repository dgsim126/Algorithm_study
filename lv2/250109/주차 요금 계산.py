def convert(num):
    time, minute= num.split(":")

    return int(time)*60 + int(minute)


def calculate(dict, set_):
    new_dict= {}

    for num in set_:
        for i in range(len(dict[num])//2):
            num2= dict[num].pop()
            num1= dict[num].pop()
            time= convert(num2)-convert(num1)

            if num not in new_dict:
                set_.add(num)
                new_dict[num] = time
            else:
                new_dict[num]=  new_dict[num]+time
    return new_dict # {'0148': 670, '0000': 334, '5961': 146}

def feeCal(dict, set_, fees):  # [180, 5000, 10, 600]
    result_dict = {}
    for num in set_:
        total_time = dict[num]
        if total_time <= fees[0]:  # 최소 요금인 경우
            result_dict[num] = fees[1]
        else:  # 추가 요금 계산
            temp_result = fees[1]
            total_time -= fees[0]
            temp_result += (total_time // fees[2]) * fees[3]
            if total_time % fees[2] > 0:  # 남은 시간 처리
                temp_result += fees[3]
            result_dict[num] = temp_result
    return result_dict



def solution(fees, records):
    dict= {}
    set_= set()

    # 딕셔너리에 넣기
    for i in range(len(records)):
        time, num, direct= records[i].split(" ")
        if num not in dict:
            set_.add(num)
            dict[num]= []
            dict[num].append(time)
        else:
            dict[num].append(time)

    # 출차 추가
    for num in set_:
        if(len(dict[num])%2!=0):
            dict[num].append("23:59")

    dict= calculate(dict, set_)
    dict= feeCal(dict, set_, fees)


    sorted_numbers = sorted(dict.keys())

    sorted_fees = []
    for num in sorted_numbers:
        sorted_fees.append(dict[num])

    return sorted_fees





## main ##
fees= [180, 5000, 10, 600]
records= ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))