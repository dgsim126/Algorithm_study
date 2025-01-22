# gpt's help(key, value를 기준으로 dict 정렬하는 법 외워둘 것)
dic = {"apple": 3, "banana": 1, "cherry": 4, "date": 2}
new_dic= dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))


# 완전탐색 문제에서 조합이 많이 사용되고 있음
# from itertools import product 사용법 숙지할 것