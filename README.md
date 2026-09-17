# 📊 Dashboard
<div style="display: flex; flex-direction: column; align-items: center;">
    <img src="powerbi/Executive Summary.png" alt="Executive Summary" width="1923" height="1093">
    <img src="powerbi/Company Analysis.png" alt="Company Analysis" width="1923" height="1093">
    <img src="powerbi/Standard DCF Analysis.png" alt="Standard DCF" width="1923" height="1093">
    <img src="powerbi/Reverse DCF Analysis.png" alt="Reverse DCF" width="1923" height="1093">
    <img src="powerbi/Portfolio Screener.png" alt="Portfolio Screener" iwidth="1923" height="1093">
</div>

## 📌 Introduction/Project Overview  
This project is an end-to-end stock valuation pipeline built using Python, SQL Server, and Power BI.

The objective is to automate the entire valuation process, starting from downloading raw financial statements, transforming them into analytics-ready datasets, calculating intrinsic values using multiple Discounted Cash Flow (DCF) models, and presenting the results through an interactive Power BI dashboard.

The project follows a modern Medallion Architecture (Bronze → Silver → Gold) commonly used in real-world data engineering projects.

## Dashboard File  
My final dashboard file is in [dashboard.pbix](powerbi/StockAutomation.pbix)

## Project Architecture  
<table>
  <tr align="center">
    <td>
      Financial Modeling Prep API <br>
      │ <br>
      ▼ <br>
      **Bronze Layer** <br>
      (Raw Financial Data) <br>
      │ <br>
      ▼ <br>
      **Silver Layer** <br>
      (Data Cleaning & Feature Engineering) <br>
      │ <br>
      ▼ <br>
      **Gold Layer** <br>
      (Business Valuation Models) <br>
      │ <br>
      ▼ <br>
      **SQL Server** <br>
      │ <br>
      ▼ <br>
      **Power BI Dashboard**
    </td>
  </tr>
</table>

## ⚙️ Tech Stack
| Category        | Technology                  |
| --------------- | --------------------------- |
| Language        | Python                      |
| Database        | SQL Server Express          |
| ETL             | Pandas + SQLAlchemy         |
| API             | Financial Modeling Prep API |
| Visualization   | Power BI                    |
| IDE             | VS Code                     |
| Version Control | Git & GitHub                |

## 🔧 Pipeline Workflow  

### Bronze Layer  
Responsible for downloading raw financial data from Financial Modeling Prep & loading it into SQL server.
-Company Information  
-Income Statement  
-Balance Sheet  
-Cash Flow  
-Financial Ratios

### Silver Layer  
Transforms raw financial data into clean analytics tables.  
-Company Financials Table  
-Growth Metrics Table    
-Financial Ratios

### Gold Layer
Contains business valuation models.
-DCF Assumptions Table  
-Standard DCF Table  
-Reverse DCF Table  
-Scenario Analysis Table  
-Investment Dashboard Table

## 🎯 Question to Analyze and why
