# [level 2] 유사 칸토어 비트열 - 148652 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/148652) 

### 성능 요약

메모리: 10.3 MB, 시간: 317.80 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 01월 20일 19:15:28

### 문제 설명

<p style="user-select: auto !important;">수학에서 칸토어 집합은 0과 1 사이의 실수로 이루어진 집합으로, [0, 1]부터 시작하여 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만들어집니다.</p>

<p style="user-select: auto !important;">남아는 칸토어 집합을 조금 변형하여 유사 칸토어 비트열을 만들었습니다. 유사 칸토어 비트열은 다음과 같이 정의됩니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">0 번째 유사 칸토어 비트열은 "1" 입니다.</li>
<li style="user-select: auto !important;">n(1 ≤ n) 번째 유사 칸토어 비트열은 n - 1 번째 유사 칸토어 비트열에서의 1을 11011로 치환하고 0을 00000로 치환하여 만듭니다.</li>
</ul>

<p style="user-select: auto !important;">남아는 <code style="user-select: auto !important;">n</code> 번째 유사 칸토어 비트열에서 특정 구간 내의 1의 개수가 몇 개인지 궁금해졌습니다.<br style="user-select: auto !important;">
<code style="user-select: auto !important;">n</code>과 1의 개수가 몇 개인지 알고 싶은 구간을 나타내는 <code style="user-select: auto !important;">l</code>, <code style="user-select: auto !important;">r</code>이 주어졌을 때 그 구간 내의 1의 개수를 return 하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">n</code> ≤ 20</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">l</code>, <code style="user-select: auto !important;">r</code> ≤ 5<sup style="user-select: auto !important;"><code style="user-select: auto !important;">n</code></sup>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">l ≤ <code style="user-select: auto !important;">r</code> &lt; <code style="user-select: auto !important;">l</code> + 10,000,000</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">l</code>과 <code style="user-select: auto !important;">r</code>은 비트열에서의 인덱스(1-base)이며 폐구간 [l, r]을 나타냅니다.</li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">n</th>
<th style="user-select: auto !important;">l</th>
<th style="user-select: auto !important;">r</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">17</td>
<td style="user-select: auto !important;">8</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">2 번째 유사 칸토어 비트열은 "110<code style="user-select: auto !important;">11110110000011</code>01111011" 입니다. 음영 표시된 부분은 폐구간 [4, 17] 이며 구간 내의 1은 8개 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges