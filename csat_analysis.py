
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import matplotlib.pyplot as plt

engine = create_engine('mysql+pymysql://root:Efua1234@localhost:3306/home_task')

query = """
SELECT sc.support_case_id,
       sc.support_case_language,
       sc.support_case_vertical,
       sc.is_support_case_escalated_to_agent,
       sc.support_case_user_persona,
       si.interaction_option,
       CASE 
       WHEN si.interaction_option = 'good' THEN 1
       WHEN si.interaction_option = 'bad' THEN 0 
       END AS interaction_status
FROM support_case sc
INNER JOIN support_case_interaction si ON si.support_case_id = sc.support_case_id
WHERE si.interaction_option IN ('good','bad') ;  
"""
# loading sql query results into a  pandas DataFrame
query_df = pd.read_sql_query(query, engine)

# inspecting the first five rows of the DataFrame

print(query_df.head(10))