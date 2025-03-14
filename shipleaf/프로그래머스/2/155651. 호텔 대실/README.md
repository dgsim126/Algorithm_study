# [level 2] 호텔 대실 - 155651 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/155651) 

### 성능 요약

메모리: 10.5 MB, 시간: 1.68 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 02월 01일 19:37:33

### 문제 설명

<p style="user-select: auto !important;">호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.<br style="user-select: auto !important;">
예약 시각이 문자열 형태로 담긴 2차원 배열&nbsp;<code style="user-select: auto !important;">book_time</code>이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">book_time</code>의 길이 ≤ 1,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">book_time[i]</code>는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">[대실 시작 시각, 대실 종료 시각] 형태입니다.</li>
</ul></li>
<li style="user-select: auto !important;">시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예약 시각이 자정을 넘어가는 경우는 없습니다.</li>
<li style="user-select: auto !important;">시작 시각은 항상 종료 시각보다 빠릅니다.</li>
</ul></li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">book_time</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]</td>
<td style="user-select: auto !important;">3</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[["09:10", "10:10"], ["10:20", "12:20"]]</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]</td>
<td style="user-select: auto !important;">3</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<p style="user-select: auto !important;"><img src="https://user-images.githubusercontent.com/62426665/199907266-561e3b75-84eb-4da1-930c-a6ac8fa82a79.png" title="" alt="example1" style="user-select: auto !important;"><br style="user-select: auto !important;">
위 사진과 같습니다.</p>

<p style="user-select: auto !important;">입출력 예 #2</p>

<p style="user-select: auto !important;">첫 번째 손님이 10시 10분에 퇴실 후 10분간 청소한 뒤 두 번째 손님이 10시 20분에 입실하여 사용할 수 있으므로 방은 1개만 필요합니다.</p>

<p style="user-select: auto !important;">입출력 예 #3</p>

<p style="user-select: auto !important;">세 손님 모두 동일한 시간대를 예약했기 때문에 3개의 방이 필요합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges