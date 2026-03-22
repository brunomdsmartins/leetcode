import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, "left", "empId")

    mask = (df["bonus"].isna()) | (df["bonus"] < 1000)
    df = df.loc[mask, ["name", "bonus"]]

    return df


employees = pd.DataFrame(
    [
        {"empId": 3, "name": "Brad", "supervisor": None, "salary": 4000},
        {"empId": 1, "name": "John", "supervisor": 3, "salary": 1000},
        {"empId": 2, "name": "Dan", "supervisor": 3, "salary": 2000},
        {"empId": 4, "name": "Thomas", "supervisor": 3, "salary": 4000},
    ]
)

bonus = pd.DataFrame(
    [
        {"empId": 2, "bonus": 500},
        {"empId": 4, "bonus": 2000},
    ]
)

print(employee_bonus(employee=employees, bonus=bonus))
