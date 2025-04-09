"""
TRANSFORM
Преобразуем данные (в этом игрушечном примере - с удаленной MySQL)
"""

import pandas as pd

def reformat_data(df: pd.DataFrame):
    df = df[['Дата', 'Плата', 'Артель', 'Чеболь', 'Товар', 'Промысел', 'Град', 'Царство', ]]
    df.Дата = pd.to_datetime(df.Дата)
    return df

def create_cube(df: pd.DataFrame):
    df = reformat_data(df)
    cube = df.groupby(['Чеболь', 'Промысел', 'Царство', ]).Плата.sum().round(2).reset_index()
    cube = cube.rename(columns={'Плата': 'Сумма_продаж'})
    return cube
