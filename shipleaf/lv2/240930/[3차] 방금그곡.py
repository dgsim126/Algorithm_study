def solution(m, musicinfos):
    answer = ''
    lyrics = []
    title = []
    for i in musicinfos:
        minute = (int(i.split(',')[1][0:2]) * 60 + int(i.split(',')[1][3:5])) - (int(i.split(',')[0][0:2]) * 60 + int(i.split(',')[0][3:5]))
        lyric = (i.split(',')[3] * (14 // len(i.split(',')[3]) + 1))[:minute]
        lyrics.append(lyric)
        title.append(i.split(',')[3])
    for i in range(len(lyrics)):
        if findSong(m, lyrics[i]):
            answer = title[i]
    return answer

def findSong(m, lyric):
    for i in range(len(lyric)-1):
        if (lyric[i]+lyric[i+1]) == (m[i]+m[i+1]):
            index = i
            while True:
                if index+2 < len(lyric) - 1:
                    if lyric[index+2] == m[index+2]:
                        index += 1
                    elif lyric[index+2] != m[index+2]:
                        break
                else:
                    if index + 2 == len(m) - 1:
                        return True
                    else:
                        break
    return False


solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])

