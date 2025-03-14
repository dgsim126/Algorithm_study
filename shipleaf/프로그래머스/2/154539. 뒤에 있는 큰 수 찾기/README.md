# [level 2] 뒤에 있는 큰 수 찾기 - 154539 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/154539) 

### 성능 요약

메모리: 74.8 MB, 시간: 308.15 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 02월 01일 21:21:47

### 문제 설명

<p style="user-select: auto !important;">정수로 이루어진 배열 <code style="user-select: auto !important;">numbers</code>가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.<br style="user-select: auto !important;">
정수 배열 <code style="user-select: auto !important;">numbers</code>가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">4 ≤ <code style="user-select: auto !important;">numbers</code>의 길이 ≤ 1,000,000

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">numbers[i]</code> ≤ 1,000,000</li>
</ul></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">numbers</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[2, 3, 3, 5]</td>
<td style="user-select: auto !important;">[3, 5, 5, -1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[9, 1, 5, 3, 6, 2]</td>
<td style="user-select: auto !important;">[-1, 5, 6, 6, -1, -1]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1<br style="user-select: auto !important;">
2의 뒷 큰수는 3입니다. 첫 번째 3의 뒷 큰수는 5입니다. 두 번째 3 또한 마찬가지입니다. 5는 뒷 큰수가 없으므로 -1입니다. 위 수들을 차례대로 배열에 담으면 [3, 5, 5, -1]이 됩니다.</p>

<p style="user-select: auto !important;">입출력 예 #2<br style="user-select: auto !important;">
9는 뒷 큰수가 없으므로 -1입니다. 1의 뒷 큰수는 5이며, 5와 3의 뒷 큰수는 6입니다. 6과 2는 뒷 큰수가 없으므로 -1입니다. 위 수들을 차례대로 배열에 담으면 [-1, 5, 6, 6, -1, -1]이 됩니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges