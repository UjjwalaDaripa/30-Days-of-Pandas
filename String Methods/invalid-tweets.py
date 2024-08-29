import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    def total_length(a):
        return len(a)
    df=tweets[['tweet_id']].where(tweets['content'].str.len()>15)
    df=df.dropna()
    return df
    
