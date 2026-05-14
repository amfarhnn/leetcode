import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    scores_list = pd.DataFrame({
        "score" : scores['score'].sort_values(ascending=False)
    }
    )

    scores_list["rank"] = scores_list['score'].rank(
        method='dense',
        ascending=False
    )

    return scores_list