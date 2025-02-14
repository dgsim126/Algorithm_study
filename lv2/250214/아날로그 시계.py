# def solution(h1, m1, s1, h2, m2, s2):
#     start = s1 + 60 * m1 + 3600 * h1
#     end = s2 + 60 * m2 + 3600 * h2
#     print(start,end)
#     h_deg = h1 * 3600 * (1/120)
#     m_deg = m1 * 60 * (1/10)
#     s_deg = s1 * 6
#     count = 0

#     if s_deg == m_deg or s_deg == h_deg:
#         count += 1

#     for i in range(start, end):
#         if m_deg == 360:
#             m_deg = 0
#         if s_deg == 360:
#             s_deg = 0
#         if h_deg == 360:
#             h_deg = 0
        
#         next_h_deg = h_deg + (1/120)
#         next_m_deg = m_deg + (1/10)
#         next_s_deg = s_deg +6

#         if s_deg < m_deg and next_s_deg >= next_m_deg:
#             count += 1
#         elif s_deg< h_deg and next_s_deg >= next_h_deg:
#             count += 1

#         s_deg += 6
#         m_deg += (1/10)
#         h_deg += (1/120)

#     return count

# print(solution(0,5,30,0,7,0))


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    startTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2  

    if startTime == 0 * 3600 or startTime == 12 * 3600:
        answer += 1

    while startTime < endTime:
        hCurAngle = startTime / 120 % 360
        mCurAngle = startTime / 10 % 360
        sCurAngle = startTime * 6 % 360

        hNextAngle = 360 if (startTime + 1) / 120 % 360 == 0 else (startTime + 1) / 120 % 360
        mNextAngle = 360 if (startTime + 1) / 10 % 360 == 0 else (startTime + 1) / 10 % 360
        sNextAngle = 360 if (startTime + 1) * 6 % 360 == 0 else (startTime + 1) * 6 % 360

        if sCurAngle < hCurAngle and sNextAngle >= hNextAngle:
            answer += 1
        if sCurAngle < mCurAngle and sNextAngle >= mNextAngle:
            answer += 1
        if sNextAngle == hNextAngle and hNextAngle == mNextAngle:
            answer -= 1

        startTime += 1
    
    return answer