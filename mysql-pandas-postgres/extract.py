"""
EXTRACT
В этом игрушечном примере создаем "куб" для сумм продаж
"""

import pandas as pd

def extract_from_mysql(sql_extract_query: str):
    import mysql.connector
    from Users.Боря.AnacondaProjects.etl_experiments.config import mysql_qm
    
    with mysql.connector.connect(
                host=mysql_qm['host'],
                user=mysql_qm['user'], 
                password=mysql_qm['password'],
                database=mysql_qm['database']
                ) as connection:
        return pd.read_sql(sql_extract_query, connection)
