import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person["duplicated"] = person["email"].duplicated()

    df = pd.DataFrame({"email": person[person["duplicated"]]["email"].unique()})

    return df


df = pd.DataFrame({"id": [1, 2, 3], "email": ["a@b.com", "c@d.com", "a@b.com"]})

print(duplicate_emails(df))
