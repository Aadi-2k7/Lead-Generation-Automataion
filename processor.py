import pandas as pd
from utils import generate_email, validate_email

def process_data(data):
    df = pd.DataFrame(data)

    df.drop_duplicates(inplace=True)
    df.fillna("Not Available", inplace=True)

    df["email"] = df.apply(
        lambda row: generate_email(row["name"], row["website"]), axis=1
    )

    df["email"] = df["email"].apply(validate_email)

    df["quality_score"] = df.apply(score_row, axis=1)

    return df


def score_row(row):
    score = 0
    if row["name"] != "Not Available":
        score += 1
    if row["website"] != "Not Available":
        score += 1
    if row["email"]:
        score += 1
    return score