# Data Dictionary: Comparable Properties Database

**Project:** Real Estate Appraisal System  
**Version:** 1.0  
**Database Type:** SQLite3  

## Table: `comparables`
This table stores the historical sales data used for property valuation and market analysis.

| Column Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | Primary Key. Unique identifier for each record. | 1, 2, 3... |
| `sale_date` | TEXT | The date when the transaction was completed (ISO 8601 format). | 2026-03-15 |
| `property_name`| TEXT | The name of the building or specific property identification. | Blue Horizon Villa |
| `parish_region`| TEXT | The administrative region or parish where the property is located. | St. James |
| `zoning` | TEXT | Local government classification for land use. | Residential / Commercial |
| `property_type`| TEXT | Category of the property (e.g., House, Condo, Land). | Single Family |
| `lot_size_sqft`| REAL | The total area of the land in Square Feet. | 5000.50 |
| `bldg_size_sqft`| REAL | The total area of the building/structure in Square Feet. | 2400.00 |
| `sale_price` | REAL | The final price the property was sold for. | 450000.00 |
| `price_per_sqft`| REAL | Calculated field: `sale_price` divided by `bldg_size_sqft`. | 187.50 |
| `remarks` | TEXT | Additional notes, descriptions, or unique property features. | Recently renovated. |

---

## Technical Notes for the Appraiser:
1. **Numeric Integrity:** All currency values are stored as decimals (REAL) without symbols ($) to allow for mathematical sorting.
2. **Search Optimization:** The database includes an index on `parish_region` and `sale_price` to ensure instantaneous search results.
3. **Empty Fields:** If a piece of information was missing in the original Excel, the field will contain `NULL`.
