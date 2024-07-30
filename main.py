from fastapi import FastAPI
from textblob import TextBlob

import schema

app = FastAPI()


@app.post("/row-based", response_model_exclude_none=True)
async def handle_row_based_request(
    *, obj_in: list[schema.RowBasedInputItem]
) -> list[schema.RowBasedOutputItem]:
    results: list[schema.RowBasedOutputItem] = []

    # Implement your custom logic here
    for row in obj_in:
        label = get_sentiment_analysis_label(row.text)
        result = schema.RowBasedOutputItem(id=row.id, label=label)
        results.append(result)

    return results


def get_sentiment_analysis_label(text: str) -> str:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
