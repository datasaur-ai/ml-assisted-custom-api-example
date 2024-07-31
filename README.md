# ML-Assisted Custom API Example

Example Python REST API Server Implementation for Datasaur ML-Assisted Labeling Custom API.

## Prerequisites

1. Install Python >= 3.12

2. Install [Poetry](https://python-poetry.org/docs/#installation) ~= 1.8

## Getting Started

1. Install dependencies

   ```sh
   poetry install
   ```

2. Download spacy model

   ```sh
   spacy download en_core_web_sm
   ```

3. Run service

   ```sh
   fastapi run main.py
   ```

## API Endpoints

### POST /row-based

Accept a list of input rows and return a list of sentiment analysis results (Positive, Negative, or Neutral).

Request:

```json
[
  {
    "id": 1,
    "text": "Product A I love this product",
    "columns": ["Product A", "I love this product"],
    "column_names": ["Product Name", "Product Review"]
  }
]
```

Response:

```json
[
  {
    "id": 1,
    "label": "Positive"
  }
]
```

### POST /span-based

Accepts a project with documents and sentences, and returns entities recognized in the text.

Request:

```json
{
  "id": "project_id",
  "name": "project_name",
  "documents": [
    {
      "id": "document_id",
      "sentences": [
        {
          "id": 0,
          "text": "John works at Abcd Corp."
        }
      ]
    }
  ]
}
```

Response:

```json
{
  "id": "project_id",
  "documents": [
    {
      "id": "document_id",
      "labels": [
        {
          "id": 0,
          "entities": [
            {
              "label": "PERSON",
              "start_char": 0,
              "end_char": 4,
              "layer": 0
            },
            {
              "label": "ORG",
              "start_char": 14,
              "end_char": 24,
              "layer": 0
            }
          ]
        }
      ]
    }
  ]
}
```
