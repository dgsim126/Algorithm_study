def solution(fees, records):
    answer = []
    dic = {}
    for record in records:
        time = record.split(" ")[0]
        number = record.split(" ")[1]
        inOut = record.split(" ")[2]
        if number not in dic:
            dic[number] = [[], 0]
            if inOut == "IN":
                dic[number][0].append(int(time.split(":")[0])*60 + int(time.split(":")[1]))
            else:
                int(time.split(":")[0])*60 + int(time.split(":")[1])
                dic[number][1] += int(time.split(":")[0])*60 + int(time.split(":")[1]) - dic[number][0].pop(0)
        else:
            if inOut == "IN":
                dic[number][0].append(int(time.split(":")[0])*60 + int(time.split(":")[1]))
            else:
                int(time.split(":")[0])*60 + int(time.split(":")[1])
                dic[number][1] += int(time.split(":")[0])*60 + int(time.split(":")[1]) - dic[number][0].pop(0)
    sorted_dic = dict(sorted(dic.items()))
    for key, values in sorted_dic.items():
        if values[0] != []:
            values[1] += 1439 - values[0].pop(0)
        if values[1] <= fees[0]:
            fee = fees[1]
            answer.append(fee)
            continue
        if (values[1] - fees[0])//fees[2] != (values[1] - fees[0])/fees[2]:
            fee = fees[1] + (int((values[1] - fees[0])//fees[2])+1)*fees[3]
        else:
            fee = fees[1] + int((values[1] - fees[0])//fees[2])*fees[3]
        answer.append(fee)
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))