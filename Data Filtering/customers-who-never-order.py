import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    df=df[['name']].where(df['customerId'].isna())
    df=df.dropna()
    df=df.rename(columns={'name': 'Customers'})
    return df
    
