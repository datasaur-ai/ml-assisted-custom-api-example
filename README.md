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

2. Run service

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
