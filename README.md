# Real Estate Appraisal System

A professional data management and search tool designed to transform raw Excel comparable data into a structured, searchable database for property valuation.

## 1. Project Overview
The goal of this project is to provide a real estate appraiser with a reliable system to store, filter, and export property comparable data. 

### Key Features:
* **Structured Database:** Migration from flat Excel files to a relational SQLite database.
* **Data Normalization:** Automated cleaning of prices, dates, and regions.
* **Dynamic Search:** Advanced filtering by Price, Square Footage, Zoning, and Region.
* **Export Tool:** Ability to generate reports for valuation analysis.

## 2. Technical Stack
To ensure high performance on local hardware, the following tools were selected:
* **Operating System:** Lubuntu (Linux)
* **Language:** Python 3.10+
* **Database Engine:** SQLite3 (Serverless and Lightweight)
* **Data Processing:** Pandas & OpenPyXL
* **Database Management:** DBeaver

## 3. Project Structure
```text
.
├── data
│   ├── raw         # Original client Excel files (.xlsm)
│   └── processed   # Cleaned SQLite database (.db)
├── notebooks       # Jupyter Notebooks for ETL and Analysis
├── src             # Source code for the search interface
├── docs            # User manuals and training materials
└── reports         # Generated exports for the client
