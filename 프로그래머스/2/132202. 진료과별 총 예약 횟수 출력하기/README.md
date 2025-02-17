# [level 2] 진료과별 총 예약 횟수 출력하기 - 132202 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/132202) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2025년 02월 16일 14:56:41

### 문제 설명

<p style="user-select: auto !important;">다음은 종합병원의 진료 예약정보를 담은 <code style="user-select: auto !important;">APPOINTMENT</code> 테이블 입니다.<br style="user-select: auto !important;">
<code style="user-select: auto !important;">APPOINTMENT</code> 테이블은 다음과 같으며 <code style="user-select: auto !important;">APNT_YMD</code>, <code style="user-select: auto !important;">APNT_NO</code>, <code style="user-select: auto !important;">PT_NO</code>, <code style="user-select: auto !important;">MCDP_CD</code>, <code style="user-select: auto !important;">MDDR_ID</code>, <code style="user-select: auto !important;">APNT_CNCL_YN</code>, <code style="user-select: auto !important;">APNT_CNCL_YMD</code>는 각각 진료예약일시, 진료예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소날짜를 나타냅니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">Column name</th>
<th style="user-select: auto !important;">Type</th>
<th style="user-select: auto !important;">Nullable</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">APNT_YMD</td>
<td style="user-select: auto !important;">TIMESTAMP</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">APNT_NO</td>
<td style="user-select: auto !important;">NUMBER(5)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PT_NO</td>
<td style="user-select: auto !important;">VARCHAR(10)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">MCDP_CD</td>
<td style="user-select: auto !important;">VARCHAR(6)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">MDDR_ID</td>
<td style="user-select: auto !important;">VARCHAR(10)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">APNT_CNCL_YN</td>
<td style="user-select: auto !important;">VARCHAR(1)</td>
<td style="user-select: auto !important;">TRUE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">APNT_CNCL_YMD</td>
<td style="user-select: auto !important;">DATE</td>
<td style="user-select: auto !important;">TRUE</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">문제</h5>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">APPOINTMENT</code> 테이블에서 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회하는 SQL문을 작성해주세요. 이때, 컬럼명은 '진료과 코드', '5월예약건수'로 지정해주시고 결과는 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">APPOINTMENT</code> 테이블이 다음과 같을 때</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">APNT_YMD</th>
<th style="user-select: auto !important;">APNT_NO</th>
<th style="user-select: auto !important;">PT_NO</th>
<th style="user-select: auto !important;">MCDP_CD</th>
<th style="user-select: auto !important;">MDDR_ID</th>
<th style="user-select: auto !important;">APNT_CNCL_YN</th>
<th style="user-select: auto !important;">APNT_CNCL_YMD</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-04-14 09:30:00.000000</td>
<td style="user-select: auto !important;">47</td>
<td style="user-select: auto !important;">PT22000064</td>
<td style="user-select: auto !important;">GS</td>
<td style="user-select: auto !important;">DR20170123</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-04-15 10:30:00.000000</td>
<td style="user-select: auto !important;">48</td>
<td style="user-select: auto !important;">PT22000065</td>
<td style="user-select: auto !important;">OB</td>
<td style="user-select: auto !important;">DR20100231</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-15 17:30:00.000000</td>
<td style="user-select: auto !important;">49</td>
<td style="user-select: auto !important;">PT22000086</td>
<td style="user-select: auto !important;">OB</td>
<td style="user-select: auto !important;">DR20100231</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-18 10:30:00.000000</td>
<td style="user-select: auto !important;">52</td>
<td style="user-select: auto !important;">PT22000019</td>
<td style="user-select: auto !important;">GS</td>
<td style="user-select: auto !important;">DR20100039</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-19 12:00:00.000000</td>
<td style="user-select: auto !important;">53</td>
<td style="user-select: auto !important;">PT22000020</td>
<td style="user-select: auto !important;">FM</td>
<td style="user-select: auto !important;">DR20010112</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-22 08:30:00.000000</td>
<td style="user-select: auto !important;">54</td>
<td style="user-select: auto !important;">PT22000021</td>
<td style="user-select: auto !important;">GS</td>
<td style="user-select: auto !important;">DR20100039</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-04 10:30:00.000000</td>
<td style="user-select: auto !important;">56</td>
<td style="user-select: auto !important;">PT22000023</td>
<td style="user-select: auto !important;">FM</td>
<td style="user-select: auto !important;">DR20090112</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-14 15:30:00.000000</td>
<td style="user-select: auto !important;">57</td>
<td style="user-select: auto !important;">PT22000074</td>
<td style="user-select: auto !important;">CS</td>
<td style="user-select: auto !important;">DR20200012</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-24 15:30:00.000000</td>
<td style="user-select: auto !important;">58</td>
<td style="user-select: auto !important;">PT22000085</td>
<td style="user-select: auto !important;">CS</td>
<td style="user-select: auto !important;">DR20200012</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2022-05-28 10:00:00.000000</td>
<td style="user-select: auto !important;">60</td>
<td style="user-select: auto !important;">PT22000092</td>
<td style="user-select: auto !important;">OS</td>
<td style="user-select: auto !important;">DR20100031</td>
<td style="user-select: auto !important;">N</td>
<td style="user-select: auto !important;">NULL</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">진료과코드</th>
<th style="user-select: auto !important;">5월예약건수</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">OB</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">OS</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">CS</td>
<td style="user-select: auto !important;">2</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">FM</td>
<td style="user-select: auto !important;">2</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">GS</td>
<td style="user-select: auto !important;">2</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges