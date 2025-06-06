"""
главный файл ETL процесса
E - забираем данные из MySQL
T - создаем "кубы" в pandas
L - занружаем в PostgreSQL
"""

from extract import extract_from_mysql
from transform import create_cube
from load import load_to_postgres


def run_etl_pipeline():
    # Extract
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
    df = extract_from_mysql(sql_extract_query)
    print("Extracted!")
    
    # Transform
    cube = create_cube(df)
    print("Transformed!")
    
    # Load
    sql_create_query = '''
        CREATE TABLE IF NOT EXISTS cube (
            Чеболь       VARCHAR(64), 
            Промысел     VARCHAR(64), 
            Царство      VARCHAR(64), 
            Сумма_продаж DECIMAL(10, 2)
        )
    '''
    load_to_postgres(sql_create_query, cube)
    print("Loaded!")
    
    print("ETL process completed!")


if __name__ == "__main__":
    run_etl_pipeline()

