# [level 1] 가장 많이 받은 선물 - 258712 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3) 

### 성능 요약

메모리: 10.6 MB, 시간: 17.28 ms

### 구분

코딩테스트 연습 > 2024 KAKAO WINTER INTERNSHIP

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 02월 15일 15:55:45

### 문제 설명

<p style="user-select: auto !important;">선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다. 당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">A</code>가 <code style="user-select: auto !important;">B</code>에게 선물을 5번 줬고, <code style="user-select: auto !important;">B</code>가 <code style="user-select: auto !important;">A</code>에게 선물을 3번 줬다면 다음 달엔 <code style="user-select: auto !important;">A</code>가 <code style="user-select: auto !important;">B</code>에게 선물을 하나 받습니다.</li>
</ul></li>
<li style="user-select: auto !important;">두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.</li>
<li style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">A</code>가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 <code style="user-select: auto !important;">A</code>의 선물 지수는 -7입니다. <code style="user-select: auto !important;">B</code>가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 <code style="user-select: auto !important;">B</code>의 선물 지수는 1입니다. 만약 <code style="user-select: auto !important;">A</code>와 <code style="user-select: auto !important;">B</code>가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면, 다음 달엔 <code style="user-select: auto !important;">B</code>가 <code style="user-select: auto !important;">A</code>에게 선물을 하나 받습니다.</li>
<li style="user-select: auto !important;"><strong style="user-select: auto !important;">만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.</strong></li>
</ul></li>
</ul>

<p style="user-select: auto !important;">위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 당신은 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶습니다.</p>

<p style="user-select: auto !important;">친구들의 이름을 담은 1차원 문자열 배열 <code style="user-select: auto !important;">friends</code> 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 <code style="user-select: auto !important;">gifts</code>가 매개변수로 주어집니다. 이때, 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">2 ≤ <code style="user-select: auto !important;">friends</code>의 길이 = 친구들의 수 ≤ 50

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">friends</code>의 원소는 친구의 이름을 의미하는 알파벳 소문자로 이루어진 길이가 10 이하인 문자열입니다.</li>
<li style="user-select: auto !important;">이름이 같은 친구는 없습니다.</li>
</ul></li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">gifts</code>의 길이 ≤ 10,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">gifts</code>의 원소는 <code style="user-select: auto !important;">"A B"</code>형태의 문자열입니다. <code style="user-select: auto !important;">A</code>는 선물을 준 친구의 이름을 <code style="user-select: auto !important;">B</code>는 선물을 받은 친구의 이름을 의미하며 공백 하나로 구분됩니다.</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">A</code>와 <code style="user-select: auto !important;">B</code>는 <code style="user-select: auto !important;">friends</code>의 원소이며 <code style="user-select: auto !important;">A</code>와 <code style="user-select: auto !important;">B</code>가 같은 이름인 경우는 존재하지 않습니다.</li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">friends</th>
<th style="user-select: auto !important;">gifts</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">["muzi", "ryan", "frodo", "neo"]</td>
<td style="user-select: auto !important;">["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]</td>
<td style="user-select: auto !important;">2</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">["joy", "brad", "alessandro", "conan", "david"]</td>
<td style="user-select: auto !important;">["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]</td>
<td style="user-select: auto !important;">4</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">["a", "b", "c"]</td>
<td style="user-select: auto !important;">["a b", "b a", "c a", "a c", "a c", "c a"]</td>
<td style="user-select: auto !important;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;"><strong style="user-select: auto !important;">입출력 예 #1</strong></p>

<p style="user-select: auto !important;">주고받은 선물과 선물 지수를 표로 나타내면 다음과 같습니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">↓준 사람 \ 받은 사람→</th>
<th style="user-select: auto !important;">muzi</th>
<th style="user-select: auto !important;">ryan</th>
<th style="user-select: auto !important;">frodo</th>
<th style="user-select: auto !important;">neo</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">muzi</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ryan</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">frodo</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">neo</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">-</td>
</tr>
</tbody>
      </table><table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">이름</th>
<th style="user-select: auto !important;">준 선물</th>
<th style="user-select: auto !important;">받은 선물</th>
<th style="user-select: auto !important;">선물 지수</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">muzi</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">-3</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ryan</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">2</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">frodo</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">neo</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">1</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;"><code style="user-select: auto !important;">muzi</code>는 선물을 더 많이 줬던 <code style="user-select: auto !important;">frodo</code>에게서 선물을 하나 받습니다.<br style="user-select: auto !important;">
<code style="user-select: auto !important;">ryan</code>은 선물을 더 많이 줬던 <code style="user-select: auto !important;">muzi</code>에게서 선물을 하나 받고, 선물을 주고받지 않았던 <code style="user-select: auto !important;">neo</code>보다 선물 지수가 커 선물을 하나 받습니다.<br style="user-select: auto !important;">
<code style="user-select: auto !important;">frodo</code>는 선물을 더 많이 줬던 <code style="user-select: auto !important;">ryan</code>에게 선물을 하나 받습니다.<br style="user-select: auto !important;">
<code style="user-select: auto !important;">neo</code>는 선물을 더 많이 줬던 <code style="user-select: auto !important;">muzi</code>에게서 선물을 하나 받고, 선물을 주고받지 않았던 <code style="user-select: auto !important;">frodo</code>보다 선물 지수가 커 선물을 하나 받습니다.</p>

<p style="user-select: auto !important;">다음달에 가장 선물을 많이 받는 사람은 <code style="user-select: auto !important;">ryan</code>과 <code style="user-select: auto !important;">neo</code>이고 2개의 선물을 받습니다. 따라서 2를 return 해야 합니다.</p>

<p style="user-select: auto !important;"><strong style="user-select: auto !important;">입출력 예 #2</strong></p>

<p style="user-select: auto !important;">주고받은 선물과 선물 지수를 표로 나타내면 다음과 같습니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">↓준 사람 \ 받은 사람→</th>
<th style="user-select: auto !important;">joy</th>
<th style="user-select: auto !important;">brad</th>
<th style="user-select: auto !important;">alessandro</th>
<th style="user-select: auto !important;">conan</th>
<th style="user-select: auto !important;">david</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">joy</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">brad</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">alessandro</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">conan</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">-</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">david</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">-</td>
</tr>
</tbody>
      </table><table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">이름</th>
<th style="user-select: auto !important;">준 선물</th>
<th style="user-select: auto !important;">받은 선물</th>
<th style="user-select: auto !important;">선물 지수</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">joy</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">-1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">brad</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">-1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">alessandro</td>
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">3</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">conan</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">-1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">david</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">0</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;"><code style="user-select: auto !important;">alessandro</code>가 선물을 더 많이 줬던 <code style="user-select: auto !important;">joy</code>, <code style="user-select: auto !important;">brad</code>, <code style="user-select: auto !important;">conan</code>에게서 선물을 3개 받습니다. 선물을 하나씩 주고받은 <code style="user-select: auto !important;">david</code>보다 선물 지수가 커 선물을 하나 받습니다.<br style="user-select: auto !important;">
<code style="user-select: auto !important;">david</code>는 선물을 주고받지 않았던 <code style="user-select: auto !important;">joy</code>, <code style="user-select: auto !important;">brad</code>, <code style="user-select: auto !important;">conan</code>보다 선물 지수가 커 다음 달에 선물을 3개 받습니다.<br style="user-select: auto !important;">
<code style="user-select: auto !important;">joy</code>, <code style="user-select: auto !important;">brad</code>, <code style="user-select: auto !important;">conan</code>은 선물을 받지 못합니다.</p>

<p style="user-select: auto !important;">다음달에 가장 선물을 많이 받는 사람은 <code style="user-select: auto !important;">alessandro</code>이고 4개의 선물을 받습니다. 따라서 4를 return 해야 합니다.</p>

<p style="user-select: auto !important;"><strong style="user-select: auto !important;">입출력 예 #3</strong></p>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">a</code>와 <code style="user-select: auto !important;">b</code>, <code style="user-select: auto !important;">a</code>와 <code style="user-select: auto !important;">c</code>, <code style="user-select: auto !important;">b</code>와 <code style="user-select: auto !important;">c</code> 사이에 서로 선물을 주고받은 수도 같고 세 사람의 선물 지수도 0으로 같아 다음 달엔 아무도 선물을 받지 못합니다. 따라서 0을 return 해야 합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges