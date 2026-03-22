import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        employee, left_on="managerId", right_on="id", suffixes=("", "_manager")
    )

    print(df)

    result = df[df["salary"] > df["salary_manager"]]

    return result[["name"]].rename(columns={"name": "Employee"})


df = pd.DataFrame(
    {
        "id": [1, 2, 3, 4],
        "name": ["Joe", "Henry", "Sam", "Max"],
        "salary": [70000, 80000, 60000, 90000],
        "managerId": [3, 4, None, None],
    }
)

print(find_employees(df))
