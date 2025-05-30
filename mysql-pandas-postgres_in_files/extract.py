"""
EXTRACT
В этом игрушечном примере из удаленной MySQL БД
"""

def extract_from_mysql():
    import pandas as pd
    import mysql.connector
    from config import mysql_qm
    
    sql_extract_query = '''
        SELECT
            *
        FROM
            sales 
            INNER JOIN companies USING(Артель)
            INNER JOIN chaebols USING(Артель)
            INNER JOIN industries USING(Товар) 
            INNER JOIN regions USING(Град)
    '''

    with mysql.connector.connect(
                host=mysql_qm['host'],
                user=mysql_qm['user'], 
                password=mysql_qm['password'],
                database=mysql_qm['database']
                ) as connection:
        return pd.read_sql(sql_extract_query, connection)
