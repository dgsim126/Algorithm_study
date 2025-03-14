def solution(data, ext, val_ext, sort_by):
    lst = []

    for i in range(len(data)):
        if(ext == "code" and data[i][0] < val_ext):
            lst.append(data[i])
        elif(ext == "date" and data[i][1] < val_ext):
            lst.append(data[i])
        elif(ext == "maximum" and data[i][2] < val_ext):
            lst.append(data[i])
        elif(ext == "remain" and data[i][3] < val_ext):
            lst.append(data[i])

    # sort_by 값에 따라 정렬
    if(sort_by == "code"):
        return sorted(lst, key=lambda x: x[0])  # 코드 정렬
    elif(sort_by == "date"):
        return sorted(lst, key=lambda x: x[1])  # 제조일 정렬
    elif(sort_by == "maximum"):
        return sorted(lst, key=lambda x: x[2])  # 최대수량 정렬
    elif(sort_by == "remain"):
        return sorted(lst, key=lambda x: x[3])  # 현재수량 정렬

# main
data = [[1, 20300104, 100, 80],  # 코드번호(code), 제조일(date), 최대수량(maximum), 현재수량(remain)
        [2, 20300804, 847, 37],
        [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"

print(solution(data, ext, val_ext, sort_by))
