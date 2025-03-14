def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 문자 제거
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    result = ''
    for char in new_id:
        if char in allowed_chars:
            result += char
    new_id = result

    # 3단계: .. -> .
    temp = ''
    for i in range(len(new_id)):
        if i > 0 and new_id[i] == '.' and new_id[i - 1] == '.':
            continue
        temp += new_id[i]
    new_id = temp

    # 4단계: 양 끝 . 제거
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계: 빈 문자열
    if not new_id:
        new_id = 'a'

    # 6단계: 16자 이상
    if len(new_id) >= 16:
        new_id = new_id[:15]
    # 제거 후 마침표(.)가 끝에 위치한다면 제거
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계: 2자 이하
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

## main ##
new_id= "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))  # "bat.y.abcdefghi"
