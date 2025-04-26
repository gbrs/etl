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
    df = extract_from_mysql()
    print("Extracted!")
    
    # Transform
    cube = create_cube(df)
    print("Transformed!")
    
    # Load
    load_to_postgres(cube)
    print("Loaded!")
    
    print("ETL process completed!")


if __name__ == "__main__":
    run_etl_pipeline()

