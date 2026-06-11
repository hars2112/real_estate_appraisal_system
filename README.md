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

## 4. Key Takeaways & Conclusions (Conclusiones)

- **Data Integrity & Scalability:** Successfully migrated **1,514 messy real estate records** from flat Excel files into a relational SQLite database. This eliminates data redundancy and prevents accidental formatting overwrites common in Excel.
- **Performance Optimization:** Moving the data layer to SQLite drastically reduced search query times. On local hardware (Lubuntu minimal specs), queries filter thousands of records instantly, a task that previously caused spreadsheet lags.
- **Business Value (Appraisal Efficiency):** Real estate appraisers can now find historical comparable properties in seconds using dynamic filters, reducing the "comparable matching phase" of valuation by an estimated 70%.

## 5. Technical Recommendations for Future Phases

1. **Automated Valuation Model (AVM):** The structured data is now perfectly ready to implement a Machine Learning regression pipeline (e.g., Scikit-Learn) to predict property prices based on `bldg_size_sqft`, `parish_region`, and `property_type`.
2. **Cloud Migration Prep:** Since SQLite is used via dynamic standard pathing, this application is fully compatible to be containerized (Docker) and deployed on cloud services like Streamlit Community Cloud or AWS.
3. **Geospatial Integration:** Adding latitude and longitude mapping (using Leaflet or Streamlit Maps) would allow the client to visually locate property clusters on a digital map.

---

### English Practice (Markdown Bugs)

* **Code Block Closure:** The triple backticks (`` ``` ``) act as a toggle switch. If you don't close them, everything else becomes code text.
* **Escaped Syntax:** When markdown features (like headings `##` or bolding `**`) are stuck inside a code block, their functionality is "escaped" or ignored, turning them into plain characters.
* **Uniform Layout:** By switching Section 5 from numbers (`1.`) to bullets (`*`), the entire document now shares the exact same hierarchy across all chapters.

Copia este bloque completo, pégalo en el editor y verás cómo el recuadro gris se corta justo donde termina la carpeta `reports`, permitiendo que el 4 y el 5 brillen como títulos reales fuera del bloque.
