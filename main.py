from scraper import scrape_companies
from api_source import fetch_from_api
from processor import process_data
from exporter import export_data
from cli import parse_args
from logger import setup_logger
import logging
import os

def run_pipeline(args=None):
    setup_logger()
    logging.info("Pipeline started")

    os.makedirs("outputs", exist_ok=True)

    if args and args.source == "scrape":
        data = scrape_companies()
        if not data:
            print("Scraping failed, switching to API...")
            data = fetch_from_api()
    else:
        data = fetch_from_api()

    df = process_data(data)

    export_type = args.export if args else "both"
    export_data(df, export_type)

    logging.info("Pipeline completed")
    print("✅ Data saved successfully in outputs folder")

if __name__ == "__main__":
    args = parse_args()
    run_pipeline(args)