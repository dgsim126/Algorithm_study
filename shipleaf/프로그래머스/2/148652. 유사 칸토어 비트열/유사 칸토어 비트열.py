def solution(n, l, r):
    def count_ones(level, left, right):
        if level == 0:  # 기본 케이스
            return 1 if left <= 1 <= right else 0

        # 현재 비트열의 길이와 각 부분의 길이
        length = 5 ** level
        part_length = length // 5

        # 각 구간의 시작과 끝
        parts = [
            (1, part_length),
            (part_length + 1, 2 * part_length),
            (2 * part_length + 1, 3 * part_length),
            (3 * part_length + 1, 4 * part_length),
            (4 * part_length + 1, 5 * part_length)
        ]

        total_ones = 0
        for i, (start, end) in enumerate(parts):
            # 현재 구간이 전체 구간 [left, right]와 겹치는 경우
            if left > end or right < start:
                continue  # 겹치지 않으면 무시
            if i == 2:  # 가운데 구간은 모두 0
                continue
            # 겹치는 구간 계산
            new_left = max(left, start) - start + 1
            new_right = min(right, end) - start + 1
            total_ones += count_ones(level - 1, new_left, new_right)

        return total_ones

    return count_ones(n, l, r)
