# [level 1] Python 개발자 찾기 - 276013 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/276013?language=mysql) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > SELECT

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2025년 02월 15일 12:13:11

### 문제 설명

<p style="user-select: auto !important;"><code style="user-select: auto !important;">DEVELOPER_INFOS</code> 테이블은 개발자들의 프로그래밍 스킬 정보를 담은 테이블입니다. <code style="user-select: auto !important;">DEVELOPER_INFOS</code> 테이블 구조는 다음과 같으며, <code style="user-select: auto !important;">ID</code>, <code style="user-select: auto !important;">FIRST_NAME</code>, <code style="user-select: auto !important;">LAST_NAME</code>, <code style="user-select: auto !important;">EMAIL</code>, <code style="user-select: auto !important;">SKILL_1</code>, <code style="user-select: auto !important;">SKILL_2</code>, <code style="user-select: auto !important;">SKILL_3</code>는 각각 ID,  이름, 성, 이메일, 첫 번째 스킬, 두 번째 스킬, 세 번째 스킬을 의미합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">NAME</th>
<th style="user-select: auto !important;">TYPE</th>
<th style="user-select: auto !important;">UNIQUE</th>
<th style="user-select: auto !important;">NULLABLE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">ID</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">Y</td>
<td style="user-select: auto !important;">N</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">FIRST_NAME</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">Y</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">LAST_NAME</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">Y</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">EMAIL</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">Y</td>
<td style="user-select: auto !important;">N</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">SKILL_1</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">Y</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">SKILL_2</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">Y</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">SKILL_3</td>
<td style="user-select: auto !important;">VARCHAR(N)</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">Y</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">문제</h5>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">DEVELOPER_INFOS</code> 테이블에서 Python 스킬을 가진 개발자의 정보를 조회하려 합니다. Python 스킬을 가진 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요. </p>

<p style="user-select: auto !important;">결과는 ID를 기준으로 오름차순 정렬해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">DEVELOPER_INFOS</code> 테이블이 다음과 같다면</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">ID</th>
<th style="user-select: auto !important;">FIRST_NAME</th>
<th style="user-select: auto !important;">LAST_NAME</th>
<th style="user-select: auto !important;">EMAIL</th>
<th style="user-select: auto !important;">SKILL_1</th>
<th style="user-select: auto !important;">SKILL_2</th>
<th style="user-select: auto !important;">SKILL_3</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">D165</td>
<td style="user-select: auto !important;">Jerami</td>
<td style="user-select: auto !important;">Edwards</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">jerami_edwards@grepp.co</code></td>
<td style="user-select: auto !important;">Java</td>
<td style="user-select: auto !important;">JavaScript</td>
<td style="user-select: auto !important;">Python</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">D161</td>
<td style="user-select: auto !important;">Carsen</td>
<td style="user-select: auto !important;">Garza</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">carsen_garza@grepp.co</code></td>
<td style="user-select: auto !important;">React</td>
<td style="user-select: auto !important;"></td>
<td style="user-select: auto !important;"></td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">D164</td>
<td style="user-select: auto !important;">Kelly</td>
<td style="user-select: auto !important;">Grant</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">kelly_grant@grepp.co</code></td>
<td style="user-select: auto !important;">C#</td>
<td style="user-select: auto !important;"></td>
<td style="user-select: auto !important;"></td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">D163</td>
<td style="user-select: auto !important;">Luka</td>
<td style="user-select: auto !important;">Cory</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">luka_cory@grepp.co</code></td>
<td style="user-select: auto !important;">Node.js</td>
<td style="user-select: auto !important;"></td>
<td style="user-select: auto !important;"></td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">D162</td>
<td style="user-select: auto !important;">Cade</td>
<td style="user-select: auto !important;">Cunningham</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">cade_cunningham@grepp.co</code></td>
<td style="user-select: auto !important;">Vue</td>
<td style="user-select: auto !important;">C++</td>
<td style="user-select: auto !important;">Python</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">다음과 같이 Python 스킬을 가진 개발자의 정보가 결과에 나와야 합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">ID</th>
<th style="user-select: auto !important;">EMAIL</th>
<th style="user-select: auto !important;">FIRST_NAME</th>
<th style="user-select: auto !important;">LAST_NAME</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">D162</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">cade_cunningham@grepp.co</code></td>
<td style="user-select: auto !important;">Cade</td>
<td style="user-select: auto !important;">Cunningham</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">D165</td>
<td style="user-select: auto !important;"><code style="user-select: auto !important;">jerami_edwards@grepp.co</code></td>
<td style="user-select: auto !important;">Jerami</td>
<td style="user-select: auto !important;">Edwards</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges