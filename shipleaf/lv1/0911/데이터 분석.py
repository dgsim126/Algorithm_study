# # 정확성 2점..

# def solution(data, ext, val_ext, sort_by):
#     answer = []
#     dic = {
#         "code": 0,
#         "date": 1,
#         "maximun": 2,
#         "remain": 3
#     }
#     arr = []
#     for i in data:
#         if i[dic[ext]] < val_ext:
#             arr.append(i)
#     print(arr)
#     if len(arr) <= 1:
#         answer = arr
#         return answer
#     answer.append(arr[0])
#     print(answer)
#     for i in range(1,len(arr)):
#         for j in range(len(answer)):
#             if arr[i][dic[sort_by]] < answer[j][dic[sort_by]]:
#                 answer.insert(j, arr[i])
#             if j == len(answer)-1 and arr[i][dic[sort_by]] > answer[j][dic[sort_by]]:
#                 answer.append(arr[i])
#             else:
#                 continue
#     return answer

### GPT

def solution(data, ext, val_ext, sort_by):

    dic = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    filtered_data = [i for i in data if i[dic[ext]] < val_ext]
    filtered_data.sort(key=lambda x: x[dic[sort_by]])
    
    return filtered_data

# 테스트
print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],"date",20300501,"remain"))