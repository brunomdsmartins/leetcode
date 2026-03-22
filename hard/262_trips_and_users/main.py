import pandas as pd


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips["request_at"] = pd.to_datetime(trips["request_at"])

    mask = (trips["request_at"] >= "2013-10-01") & (trips["request_at"] <= "2013-10-03")
    trips = trips.loc[mask]

    trips = trips.merge(
        users[["users_id", "banned"]],
        how="left",
        left_on="client_id",
        right_on="users_id",
    ).drop(columns=["users_id"])

    trips = trips.rename(columns={"banned": "client_banned"})

    trips = trips.merge(
        users[["users_id", "banned"]],
        how="left",
        left_on="driver_id",
        right_on="users_id",
    ).drop(columns=["users_id"])

    trips = trips.rename(columns={"banned": "driver_banned"})

    trips = trips[(trips["client_banned"] == "No") & (trips["driver_banned"] == "No")]

    trips["status"] = (
        trips["status"].isin(["cancelled_by_client", "cancelled_by_driver"]).astype(int)
    )

    grouped = trips.groupby("request_at").agg(
        n_trips=("id", "count"), cancelled=("status", "sum")
    )

    grouped["result"] = (grouped["cancelled"] / grouped["n_trips"]).round(2)

    return (
        grouped[["result"]]
        .reset_index()
        .rename(columns={"request_at": "Day", "result": "Cancellation Rate"})
    )


trips = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "client_id": [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
        "driver_id": [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
        "city_id": [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
        "status": [
            "completed",
            "cancelled_by_driver",
            "completed",
            "cancelled_by_client",
            "completed",
            "completed",
            "completed",
            "completed",
            "completed",
            "cancelled_by_driver",
        ],
        "request_at": [
            "2013-10-01",
            "2013-10-01",
            "2013-10-01",
            "2013-10-01",
            "2013-10-02",
            "2013-10-02",
            "2013-10-02",
            "2013-10-03",
            "2013-10-03",
            "2013-10-03",
        ],
    }
)

users = pd.DataFrame(
    {
        "users_id": [1, 2, 3, 4, 10, 11, 12, 13],
        "banned": ["No", "Yes", "No", "No", "No", "No", "No", "No"],
        "role": [
            "client",
            "client",
            "client",
            "client",
            "driver",
            "driver",
            "driver",
            "driver",
        ],
    }
)


print(trips_and_users(trips, users))
