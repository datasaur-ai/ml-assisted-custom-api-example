import spacy
from fastapi import FastAPI
from textblob import TextBlob

import schema

nlp = spacy.load("en_core_web_sm")

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


@app.post("/span-based", response_model_exclude_none=True)
async def handle_span_based_request(
    span_based_input: schema.SpanBasedInput,
) -> schema.SpanBasedOutput:
    # Implement your custom logic here
    return schema.SpanBasedOutput(
        id=span_based_input.id,
        documents=[
            schema.SpanBasedOutputDocument(
                id=document.id,
                labels=[
                    schema.SpanBasedOutputLabel(
                        id=sentence.id,
                        entities=get_entities(sentence.text),
                    )
                    for sentence in document.sentences
                ],
            )
            for document in span_based_input.documents
        ],
    )


def get_sentiment_label(text: str) -> str:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


def get_entities(text: str) -> list[schema.SpanBasedOutputEntity]:
    doc = nlp(text)
    return [
        schema.SpanBasedOutputEntity(
            label=ent.label_,
            start_char=ent.start_char,
            end_char=ent.end_char,
        )
        for ent in doc.ents
    ]
