# Lead Generation Automation Pipeline

## Overview

This project is a Python-based automation pipeline that collects, processes, and serves lead data using both scripting and API-based architecture. It demonstrates practical implementation of data automation, preprocessing, and backend service integration.

---

## Features

* Data collection via API and web scraping
* Data cleaning and preprocessing using pandas
* Email generation and validation
* Data quality scoring system
* Export to Excel and CSV
* Command-line interface (CLI) support
* Logging for execution tracking
* FastAPI-based backend service

---

## Tech Stack

* Python
* Pandas
* Requests, BeautifulSoup
* FastAPI

---

## How to Run

### Run pipeline

```bash
python main.py --source api
```

### Run API

```bash
python -m uvicorn api:app --reload
```

---

## API Usage

Open in browser:
http://127.0.0.1:8000/docs

Available endpoints:

* `/generate` – Generate lead data
* `/health` – Check API status

---

## Output

Generated files:

* outputs/leads.csv
* outputs/leads.xlsx

---

## Approach

1. Collect data from API or web scraping
2. Clean and structure data using pandas
3. Generate email patterns
4. Assign data quality scores
5. Export results and serve via API

---

## Future Improvements

* Database integration (PostgreSQL or MongoDB)
* Cloud deployment (Render, AWS, etc.)
* Advanced email validation using external APIs
* Scheduled automation using cron jobs

---

## Demo

Include screenshots of:

* FastAPI Swagger UI
* Output files (Excel/CSV)

---

## Key Learning

This project demonstrates modular system design, automation of data workflows, and extension of scripts into scalable backend services using APIs.
