import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Lead Generation Automation Tool")

    parser.add_argument("--source", choices=["scrape", "api"], default="api")
    parser.add_argument("--export", choices=["excel", "csv", "both"], default="both")
    parser.add_argument("--sheets", action="store_true")

    return parser.parse_args()