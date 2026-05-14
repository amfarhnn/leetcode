import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)
    
    N = N - 1
    
    if len(salaries) > N:
        if N >= 0:
            nthhighest = salaries.iloc[N]
        else:
            nthhighest = None
    else:
        nthhighest = None

    return pd.DataFrame({
        f"getNthHighestSalary({N+1})" : [nthhighest]
    })