# [level 2] 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기 - 151137 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/151137) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2025년 02월 16일 14:43:48

### 문제 설명

<p style="user-select: auto !important;">다음은 어느 자동차 대여 회사에서 대여중인 자동차들의 정보를 담은 <code style="user-select: auto !important;">CAR_RENTAL_COMPANY_CAR</code> 테이블입니다. <code style="user-select: auto !important;">CAR_RENTAL_COMPANY_CAR</code> 테이블은 아래와 같은 구조로 되어있으며, <code style="user-select: auto !important;">CAR_ID</code>, <code style="user-select: auto !important;">CAR_TYPE</code>, <code style="user-select: auto !important;">DAILY_FEE</code>, <code style="user-select: auto !important;">OPTIONS</code> 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">Column name</th>
<th style="user-select: auto !important;">Type</th>
<th style="user-select: auto !important;">Nullable</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">CAR_ID</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">CAR_TYPE</td>
<td style="user-select: auto !important;">VARCHAR(255)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">DAILY_FEE</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">OPTIONS</td>
<td style="user-select: auto !important;">VARCHAR(255)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다. 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(옵션 리스트 값 예시: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">문제</h5>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">CAR_RENTAL_COMPANY_CAR</code> 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 자동차 종류 별로 몇 대인지 출력하는 SQL문을 작성해주세요. 이때 자동차 수에 대한 컬럼명은 <code style="user-select: auto !important;">CARS</code>로 지정하고, 결과는 자동차 종류를 기준으로 오름차순 정렬해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">CAR_RENTAL_COMPANY_CAR</code> 테이블이 다음과 같다면</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">CAR_ID</th>
<th style="user-select: auto !important;">CAR_TYPE</th>
<th style="user-select: auto !important;">DAILY_FEE</th>
<th style="user-select: auto !important;">OPTIONS</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">세단</td>
<td style="user-select: auto !important;">16000</td>
<td style="user-select: auto !important;">가죽시트,열선시트,후방카메라</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">SUV</td>
<td style="user-select: auto !important;">14000</td>
<td style="user-select: auto !important;">스마트키,네비게이션,열선시트</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">SUV</td>
<td style="user-select: auto !important;">22000</td>
<td style="user-select: auto !important;">주차감지센서,후방카메라</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">트럭</td>
<td style="user-select: auto !important;">35000</td>
<td style="user-select: auto !important;">주차감지센서,네비게이션,열선시트</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">SUV</td>
<td style="user-select: auto !important;">16000</td>
<td style="user-select: auto !important;">가죽시트,네비게이션,열선시트,후방카메라,주차감지센서</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">'통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차는 자동차 ID가 1, 2, 4, 5인 자동차이고, 자동차 종류 별로 몇 대인지 구하고 자동차 종류를 기준으로 오름차순 정렬하면 다음과 같은 결과가 나와야 합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">CAR_TYPE</th>
<th style="user-select: auto !important;">CARS</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">SUV</td>
<td style="user-select: auto !important;">2</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">세단</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">트럭</td>
<td style="user-select: auto !important;">1</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges