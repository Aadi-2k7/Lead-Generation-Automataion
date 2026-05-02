from fastapi import FastAPI
from api_source import fetch_from_api
from scraper import scrape_companies
from processor import process_data

app = FastAPI(title="Lead Generation API")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/generate")
def generate(source: str = "api"):
    if source == "scrape":
        data = scrape_companies()
        if not data:
            data = fetch_from_api()
    else:
        data = fetch_from_api()

    df = process_data(data)

    return {
        "total_records": len(df),
        "data": df.to_dict(orient="records")
    }

@app.get("/health")
def health():
    return {"status": "OK"}