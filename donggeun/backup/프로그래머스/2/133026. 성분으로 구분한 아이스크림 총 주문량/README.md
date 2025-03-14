# [level 2] 성분으로 구분한 아이스크림 총 주문량 - 133026 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/133026) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2025년 02월 16일 14:48:15

### 문제 설명

<p style="user-select: auto !important;">다음은 아이스크림 가게의 상반기 주문 정보를 담은 <code style="user-select: auto !important;">FIRST_HALF</code> 테이블과 아이스크림 성분에 대한 정보를 담은 <code style="user-select: auto !important;">ICECREAM_INFO</code> 테이블입니다. <code style="user-select: auto !important;">FIRST_HALF</code> 테이블 구조는 다음과 같으며, <code style="user-select: auto !important;">SHIPMENT_ID</code>, <code style="user-select: auto !important;">FLAVOR</code>, <code style="user-select: auto !important;">TOTAL_ORDER</code> 는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을 나타냅니다. <code style="user-select: auto !important;">FIRST_HALF</code> 테이블의 기본 키는 <code style="user-select: auto !important;">FLAVOR</code>입니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="text-align: left; user-select: auto !important;">NAME</th>
<th style="text-align: left; user-select: auto !important;">TYPE</th>
<th style="user-select: auto !important;">NULLABLE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">SHIPMENT_ID</td>
<td style="text-align: left; user-select: auto !important;">INT(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">FLAVOR</td>
<td style="text-align: left; user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">TOTAL_ORDER</td>
<td style="text-align: left; user-select: auto !important;">INT(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;"><code style="user-select: auto !important;">ICECREAM_INFO</code> 테이블 구조는 다음과 같으며, <code style="user-select: auto !important;">FLAVOR</code>, <code style="user-select: auto !important;">INGREDITENT_TYPE</code> 은 각각 아이스크림 맛, 아이스크림의 성분 타입을 나타냅니다. <code style="user-select: auto !important;">INGREDIENT_TYPE</code>에는 아이스크림의 주 성분이 설탕이면 <code style="user-select: auto !important;">sugar_based</code>라고 입력되고, 아이스크림의 주 성분이 과일이면 <code style="user-select: auto !important;">fruit_based</code>라고 입력됩니다. <code style="user-select: auto !important;">ICECREAM_INFO</code>의 기본 키는 <code style="user-select: auto !important;">FLAVOR</code>입니다. <code style="user-select: auto !important;">ICECREAM_INFO</code>테이블의 <code style="user-select: auto !important;">FLAVOR</code>는 <code style="user-select: auto !important;">FIRST_HALF</code> 테이블의  <code style="user-select: auto !important;">FLAVOR</code>의 외래 키입니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="text-align: left; user-select: auto !important;">NAME</th>
<th style="text-align: left; user-select: auto !important;">TYPE</th>
<th style="user-select: auto !important;">NULLABLE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">FLAVOR</td>
<td style="text-align: left; user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">INGREDIENT_TYPE</td>
<td style="text-align: left; user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">문제</h5>

<p style="user-select: auto !important;">상반기 동안 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량을 총주문량이 작은 순서대로 조회하는 SQL 문을 작성해주세요. 이때 총주문량을 나타내는 컬럼명은 TOTAL_ORDER로 지정해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">FIRST_HALF</code> 테이블이 다음과 같고</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="text-align: left; user-select: auto !important;">SHIPMENT_ID</th>
<th style="text-align: left; user-select: auto !important;">FLAVOR</th>
<th style="user-select: auto !important;">TOTAL_ORDER</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">101</td>
<td style="text-align: left; user-select: auto !important;">chocolate</td>
<td style="user-select: auto !important;">3200</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">102</td>
<td style="text-align: left; user-select: auto !important;">vanilla</td>
<td style="user-select: auto !important;">2800</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">103</td>
<td style="text-align: left; user-select: auto !important;">mint_chocolate</td>
<td style="user-select: auto !important;">1700</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">104</td>
<td style="text-align: left; user-select: auto !important;">caramel</td>
<td style="user-select: auto !important;">2600</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">105</td>
<td style="text-align: left; user-select: auto !important;">white_chocolate</td>
<td style="user-select: auto !important;">3100</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">106</td>
<td style="text-align: left; user-select: auto !important;">peach</td>
<td style="user-select: auto !important;">2450</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">107</td>
<td style="text-align: left; user-select: auto !important;">watermelon</td>
<td style="user-select: auto !important;">2150</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">108</td>
<td style="text-align: left; user-select: auto !important;">mango</td>
<td style="user-select: auto !important;">2900</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">109</td>
<td style="text-align: left; user-select: auto !important;">strawberry</td>
<td style="user-select: auto !important;">3100</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">110</td>
<td style="text-align: left; user-select: auto !important;">melon</td>
<td style="user-select: auto !important;">3150</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">111</td>
<td style="text-align: left; user-select: auto !important;">orange</td>
<td style="user-select: auto !important;">2900</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">112</td>
<td style="text-align: left; user-select: auto !important;">pineapple</td>
<td style="user-select: auto !important;">2900</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;"><code style="user-select: auto !important;">ICECREAM_INFO</code> 테이블이 다음과 같다면</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="text-align: left; user-select: auto !important;">FLAVOR</th>
<th style="text-align: left; user-select: auto !important;">INGREDIENT_TYPE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">chocolate</td>
<td style="text-align: left; user-select: auto !important;">sugar_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">vanilla</td>
<td style="text-align: left; user-select: auto !important;">sugar_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">mint_chocolate</td>
<td style="text-align: left; user-select: auto !important;">sugar_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">caramel</td>
<td style="text-align: left; user-select: auto !important;">sugar_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">white_chocolate</td>
<td style="text-align: left; user-select: auto !important;">sugar_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">peach</td>
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">watermelon</td>
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">mango</td>
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">strawberry</td>
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">melon</td>
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">orange</td>
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">pineapple</td>
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">상반기에 아이스크림의 주 성분이 설탕인 아이스크림들에 대한 총주문량을 구하면 3,200 + 2,800 + 1,700 + 2,600 + 3,100 = 13,400입니다.  아이스크림의 주 성분이 과일인 아이스크림들에 대한 총주문량을 구하면 3,100 + 2,450 + 2,150 + 2,900 + 3,150 + 2,900 + 2,900 = 19,550입니다. 따라서 총주문량이 작은 순서대로 조회하는 SQL 문을 실행하면 다음과 같이 나와야 합니다. </p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="text-align: left; user-select: auto !important;">INGREDIENT_TYPE</th>
<th style="user-select: auto !important;">TOTAL_ORDER</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">sugar_based</td>
<td style="user-select: auto !important;">13400</td>
</tr>
<tr style="user-select: auto !important;">
<td style="text-align: left; user-select: auto !important;">fruit_based</td>
<td style="user-select: auto !important;">19550</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges