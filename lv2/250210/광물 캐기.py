def solution(picks, minerals):
    g_minerals = []
    for i in range(0, len(minerals), 5):
        g_minerals.append(minerals[i:i+5])

    gm_count = []
    for gm in g_minerals:
        diamond_count = gm.count("diamond")
        iron_count = gm.count("iron")
        stone_count = gm.count("stone")

        gm_count.append([diamond_count, iron_count, stone_count, gm])

    gm_count.sort(reverse=True)

    total_pirodo = 0
    pick_i = 0

    # gpt ---------------------------------
    # 곡괭이 리스트
    available_picks = (["diamond"] * picks[0] +
                       ["iron"] * picks[1] +
                       ["stone"] * picks[2])

    for d, i, s, gm in gm_count:  # 정렬된 광물 그룹을 순서대로 처리
        if pick_i >= len(available_picks):  # 사용할 곡괭이가 없으면 종료
            break

        pick = available_picks[pick_i]  # 현재 곡괭이 선택
        pick_i += 1  # 다음 곡괭이로 이동

    # --------------------------------------
        for mineral in gm:
            if pick == "diamond":
                pirodo = 1

            elif pick == "iron":
                if mineral == "diamond":
                    pirodo = 5
                else:
                    pirodo = 1

            elif pick == "stone":
                if mineral == "diamond":
                    pirodo = 25
                elif mineral == "iron":
                    pirodo = 5
                else:
                    pirodo = 1

            total_pirodo += pirodo

    return total_pirodo