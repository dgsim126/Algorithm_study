# 딕셔너리에 넣고 그리디

def solution(k, tangerine):
    dic= {}
    cnt=0

    for size in tangerine:
        if size in dic.keys():
            dic[size]+=1
        else:
            dic[size]= 1

    # print(dic)

    # gpt's help(key, value를 기준으로 dict 정렬하는 법 외워둘 것)
    new_dic= dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    # print(new_dic)

    for key, value in new_dic.items():
        # print(key, value)
        k-=value
        cnt+=1

        if(k<=0):
            return cnt



## main ##
k= 6
tangerine= [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))