SELECT OUT("iati105_iati_activity_iati105_description")[0].text AS description,
$trans_Value.OUT("iati105_transaction_iati105_value").text__int__ AS costs,
$trans_Value.OUT("iati105_transaction_iati105_value").value_date 
FROM iati105_iati_activity  LET $trans_Value = OUT("iati105_iati_activity_iati105_transaction")
WHERE $trans_Value.OUT("iati105_transaction_iati105_transaction_type").code IS "D"

SELECT 
@rid,
OUT("iati105_iati_activity_iati105_description")[0].text AS description,
$trans_Value.OUT("iati105_transaction_iati105_value")[$parent.OUT("iati105_transaction_iati105_transaction_type").code='D'].text__int__ AS costs,
$trans_Value.OUT("iati105_transaction_iati105_value").value_date FROM iati105_iati_activity  LET $trans_Value = OUT("iati105_iati_activity_iati105_transaction")

SELECT 
@rid,
OUT("iati105_iati_activity_iati105_description")[0].text AS description,
$trans_Value.OUT("iati105_transaction_iati105_value").text__int__ AS costs,
$trans_Value.OUT("iati105_transaction_iati105_value").IN("iati105_transaction_iati105_value").OUT("iati105_transaction_iati105_transaction_type").code AS code_1,
$trans_Value.OUT("iati105_transaction_iati105_transaction_type").code AS code,
$trans_Value.OUT("iati105_transaction_iati105_transaction_type")[code="D"][text = "Disbursement"].IN("iati105_transaction_iati105_transaction_type").OUT("iati105_transaction_iati105_value").text__int__ AS code_filter_d,                           
$trans_Value.OUT("iati105_transaction_iati105_value").value_date FROM iati105_iati_activity  
LET $trans_Value = OUT("iati105_iati_activity_iati105_transaction")




SELECT code,description,sum(costs) FROM 
(
SELECT  EXPAND( $c )  
LET $a =
(SELECT 
code,
IN("iati105_transaction_iati105_transaction_type").OUT("iati105_transaction_iati105_value").text__int__ AS costs,
IN("iati105_transaction_iati105_transaction_type").IN("iati105_iati_activity_iati105_transaction").OUT("iati105_iati_activity_iati105_description")[0].text AS description
FROM iati105_transaction_type ),
$b =
(SELECT 
code,
IN("iati201_transaction_iati201_transaction_type").OUT("iati201_transaction_iati201_value").text__dec__ AS costs,
IN("iati201_transaction_iati201_transaction_type").IN("iati201_iati_activity_iati201_transaction").OUT("iati201_iati_activity_iati201_description").OUT("iati201_description_iati201_narrative")[0].text AS description
FROM iati201_transaction_type  ),
$c = UNIONALL( $a, $b )
)
GROUP BY code,description
ORDER BY description


SELECT code,description,sum(costs) FROM 
(
SELECT  EXPAND( $c )  
LET $a =
(SELECT 
code,
SUM(IN("iati105_transaction_iati105_transaction_type").OUT("iati105_transaction_iati105_value").text__int__) AS costs,
IN("iati105_transaction_iati105_transaction_type").IN("iati105_iati_activity_iati105_transaction").OUT("iati105_iati_activity_iati105_description")[0].text AS description
FROM iati105_transaction_type 
GROUP BY code,description),
$b =
(SELECT 
code,
SUM(IN("iati201_transaction_iati201_transaction_type").OUT("iati201_transaction_iati201_value").text__dec__) AS costs,
IN("iati201_transaction_iati201_transaction_type").IN("iati201_iati_activity_iati201_transaction").OUT("iati201_iati_activity_iati201_description").OUT("iati201_description_iati201_narrative")[0].text AS description
FROM iati201_transaction_type  
GROUP BY code,description),
$c = UNIONALL( $a, $b )
)
ORDER BY description





