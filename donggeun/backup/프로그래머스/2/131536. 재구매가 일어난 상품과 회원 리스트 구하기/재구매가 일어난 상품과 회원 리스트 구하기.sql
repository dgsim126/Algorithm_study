/*
SELECT A.USER_ID, A.PRODUCT_ID FROM ONLINE_SALE A LEFT JOIN ONLINE_SALE B ON A.USER_ID=B.USER_ID
WHERE A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY A.USER_ID ASC, A.PRODUCT_ID DESC;
*/

SELECT USER_ID, PRODUCT_ID FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC;