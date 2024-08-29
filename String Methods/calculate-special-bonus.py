import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=employees['salary']*(100/100)
    employees['bonus']=np.where((employees['name'].str[0]=='M')|(employees['employee_id']%2==0),0,employees['bonus'])
    df=employees[['employee_id','bonus']]
    df=df.sort_values(by='employee_id')
    return df

    
