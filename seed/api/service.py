import pandas as pd

from seed.api.config import REVIEW_FILE


class ReviewService:

    @staticmethod
    def get_reviews():

        df = pd.read_csv(REVIEW_FILE)

        # Replace NaN with None (JSON null)
        df = df.where(pd.notnull(df), None)

        return df.to_dict(orient="records")