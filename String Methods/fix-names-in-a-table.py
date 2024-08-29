import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def up(b):
        l=len(b)
        #print(b)
        for i in range(l):
            b[i]=b[i][0].upper()+b[i][1:].lower()
        return b
    df1=users[['user_id','name']]
    df1['name']=up(df1['name'])
    df1=df1.sort_values(by='user_id')
    return(df1)
