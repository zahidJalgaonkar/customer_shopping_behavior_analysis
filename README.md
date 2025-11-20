🛒 Customer Shopping Behavior Analysis

A professional end-to-end data analysis project focused on understanding customer purchasing patterns, segmentation, and engagement to generate actionable business insights. This repository includes Python scripts, SQL analytics, Power BI dashboards, and fully documented files demonstrating how data-driven decisions enhance customer targeting, retention, and revenue growth.

📁 Repository Contents

-customer_shopping_behavior.csv— Raw dataset used for analysis  
-script.py— Python script for cleaning, processing, and feature engineering  
-customer_behavior_analysis_sql_queries.sql— SQL queries for insights & aggregations  
-customer_behaviour_dashboard.pbix— Interactive Power BI dashboard  
-Customer Shopping Behavior Analysis report.docx— Full project report  
-Customer-Shopping-Behavior-Analysis-PPT.pdf— Presentation summarizing findings  
-Business Problem Statement.docx— Business goals and project scope  

📌 Project Overview

This project analyzes customer shopping behavior to identify the key factors influencing purchasing decisions. It explores spending patterns, category preferences, purchase frequency, discount impact, and overall engagement. The goal is to convert raw behavioral data into meaningful insights that help businesses make smarter decisions across marketing, sales, and product planning.

⭐ Key Features & Deliverables

- 🧹 Cleaned & well-structured dataset  
- 🐍 Python-based data cleaning, transformation & feature engineering  
- 🗄️ SQL queries for segmentation, retention signals & trend extraction  
- 📊 Power BI dashboard with interactive insights  
- 📄 Professional report and presentation with recommendations  

🚀 Quickstart — Run Locally

1️⃣ Clone the Repository
bash
git clone https://github.com/zahidJalgaonkar/customer_shopping_behavior_analysis.git
cd customer_shopping_behavior_analysis
2️⃣ (Optional) Create & Activate a Virtual Environment

bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
3️⃣ Install Required Python Packages
If requirements.txt does not exist:

bash
pip install pandas numpy sqlalchemy psycopg2-binary matplotlib seaborn
4️⃣ Run the Cleaning & Loading Script
bash
python script.py

This script:
Cleans & transforms data
Creates age groups and frequency mappings
Loads cleaned data into PostgreSQL

🗃️ SQL Analysis
5️⃣ Confirm Data Loaded into PostgreSQL
SELECT * FROM customer LIMIT 10;
6️⃣ Run SQL Queries for Insights
Open:
customer_behavior_analysis_sql_queries.sql
These queries include:
Customer segmentation
Category-level performance
Purchase frequency trends
Discount impact analysis
High-value customers (RFM-style metrics)

Example:
SELECT category, COUNT(*), AVG(purchase_amount)
FROM customer
GROUP BY category;

📊 Power BI Dashboard
7️⃣ Open Dashboard File
Launch Power BI Desktop
Open: customer_behaviour_dashboard.pbix

