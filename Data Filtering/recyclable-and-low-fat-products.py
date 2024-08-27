import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df=products[['product_id']].where((products['low_fats']=='Y')&(products['recyclable']=='Y'))
    df=df.dropna()
    return df
    
