import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[['author_id']].where(views['author_id']==views['viewer_id'])
    df=df.dropna()
    df=df.sort_values(by='author_id')
    df=df.rename(columns={'author_id':'id'})
    df=df.drop_duplicates()
    return df
    
