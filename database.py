from sqlalchemy import create_engine
import pandas as pd

def save_to_database(data):
    engine=create_engine("sqlite:///scholarships.db")
    df=pd.DataFrame(data)
    df.drop_duplicates(inplace=True)
    df.to_sql(
        "scholarships",
        engine,
        if_exists="replace",
        index=False
    )
    print("Data saved to scholarships.db successfully!")