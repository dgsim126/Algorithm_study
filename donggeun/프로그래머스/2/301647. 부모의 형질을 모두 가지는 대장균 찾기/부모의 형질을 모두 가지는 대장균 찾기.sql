/*
DCOLI_DATA에 PARENT_ID에 해당하는 GENOTYPE이 추가되어야 함
추가한 후 두 개를 비트 연산자 &로 계산하여 형질을 포함하는지 확인

GENOTYPE이 P_GENOTYPE을 포함하는지 확인

!! 비트 연산자 제대로 기억할 것 !!
*/

SELECT ID, GENOTYPE, P_GENOTYPE AS PARENT_GENOTYPE FROM ECOLI_DATA A 
JOIN (SELECT ID AS P_ID, GENOTYPE AS P_GENOTYPE FROM ECOLI_DATA) B
ON A.PARENT_ID = B.P_ID
WHERE (GENOTYPE & P_GENOTYPE) = P_GENOTYPE
ORDER BY ID ASC;