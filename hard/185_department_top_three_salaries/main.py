import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    merged = employee.merge(
        department, how="left", left_on="departmentId", right_on="id"
    )

    merged["rank"] = merged.groupby("name_y")["salary"].rank(
        method="dense", ascending=False
    )

    df = merged[merged["rank"] <= 3][["name_y", "name_x", "salary"]]

    df.columns = ["Department", "Employee", "Salary"]

    return df


employee = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6, 7],
        "name": ["Joe", "Henry", "Sam", "Max", "Janet", "Randy", "Will"],
        "salary": [85000, 80000, 60000, 90000, 69000, 85000, 70000],
        "departmentId": [1, 2, 2, 1, 1, 1, 1],
    }
)

department = pd.DataFrame({"id": [1, 2], "name": ["IT", "Sales"]})

print(top_three_salaries(employee, department))
