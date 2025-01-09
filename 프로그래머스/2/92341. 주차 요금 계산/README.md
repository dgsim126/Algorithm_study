# [level 2] 주차 요금 계산 - 92341 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/92341) 

### 성능 요약

메모리: 10.6 MB, 시간: 4.56 ms

### 구분

코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 01월 10일 00:01:15

### 문제 설명

<h5 style="user-select: auto !important;">문제 설명</h5>

<p style="user-select: auto !important;">주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">요금표</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">기본 시간(분)</th>
<th style="user-select: auto !important;">기본 요금(원)</th>
<th style="user-select: auto !important;">단위 시간(분)</th>
<th style="user-select: auto !important;">단위 요금(원)</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">180</td>
<td style="user-select: auto !important;">5000</td>
<td style="user-select: auto !important;">10</td>
<td style="user-select: auto !important;">600</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">&nbsp;</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">입/출차 기록</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">시각(시:분)</th>
<th style="user-select: auto !important;">차량 번호</th>
<th style="user-select: auto !important;">내역</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">05:34</td>
<td style="user-select: auto !important;">5961</td>
<td style="user-select: auto !important;">입차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">06:00</td>
<td style="user-select: auto !important;">0000</td>
<td style="user-select: auto !important;">입차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">06:34</td>
<td style="user-select: auto !important;">0000</td>
<td style="user-select: auto !important;">출차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">07:59</td>
<td style="user-select: auto !important;">5961</td>
<td style="user-select: auto !important;">출차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">07:59</td>
<td style="user-select: auto !important;">0148</td>
<td style="user-select: auto !important;">입차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">18:59</td>
<td style="user-select: auto !important;">0000</td>
<td style="user-select: auto !important;">입차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">19:09</td>
<td style="user-select: auto !important;">0148</td>
<td style="user-select: auto !important;">출차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">22:59</td>
<td style="user-select: auto !important;">5961</td>
<td style="user-select: auto !important;">입차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">23:00</td>
<td style="user-select: auto !important;">5961</td>
<td style="user-select: auto !important;">출차</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">&nbsp;</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">자동차별 주차 요금</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">차량 번호</th>
<th style="user-select: auto !important;">누적 주차 시간(분)</th>
<th style="user-select: auto !important;">주차 요금(원)</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0000</td>
<td style="user-select: auto !important;">34 + 300 = 334</td>
<td style="user-select: auto !important;">5000 + <code style="user-select: auto !important;">⌈</code>(334 - 180) / 10<code style="user-select: auto !important;">⌉</code> x 600 = 14600</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0148</td>
<td style="user-select: auto !important;">670</td>
<td style="user-select: auto !important;">5000 +<code style="user-select: auto !important;">⌈</code>(670 - 180) / 10<code style="user-select: auto !important;">⌉</code>x 600 = 34400</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5961</td>
<td style="user-select: auto !important;">145 + 1 = 146</td>
<td style="user-select: auto !important;">5000</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">0000</code>번 차량은 18:59에 입차된 이후, 출차된 내역이 없습니다. 따라서, 23:59에 출차된 것으로 간주합니다.</li>
</ul></li>
<li style="user-select: auto !important;">00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다. </li>
<li style="user-select: auto !important;">누적 주차 시간이 <code style="user-select: auto !important;">기본 시간</code>이하라면, <code style="user-select: auto !important;">기본 요금</code>을 청구합니다.<br style="user-select: auto !important;"></li>
<li style="user-select: auto !important;">누적 주차 시간이 <code style="user-select: auto !important;">기본 시간</code>을 초과하면, <code style="user-select: auto !important;">기본 요금</code>에 더해서, 초과한 시간에 대해서 <code style="user-select: auto !important;">단위 시간</code> 마다 <code style="user-select: auto !important;">단위 요금</code>을 청구합니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">초과한 시간이 <code style="user-select: auto !important;">단위 시간</code>으로 나누어 떨어지지 않으면, <code style="user-select: auto !important;">올림</code>합니다.<br style="user-select: auto !important;"></li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">⌈</code>a<code style="user-select: auto !important;">⌉</code> : a보다 작지 않은 최소의 정수를 의미합니다. 즉, <code style="user-select: auto !important;">올림</code>을 의미합니다.</li>
</ul></li>
</ul>

<p style="user-select: auto !important;">주차 요금을 나타내는 정수 배열 <code style="user-select: auto !important;">fees</code>, 자동차의 입/출차 내역을 나타내는 문자열 배열 <code style="user-select: auto !important;">records</code>가 매개변수로 주어집니다. <strong style="user-select: auto !important;">차량 번호가 작은 자동차부터</strong> 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.</p>

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><p style="user-select: auto !important;"><code style="user-select: auto !important;">fees</code>의 길이 = 4</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">fees[0] = <code style="user-select: auto !important;">기본 시간(분)</code></li>
<li style="user-select: auto !important;">1 ≤ fees[0] ≤ 1,439 </li>
<li style="user-select: auto !important;">fees[1] = <code style="user-select: auto !important;">기본 요금(원)</code></li>
<li style="user-select: auto !important;">0 ≤ fees[1] ≤ 100,000</li>
<li style="user-select: auto !important;">fees[2] = <code style="user-select: auto !important;">단위 시간(분)</code></li>
<li style="user-select: auto !important;">1 ≤ fees[2] ≤ 1,439</li>
<li style="user-select: auto !important;">fees[3] = <code style="user-select: auto !important;">단위 요금(원)</code> </li>
<li style="user-select: auto !important;">1 ≤ fees[3] ≤ 10,000</li>
</ul></li>
<li style="user-select: auto !important;"><p style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">records</code>의 길이 ≤ 1,000</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">records</code>의 각 원소는 <code style="user-select: auto !important;">"시각 차량번호 내역"</code> 형식의 문자열입니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">시각</code>, <code style="user-select: auto !important;">차량번호</code>, <code style="user-select: auto !important;">내역</code>은 하나의 공백으로 구분되어 있습니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">시각</code>은 차량이 입차되거나 출차된 시각을 나타내며, <code style="user-select: auto !important;">HH:MM</code> 형식의 길이 5인 문자열입니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">HH:MM</code>은 00:00부터 23:59까지 주어집니다.</li>
<li style="user-select: auto !important;">잘못된 시각("25:22", "09:65" 등)은 입력으로 주어지지 않습니다.</li>
</ul></li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">차량번호</code>는 자동차를 구분하기 위한, `0'~'9'로 구성된 길이 4인 문자열입니다.<br style="user-select: auto !important;"></li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">내역</code>은 길이 2 또는 3인 문자열로, <code style="user-select: auto !important;">IN</code> 또는 <code style="user-select: auto !important;">OUT</code>입니다. <code style="user-select: auto !important;">IN</code>은 입차를, <code style="user-select: auto !important;">OUT</code>은 출차를 의미합니다. </li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">records</code>의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">records</code>는 하루 동안의 입/출차된 기록만 담고 있으며, 입차된 차량이 다음날 출차되는 경우는 입력으로 주어지지 않습니다.</li>
<li style="user-select: auto !important;">같은 시각에, 같은 차량번호의 내역이 2번 이상 나타내지 않습니다.</li>
<li style="user-select: auto !important;">마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.</li>
<li style="user-select: auto !important;">아래의 예를 포함하여, 잘못된 입력은 주어지지 않습니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">주차장에 없는 차량이 출차되는 경우</li>
<li style="user-select: auto !important;">주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우</li>
</ul></li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">fees</th>
<th style="user-select: auto !important;">records</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[180, 5000, 10, 600]</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]</code></td>
<td style="user-select: auto !important;">[14600, 34400, 5000]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[120, 0, 60, 591]</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]</code></td>
<td style="user-select: auto !important;">[0, 591]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[1, 461, 1, 10]</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">["00:00 1234 IN"]</code></td>
<td style="user-select: auto !important;">[14841]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;"><strong style="user-select: auto !important;">입출력 예 #1</strong></p>

<p style="user-select: auto !important;">문제 예시와 같습니다.</p>

<p style="user-select: auto !important;"><strong style="user-select: auto !important;">입출력 예 #2</strong></p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">요금표</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">기본 시간(분)</th>
<th style="user-select: auto !important;">기본 요금(원)</th>
<th style="user-select: auto !important;">단위 시간(분)</th>
<th style="user-select: auto !important;">단위 요금(원)</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">120</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">60</td>
<td style="user-select: auto !important;">591</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">&nbsp;</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">입/출차 기록</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">시각(시:분)</th>
<th style="user-select: auto !important;">차량 번호</th>
<th style="user-select: auto !important;">내역</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">16:00</td>
<td style="user-select: auto !important;">3961</td>
<td style="user-select: auto !important;">입차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">16:00</td>
<td style="user-select: auto !important;">0202</td>
<td style="user-select: auto !important;">입차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">18:00</td>
<td style="user-select: auto !important;">3961</td>
<td style="user-select: auto !important;">출차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">18:00</td>
<td style="user-select: auto !important;">0202</td>
<td style="user-select: auto !important;">출차</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">23:58</td>
<td style="user-select: auto !important;">3961</td>
<td style="user-select: auto !important;">입차</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">&nbsp;</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">자동차별 주차 요금</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">차량 번호</th>
<th style="user-select: auto !important;">누적 주차 시간(분)</th>
<th style="user-select: auto !important;">주차 요금(원)</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0202</td>
<td style="user-select: auto !important;">120</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3961</td>
<td style="user-select: auto !important;">120 + 1 = 121</td>
<td style="user-select: auto !important;">0 +<code style="user-select: auto !important;">⌈</code>(121 - 120) / 60<code style="user-select: auto !important;">⌉</code>x 591 = 591</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">3961</code>번 차량은 2번째 입차된 후에는 출차된 내역이 없으므로, 23:59에 출차되었다고 간주합니다. </li>
</ul>

<p style="user-select: auto !important;">&nbsp;</p>

<p style="user-select: auto !important;"><strong style="user-select: auto !important;">입출력 예 #3</strong></p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">요금표</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">기본 시간(분)</th>
<th style="user-select: auto !important;">기본 요금(원)</th>
<th style="user-select: auto !important;">단위 시간(분)</th>
<th style="user-select: auto !important;">단위 요금(원)</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">461</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">10</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">&nbsp;</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">입/출차 기록</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">시각(시:분)</th>
<th style="user-select: auto !important;">차량 번호</th>
<th style="user-select: auto !important;">내역</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">00:00</td>
<td style="user-select: auto !important;">1234</td>
<td style="user-select: auto !important;">입차</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">&nbsp;</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">자동차별 주차 요금</strong></li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">차량 번호</th>
<th style="user-select: auto !important;">누적 주차 시간(분)</th>
<th style="user-select: auto !important;">주차 요금(원)</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1234</td>
<td style="user-select: auto !important;">1439</td>
<td style="user-select: auto !important;">461 +<code style="user-select: auto !important;">⌈</code>(1439 - 1) / 1<code style="user-select: auto !important;">⌉</code>x 10 = 14841</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">1234</code>번 차량은 출차 내역이 없으므로, 23:59에 출차되었다고 간주합니다.</li>
</ul>

<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">​</p>

<h5 style="user-select: auto !important;">제한시간 안내</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">정확성 테스트 : 10초</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges