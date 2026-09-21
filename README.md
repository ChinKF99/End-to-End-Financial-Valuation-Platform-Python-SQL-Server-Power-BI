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

## 🏗️ Data Model/Pipeline Workflow

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
-Scenario Analysis Table (Base vs Bull vs Bear Case)
-Investment Dashboard Table

### PowerBI Dashboard
Contains visualization of the transform data  
-Executive Summary  
-Standard DCF Chart  
-Reverse DCF Chart  
-Scenario Analysis Chart (Base vs Bull vs Bear Case)  
-Portfolio Screener

## 🎯 Question to Analyze
### Executive Summary & Standard DCF Chart:  
-Is the market currently pricing this company above or below its estimated intrinsic value?

### Reverse DCF Chart:  
-How much future growth is the market expecting?  
-Is the market expecting unrealistic growth?

### Scenario Analysis Chart:  
-How much does intrinsic value change under different business assumptions?

### Portfolio Screener:  
-How do different sectors compare?

## 🔍 Insights  
### Executive Summary/Standard DCF Chart:  
-Most large-cap technology stocks trade above Standard DCF intrinsic value, which indicates that the market is pricing in future growth well beyond historical performance.

### Reverse DCF Chart:  
-Reverse DCF reveals the market's growth expectations, several companies require exceptionally high future growth to justify today's valuation. (E.g. Apple, Amazon, AMD, Microsoft)  

### Scenario Analaysis Chart:  
-Scenario Analysis highlights valuation sensitivity, changing only a few assumptions produces large valuation differences.  
-This demonstrates why DCF outputs should always be interpreted together with scenario analysis rather than as a single absolute value.


## 💡 Business Recommendations:
-Do not rely solely on Standard DCF, it should be used as one valuation framework rather than the only investment decision tool.  

-Use Reverse DCF to understand market expectations, as it provides valuable insight into whether current market prices already assume aggressive future growth.  

-Focus on companies with both Positive Margin of Safety & Reasonable Implied Growth, it represent better long-term investment opportunities because they combine attractive valuation with realistic market expectations.  

-Use Scenario Analysis for risk assessment, instead of making decisions based on one valuation investor should compare different cases to understand downside risk and upside potential.

## ✅ Conclusion
This project demonstrates how a complete financial data pipeline can automate the investment valuation process from raw financial statements to interactive business intelligence dashboards.

The solution integrates:  
Python  
SQL Server  
ETL Pipeline  
Financial Modelling  
Discounted Cash Flow  
Reverse DCF  
Scenario Analysis  
Power BI  

Into a fully automated workflow. Rather than relying solely on intrinsic value estimates, the project combines multiple valuation approaches to provide deeper insight into market expectations, valuation sensitivity, and investment risk.

The modular Bronze–Silver–Gold architecture also makes the solution scalable and maintainable, allowing additional valuation models or financial metrics to be incorporated with minimal changes.

Overall, the project demonstrates practical skills in:  
-Data Engineering  
-ETL Development  
-Financial Data Analysis  
-SQL Database Design  
-Python Automation  
-Business Intelligence  
-Data Visualization

making it representative of an end-to-end data analytics project suitable for investment research and financial decision support.

