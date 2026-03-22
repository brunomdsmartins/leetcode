import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    string = f"getNthHighestSalary({N})"

    if N <= 0:
        return pd.DataFrame({string: [None]})

    unique_salaries = (
        employee["salary"].drop_duplicates().sort_values(ascending=False)
    )  # pandas series

    if len(unique_salaries) < N:
        return pd.DataFrame({string: [None]})

    return pd.DataFrame({string: [unique_salaries.iloc[N - 1]]})
