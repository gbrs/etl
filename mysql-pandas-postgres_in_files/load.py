"""
LOAD
Загрузим данные (в этом игрушечном примере [пере]запишем полученную таблицу в БД Postgres)
"""

import pandas as pd

def load_to_postgres(cube: pd.DataFrame):
    import psycopg2
    from sqlalchemy import create_engine
    from sqlalchemy import URL
    from config import postgresql_home

    sql_create_query = '''
        CREATE TABLE IF NOT EXISTS cube (
            Чеболь       VARCHAR(64), 
            Промысел     VARCHAR(64), 
            Царство      VARCHAR(64), 
            Сумма_продаж DECIMAL(10, 2)
        )
    '''

    with psycopg2.connect(
            host=postgresql_home['host'],
            user=postgresql_home['user'], 
            password=postgresql_home['password'],
            database=postgresql_home['database']
            ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql_create_query)
    
    url_object = URL.create(
        "postgresql+psycopg2",
        username=postgresql_home['user'],
        password=postgresql_home['password'], 
        host=postgresql_home['host'],
        port=postgresql_home['port'],
        database='competition_analysis',
    )
    
    engine = create_engine(url_object)
    
    cube.to_sql(
        name='cube', # имя таблицы
        con=engine,  # движок
        if_exists="replace", # если в таблице данные уже есть, заменяем их
        index=False # без индекса датафрейма
    )



