def solution(s):
    # s를 일단 리스트 등의 형태로 변경해야 함
    # s를 길이가 작은 순서대로 정렬
    # s를 돌며 s내부의 값이 결과가 저장된 result에 없다면 append

    lst= []
    current_array= []
    current_value= ""
    for i in range(1, len(s)-1):
        if(47<=ord(s[i])<=57):
            current_value+=s[i]
        elif(s[i]=="," and len(current_value)!=0):
            current_array.append(int(current_value))
            current_value= ""
        elif(s[i]=="}"):
            current_array.append(int(current_value))
            lst.append(current_array)
            current_array= []
            current_value= ""

    # print(lst) # [[4, 2, 3], [3], [2, 3, 4, 1], [2, 3]]

    lst= sorted(lst, key=len)
    # print(lst) # [[3], [2, 3], [4, 2, 3], [2, 3, 4, 1]]

    result_check= set()
    result= []

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            before= len(result_check)
            result_check.add(lst[i][j])
            after= len(result_check)

            if(before<after):
                result.append(lst[i][j])

    return result


## main ##
a= "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(a))