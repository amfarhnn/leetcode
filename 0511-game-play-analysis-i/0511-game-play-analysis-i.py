import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["rank_date"] = activity.sort_values('event_date').groupby('player_id').cumcount() + 1

    result = activity[(activity["rank_date"] == 1)]
    return pd.DataFrame({
        "player_id" : result["player_id"],
        "first_login" : result["event_date"]
        })