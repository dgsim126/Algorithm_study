# [level 1] 어린 동물 찾기 - 59037 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59037) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > SELECT

### 채점결과

Empty

### 제출 일자

2025년 02월 15일 12:03:13

### 문제 설명

<p style="user-select: auto !important;"><code style="user-select: auto !important;">ANIMAL_INS</code> 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. <code style="user-select: auto !important;">ANIMAL_INS</code> 테이블 구조는 다음과 같으며, <code style="user-select: auto !important;">ANIMAL_ID</code>, <code style="user-select: auto !important;">ANIMAL_TYPE</code>, <code style="user-select: auto !important;">DATETIME</code>, <code style="user-select: auto !important;">INTAKE_CONDITION</code>, <code style="user-select: auto !important;">NAME</code>, <code style="user-select: auto !important;">SEX_UPON_INTAKE</code>는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">NAME</th>
<th style="user-select: auto !important;">TYPE</th>
<th style="user-select: auto !important;">NULLABLE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ANIMAL_ID</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ANIMAL_TYPE</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">DATETIME</td>
<td style="user-select: auto !important;">DATETIME</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">INTAKE_CONDITION</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">NAME</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">TRUE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">SEX_UPON_INTAKE</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">동물 보호소에 들어온 동물 중 젊은 동물<sup id="fnref1" style="user-select: auto !important;"><a href="#fn1" style="user-select: auto !important;">1</a></sup>의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요. </p>

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">ANIMAL_INS</code> 테이블이 다음과 같다면</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">ANIMAL_ID</th>
<th style="user-select: auto !important;">ANIMAL_TYPE</th>
<th style="user-select: auto !important;">DATETIME</th>
<th style="user-select: auto !important;">INTAKE_CONDITION</th>
<th style="user-select: auto !important;">NAME</th>
<th style="user-select: auto !important;">SEX_UPON_INTAKE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A365172</td>
<td style="user-select: auto !important;">Dog</td>
<td style="user-select: auto !important;">2014-08-26 12:53:00</td>
<td style="user-select: auto !important;">Normal</td>
<td style="user-select: auto !important;">Diablo</td>
<td style="user-select: auto !important;">Neutered Male</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A367012</td>
<td style="user-select: auto !important;">Dog</td>
<td style="user-select: auto !important;">2015-09-16 09:06:00</td>
<td style="user-select: auto !important;">Sick</td>
<td style="user-select: auto !important;">Miller</td>
<td style="user-select: auto !important;">Neutered Male</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A365302</td>
<td style="user-select: auto !important;">Dog</td>
<td style="user-select: auto !important;">2017-01-08 16:34:00</td>
<td style="user-select: auto !important;">Aged</td>
<td style="user-select: auto !important;">Minnie</td>
<td style="user-select: auto !important;">Spayed Female</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A381217</td>
<td style="user-select: auto !important;">Dog</td>
<td style="user-select: auto !important;">2017-07-08 09:41:00</td>
<td style="user-select: auto !important;">Sick</td>
<td style="user-select: auto !important;">Cherokee</td>
<td style="user-select: auto !important;">Neutered Male</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">이 중 젊은 동물은 Diablo, Miller, Cherokee입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다. </p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">ANIMAL_ID</th>
<th style="user-select: auto !important;">NAME</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A365172</td>
<td style="user-select: auto !important;">Diablo</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A367012</td>
<td style="user-select: auto !important;">Miller</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A381217</td>
<td style="user-select: auto !important;">Cherokee</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener" style="user-select: auto !important;">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener" style="user-select: auto !important;">ODbL</a>의 적용을 받습니다.</p>

<div class="footnotes" style="user-select: auto !important;">
<hr style="user-select: auto !important;">
<ol style="user-select: auto !important;">

<li id="fn1" style="user-select: auto !important;">
<p style="user-select: auto !important;"><code style="user-select: auto !important;">INTAKE_CONDITION</code>이 Aged가 아닌 경우를 뜻함&nbsp;<a href="#fnref1" style="user-select: auto !important;">↩</a></p>
</li>

</ol>
</div>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges