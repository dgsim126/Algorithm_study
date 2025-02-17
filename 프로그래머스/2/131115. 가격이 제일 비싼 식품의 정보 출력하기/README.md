# [level 2] 가격이 제일 비싼 식품의 정보 출력하기 - 131115 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131115) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > SUM， MAX， MIN

### 채점결과

Empty

### 제출 일자

2025년 02월 16일 12:27:03

### 문제 설명

<p style="user-select: auto !important;">다음은 식품의 정보를 담은 <code style="user-select: auto !important;">FOOD_PRODUCT</code> 테이블입니다. <code style="user-select: auto !important;">FOOD_PRODUCT</code> 테이블은 다음과 같으며 <code style="user-select: auto !important;">PRODUCT_ID</code>, <code style="user-select: auto !important;">PRODUCT_NAME</code>, <code style="user-select: auto !important;">PRODUCT_CD</code>, <code style="user-select: auto !important;">CATEGORY</code>, <code style="user-select: auto !important;">PRICE</code>는 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 의미합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">Column name</th>
<th style="user-select: auto !important;">Type</th>
<th style="user-select: auto !important;">Nullable</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRODUCT_ID</td>
<td style="user-select: auto !important;">VARCHAR(10)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRODUCT_NAME</td>
<td style="user-select: auto !important;">VARCHAR(50)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRODUCT_CD</td>
<td style="user-select: auto !important;">VARCHAR(10)</td>
<td style="user-select: auto !important;">TRUE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">CATEGORY</td>
<td style="user-select: auto !important;">VARCHAR(10)</td>
<td style="user-select: auto !important;">TRUE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRICE</td>
<td style="user-select: auto !important;">NUMBER</td>
<td style="user-select: auto !important;">TRUE</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">문제</h5>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">FOOD_PRODUCT</code> 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요. </p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">FOOD_PRODUCT</code> 테이블이 다음과 같을 때</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">PRODUCT_ID</th>
<th style="user-select: auto !important;">PRODUCT_NAME</th>
<th style="user-select: auto !important;">PRODUCT_CD</th>
<th style="user-select: auto !important;">CATEGORY</th>
<th style="user-select: auto !important;">PRICE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">P0018</td>
<td style="user-select: auto !important;">맛있는고추기름</td>
<td style="user-select: auto !important;">CD_OL00008</td>
<td style="user-select: auto !important;">식용유</td>
<td style="user-select: auto !important;">6100</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">P0019</td>
<td style="user-select: auto !important;">맛있는카놀라유</td>
<td style="user-select: auto !important;">CD_OL00009</td>
<td style="user-select: auto !important;">식용유</td>
<td style="user-select: auto !important;">5100</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">P0020</td>
<td style="user-select: auto !important;">맛있는산초유</td>
<td style="user-select: auto !important;">CD_OL00010</td>
<td style="user-select: auto !important;">식용유</td>
<td style="user-select: auto !important;">6500</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">P0021</td>
<td style="user-select: auto !important;">맛있는케첩</td>
<td style="user-select: auto !important;">CD_OL00001</td>
<td style="user-select: auto !important;">소스</td>
<td style="user-select: auto !important;">4500</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">P0022</td>
<td style="user-select: auto !important;">맛있는마요네즈</td>
<td style="user-select: auto !important;">CD_OL00002</td>
<td style="user-select: auto !important;">소스</td>
<td style="user-select: auto !important;">4700</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">PRODUCT_ID</th>
<th style="user-select: auto !important;">PRODUCT_NAME</th>
<th style="user-select: auto !important;">PRODUCT_CD</th>
<th style="user-select: auto !important;">CATEGORY</th>
<th style="user-select: auto !important;">PRICE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">P0020</td>
<td style="user-select: auto !important;">맛있는산초유</td>
<td style="user-select: auto !important;">CD_OL00010</td>
<td style="user-select: auto !important;">식용유</td>
<td style="user-select: auto !important;">6500</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges