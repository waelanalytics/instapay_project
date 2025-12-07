# instapay_project
End-to-End Data Analysis Project for InstaPay Egypt App using Python, SQL, and Power BI.
# 📱 InstaPay Egypt: User Sentiment Analysis & ETL Project

![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-Web%20Scraping-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 📊 Project Overview
This project analyzes the user experience of **InstaPay Egypt**, the leading instant payment network in the region. By scraping over **24,000 real user reviews** from the Google Play Store, building an automated ETL pipeline, and visualizing the data, this project aims to provide actionable insights into user satisfaction and technical stability.

### 🎯 Key Objectives
*   **Data Collection:** Automated scraping of Arabic user reviews using Python.
*   **Data Warehousing:** Designing a MySQL database schema to store and manage large datasets.
*   **Sentiment Analysis:** Categorizing user feedback (Positive, Negative, Neutral) to identify pain points.
*   **Visualization:** Creating an interactive Power BI dashboard for business stakeholders.

---

## 📸 Dashboard Preview
*(A snapshot of the interactive dashboard analyzing 24K+ reviews)*

![Dashboard Screenshot](dashboard_screenshot.png)
<!-- 👆 Make sure to upload your screenshot and name it 'dashboard_screenshot.png' -->

---

## 🛠️ Tech Stack & Tools Used

| Category | Tool | Usage |
| :--- | :--- | :--- |
| **Data Collection** | **Python** | Used `google-play-scraper` & `pandas` to extract data. |
| **ETL & Storage** | **MySQL** | Stored raw and transformed data with UTF-8 support for Arabic text. |
| **Data Cleaning** | **Pandas / SQL** | Handled missing values, date formatting, and emoji support. |
| **Visualization** | **Power BI** | Built KPI cards, Sentiment Donut charts, and Time-series analysis. |

---

## 🔄 The ETL Pipeline (How it works)

1.  **Extract:** The Python script (`scraper.py`) connects to Google Play Store and scrapes the latest 24,000 reviews.
2.  **Transform:** Data is cleaned using Pandas (handling dates, filtering columns).
3.  **Load:** The script (`upload_to_db.py`) uses `mysql-connector` to push data into a local MySQL Database, handling Arabic encoding (`utf8mb4`).
4.  **Analyze:** Power BI connects directly to the MySQL database view (`v_reviews_dashboard`) to fetch real-time insights.

---

## 📈 Key Insights
*   **Overall Satisfaction:** The app maintains a high positive sentiment ratio, indicating strong market fit.
*   **Volume:** Analyzed a sample size of **24,595** reviews.
*   **Critical Issues:** Negative feedback is often correlated with specific update dates (visible in the Time-Series chart), allowing developers to pinpoint buggy releases.

---

## 💻 How to Run This Project
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/InstaPay-Analysis-Egypt.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install google-play-scraper pandas mysql-connector-python
    ```
3.  **Setup Database:** Run the SQL script provided in `database_setup.sql` to create the schema.
4.  **Run ETL:** Execute `scraper.py` then `upload_to_db.py`.
5.  **Open Dashboard:** Open `InstaPay_Dashboard.pbix` in Power BI Desktop.

---

## 👤 Author
**Wael Yousef**
*Data Analyst | Python | SQL | Power BI*

Don't hesitate to reach out or check my portfolio:
*   🌐 **Portfolio:** [waelanalytics.carrd.co](https://waelanalytics.carrd.co/)
*   💼 **LinkedIn:** [Wael Yousef](https://www.linkedin.com/in/wael-yousef-data-analyst/)

---
*Disclaimer: This project is for educational and analytical purposes only and is not affiliated with InstaPay Egypt.*
