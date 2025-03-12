# chatgpt
def solution(n, arr1, arr2):
    answer = []
    arr1base2 = []
    arr2base2 = []

    for i in range(n):
        forarr1 = []
        forarr2 = []

        while arr1[i] > 0:
            forarr1.append(arr1[i] % 2)
            arr1[i] = arr1[i] // 2
        forarr1 += [0] * (n - len(forarr1))
        forarr1.reverse()
        arr1base2.append(forarr1)

        while arr2[i] > 0:
            forarr2.append(arr2[i] % 2)
            arr2[i] = arr2[i] // 2
        forarr2 += [0] * (n - len(forarr2))
        forarr2.reverse()
        arr2base2.append(forarr2)

    for i in range(n):
        smap = []
        for j in range(n):
            if arr1base2[i][j] == 1 or arr2base2[i][j] == 1:
                smap.append('#')
            else:
                smap.append(' ')
        answer.append(''.join(smap))

    return answer