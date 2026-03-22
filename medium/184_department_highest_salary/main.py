import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    merged = employee.merge(
        department, how="left", left_on="departmentId", right_on="id"
    )

    merged["max_salary"] = merged.groupby("name_y")["salary"].transform("max")

    df = merged[merged["salary"] == merged["max_salary"]]

    result = df[["name_y", "name_x", "salary"]]

    result.columns = ["Department", "Employee", "Salary"]

    return result


employee = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5],
        "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
        "salary": [70000, 90000, 80000, 60000, 90000],
        "departmentId": [1, 1, 2, 2, 1],
    }
)

department = pd.DataFrame({"id": [1, 2], "name": ["IT", "Sales"]})


print(department_highest_salary(employee, department))
