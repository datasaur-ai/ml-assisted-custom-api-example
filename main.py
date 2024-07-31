from fastapi import FastAPI
from textblob import TextBlob

import schema

app = FastAPI()


@app.post("/row-based", response_model_exclude_none=True)
async def handle_row_based_request(
    row_based_input: list[schema.RowBasedInputItem],
) -> list[schema.RowBasedOutputItem]:
    # Implement your custom logic here
    return [
        schema.RowBasedOutputItem(id=item.id, label=get_sentiment_label(item.text))
        for item in row_based_input
    ]


def get_sentiment_label(text: str) -> str:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
