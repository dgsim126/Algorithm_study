def solution(k, dungeons):
    def dfs(k, dungeons, is_visited, depth):
        if (depth > max_depth[0]):
            max_depth[0] = depth

        for i in range(len(dungeons)):
            if (is_visited[i] == True and dungeons[i][0] <= k):  # 방문 가능
                is_visited[i] = False
                # print("던전 방문: ", dungeons[i])
                # print("after: ", k-dungeons[i][1], dungeons, is_visited, depth)

                # print("")
                dfs(k - dungeons[i][1], dungeons, is_visited, depth + 1)

                is_visited[i] = True

    max_depth = [-1]
    is_visited = [True for _ in range(len(dungeons))]
    print(is_visited)

    dfs(k, dungeons, is_visited, 0)
    return max_depth[0]
