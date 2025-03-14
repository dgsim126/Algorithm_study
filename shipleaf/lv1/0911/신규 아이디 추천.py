def solution(new_id):
    answer = ''
    arr = [
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","s","y","z",
        "0","1","2","3","4","5","6","7","8","9","0",
        "-","_","."
    ]
    str_lower = new_id.lower()
    arr2 = []

    for i in range(len(str_lower)):
        if str_lower[i] in arr:
            arr2.append(str_lower[i])
    print(arr2)
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))