/*
DEVELOPERS 테이블에서 SKILL_CODE를 가져온다.
해당 SKILL_CODE를 SKILLCODES 테이블의 CODE로 %했을 때, 0이 되지 않는다면 해당 스킬을 가지고 있는 것
*/

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME 
FROM DEVELOPERS 
WHERE (SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = "Python")) > 0
 OR (SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = "C#")) > 0
ORDER BY ID ASC;

/*
400 →  110010000 (2진수)
256 →  100000000 (2진수)
----------------
400 & 256 → 100000000 (256) ✅ (Python 포함)
*/