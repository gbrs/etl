"""
EXTRACT
Забираем данные из БД (в этом игрушечном примере - с удаленной MySQL)
"""

def extract():
    sql_query = '''
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
        df = pd.read_sql(sql_query, connection)
    
    df = df[['Дата', 'Плата', 'Артель', 'Чеболь', 'Товар', 'Промысел', 'Град', 'Царство', ]]
    
    df.Дата = pd.to_datetime(df.Дата)

if __name__ == '__main__':
    extract()
