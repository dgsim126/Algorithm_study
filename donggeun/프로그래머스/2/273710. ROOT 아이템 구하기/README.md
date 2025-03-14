# [level 2] ROOT 아이템 구하기 - 273710 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/273710) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > IS NULL

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2025년 02월 16일 14:10:12

### 문제 설명

<p style="user-select: auto !important;">어느 한 게임에서 사용되는 아이템들은 업그레이드가 가능합니다.<br style="user-select: auto !important;">
'ITEM_A'-&gt;'ITEM_B'와 같이 업그레이드가 가능할 때 <br style="user-select: auto !important;">
'ITEM_A'를 'ITEM_B'의 PARENT 아이템,<br style="user-select: auto !important;">
 PARENT 아이템이 없는 아이템을 ROOT 아이템이라고 합니다.</p>

<p style="user-select: auto !important;">예를 들어 'ITEM_A'-&gt;'ITEM_B'-&gt;'ITEM_C' 와 같이 업그레이드가 가능한 아이템이 있다면<br style="user-select: auto !important;">
'ITEM_C'의 PARENT 아이템은 'ITEM_B'<br style="user-select: auto !important;">
'ITEM_B'의 PARENT 아이템은 'ITEM_A'<br style="user-select: auto !important;">
ROOT 아이템은 'ITEM_A'가 됩니다.</p>

<p style="user-select: auto !important;">다음은 해당 게임에서 사용되는 아이템 정보를 담은 <code style="user-select: auto !important;">ITEM_INFO</code> 테이블과 아이템 관계를 나타낸 <code style="user-select: auto !important;">ITEM_TREE</code> 테이블입니다. <code style="user-select: auto !important;">ITEM_INFO</code> 테이블은 다음과 같으며, <code style="user-select: auto !important;">ITEM_ID</code>, <code style="user-select: auto !important;">ITEM_NAME</code>, <code style="user-select: auto !important;">RARITY</code>, <code style="user-select: auto !important;">PRICE</code>는 각각 아이템 ID, 아이템 명, 아이템의 희귀도, 아이템의 가격을 나타냅니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">Column name</th>
<th style="user-select: auto !important;">Type</th>
<th style="user-select: auto !important;">Nullable</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ITEM_ID</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ITEM_NAME</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">RARITY</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRICE</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;"><code style="user-select: auto !important;">ITEM_TREE</code> 테이블은 다음과 같으며, <code style="user-select: auto !important;">ITEM_ID</code>, <code style="user-select: auto !important;">PARENT_ITEM_ID</code>는 각각 아이템 ID, PARENT 아이템의 ID를 나타냅니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">Column name</th>
<th style="user-select: auto !important;">Type</th>
<th style="user-select: auto !important;">Nullable</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ITEM_ID</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PARENT_ITEM_ID</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">TRUE</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">단, 각 아이템들은 오직 하나의 PARENT 아이템 ID를 가지며, ROOT 아이템의 PARENT 아이템 ID는 NULL 입니다.</p>

<p style="user-select: auto !important;">ROOT 아이템이 없는 경우는 존재하지 않습니다.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">문제</h5>

<p style="user-select: auto !important;">ROOT 아이템을 찾아 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME)을 출력하는 SQL문을 작성해 주세요. 이때, 결과는 아이템 ID를 기준으로 오름차순 정렬해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">ITEM_INFO</code> 테이블이 다음과 같고</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">ITEM_ID</th>
<th style="user-select: auto !important;">ITEM_NAME</th>
<th style="user-select: auto !important;">RARITY</th>
<th style="user-select: auto !important;">PRICE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">ITEM_A</td>
<td style="user-select: auto !important;">COMMON</td>
<td style="user-select: auto !important;">10000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">ITEM_B</td>
<td style="user-select: auto !important;">LEGEND</td>
<td style="user-select: auto !important;">9000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">ITEM_C</td>
<td style="user-select: auto !important;">LEGEND</td>
<td style="user-select: auto !important;">11000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">ITEM_D</td>
<td style="user-select: auto !important;">UNIQUE</td>
<td style="user-select: auto !important;">10000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">ITEM_E</td>
<td style="user-select: auto !important;">LEGEND</td>
<td style="user-select: auto !important;">12000</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;"><code style="user-select: auto !important;">ITEM_TREE</code>  테이블이 다음과 같다면</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">ITEM_ID</th>
<th style="user-select: auto !important;">PARENT_ITEM_ID</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">0</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">3</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">ROOT 아이템의 아이템 ID는 PARENT 아이템 ID(PARENT_ITEM_ID)가 NULL 인 0, 3 이므로 SQL문을 실행하면 다음과 같은 결과가 나와야 합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">ITEM_ID</th>
<th style="user-select: auto !important;">ITEM_NAME</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">ITEM_A</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">ITEM_D</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">※ 참고: 본 문제는 제출 내역 확인 기능을 지원하지 않습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges