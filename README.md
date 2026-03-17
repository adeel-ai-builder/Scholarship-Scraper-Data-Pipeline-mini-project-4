# Scholarship-Scraper-Data-Pipeline-mini-project-4

## Project Overview

This project is an automated web scraping and data pipeline system designed to collect scholarship-related data from multiple pages, process it, and store it in structured formats for analysis.

The system follows a modular and scalable architecture, separating scraping, parsing, and database operations—aligning with industry-level data engineering practices.

## Business Objective

### The purpose of this project is to:

### Collect scholarship-related data automatically

### Structure and store data for easy access and analysis

### Build a scalable pipeline for future expansion

### Support use cases like:

          Scholarship recommendation systems

          Student opportunity platforms

          Data-driven decision making

## Key Features

✔ Multi-page web scraping

✔ Modular architecture (Scraper + Parser + Database)

✔ Data cleaning and deduplication

✔ Structured data storage (CSV + SQLite)

✔ Error handling for robust scraping

✔ Scalable pipeline design

## Technologies Used

Python

Requests

BeautifulSoup

Pandas

SQLAlchemy

SQLite

## Project Structure

scholarship-data-pipeline/

              │
              ├── data/
              │   └── scholarships.csv
              │
              ├── database/
              │   └── scholarships.db
              
              ├── scripts/
              │   ├── scraper.py
              │   ├── parser.py
              │   ├── database.py
              │   └── main.py
              │
              ├── README.md
              └── requirements.txt
              
## Pipeline Architecture

### 1️⃣ Data Collection (Scraper)

Scrapes data from multiple pages

Uses HTTP requests with headers

Handles errors and timeouts

👉 Implemented in scraper.py

### 2️⃣ Data Parsing

Extracts structured data from HTML

Extracted fields:

Title

Country (placeholder)

Deadline

Link

👉 Implemented in parser.py

### 3️⃣ Data Processing & Orchestration

Combines data from all pages

Removes duplicates

Converts deadline column into datetime format

Saves data into CSV

👉 Implemented in main.py

### 4️⃣ Data Storage

Stores data into SQLite database

Ensures clean and structured storage

👉 Implemented in database.py

## How to Run the Project

### Step 1: Clone Repository

git clone https://github.com/yourusername/scholarship-data-pipeline.git

cd scholarship-data-pipeline

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Run the Pipeline
python main.py

### Output

CSV file → data/scholarships.csv

SQLite database → scholarships.db

## Example Output
Title	           Country	   Deadline

Scholarship A	   UK	         2025-12-01

## Key Insights

Demonstrates multi-page scraping capability

Shows how to build end-to-end data pipelines

Highlights importance of data cleaning and structuring

## Industry-Level Highlights

### This project follows best practices:

✔ Modular architecture (separation of concerns)

✔ Data pipeline orchestration

✔ Error handling (important for real systems)

✔ Database integration

✔ Clean and scalable design

## Future Improvements

Replace dummy data with real scholarship APIs

Add filtering (country, deadline, category)

Build REST API for data access

Deploy pipeline using Airflow

Add dashboard (Streamlit / Power BI)

## Author

### Adeel Khan
### Aspiring Data Engineer
