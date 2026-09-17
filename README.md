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
Financial Modeling Prep API  
            │  
            ▼  
     Bronze Layer
 (Raw Financial Data)
            │
            ▼
     Silver Layer
(Data Cleaning & Feature Engineering)
            │
            ▼
      Gold Layer
 (Business Valuation Models)
            │
            ▼
      SQL Server
            │
            ▼
      Power BI Dashboard