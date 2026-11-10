# 🎬 Streaming Intelligence Platform

A Netflix-style analytics platform that transforms streaming data into actionable business intelligence. The platform provides insights into user engagement, content performance, subscription behavior, and personalized recommendations through interactive dashboards.

---

## 🚀 Features

### 👥 User Analytics
- Analyze streaming behavior across users
- Track engagement levels
- Understand subscription patterns
- Explore country-wise user distribution

### 🎥 Content Analytics
- Identify top-performing movies and shows
- Analyze content ratings and popularity
- Discover viewing trends across genres

### 📊 Platform Intelligence
- Total watch time tracking
- Average engagement metrics
- Subscription performance analysis
- Genre popularity insights

### 🤖 Recommendation Engine
- Simple content recommendations based on viewing history
- Genre-based personalized suggestions
- Foundation for advanced recommendation systems

### 📈 Interactive Dashboard
- Real-time KPI monitoring
- Dynamic visualizations using Plotly
- User-friendly Streamlit interface

---

## 🏗️ Project Architecture

```text
Users Data
      │
      ▼
Watch History Data
      │
      ▼
Content Metadata
      │
      ▼
Data Processing Layer (Pandas)
      │
      ▼
Analytics Engine
      │
      ├── User Analytics
      ├── Content Analytics
      ├── Engagement Analytics
      └── Recommendation Engine
      │
      ▼
Streamlit Dashboard
```

---

## 🛠️ Technology Stack

### Backend
- Python

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly
- Streamlit

### Machine Learning
- Scikit-Learn

### Data Storage
- CSV Files (V1)

---

## 📂 Project Structure

```text
streaming_intelligence_platform

app.py
requirements.txt
README.md

users.csv
content.csv
watch_history.csv

generate_data.py
```

---

## 📋 Dataset Overview

### users.csv
Contains user demographics and subscription information.

| Column | Description |
|----------|-------------|
| user_id | Unique user identifier |
| age | User age |
| country | User location |
| subscription | Subscription plan |

---

### content.csv
Contains movie and show metadata.

| Column | Description |
|----------|-------------|
| content_id | Unique content identifier |
| title | Movie/Show title |
| genre | Content genre |
| rating | IMDb-style rating |

---

### watch_history.csv
Contains user viewing activity.

| Column | Description |
|----------|-------------|
| user_id | User identifier |
| content_id | Content identifier |
| watch_time | Minutes watched |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/streaming-intelligence-platform.git

cd streaming-intelligence-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📊 Current Dashboard Modules

### KPI Dashboard
- Total Users
- Total Content
- Total Watch Time
- Average Watch Time

### Genre Analytics
- Most popular genres
- Watch-time distribution

### Content Performance
- Top watched titles
- Engagement ranking

### Subscription Insights
- Plan comparison
- User behavior analysis

### Recommendation System
- Genre-based recommendations
- Personalized content suggestions

---

## 🔮 Future Enhancements

### V2 — Advanced Analytics
- User Segmentation (K-Means)
- Churn Prediction
- Engagement Scoring
- Cohort Analysis

### V3 — Data Engineering Layer
- PostgreSQL Data Warehouse
- ETL Pipelines
- Airflow Orchestration
- Automated Data 
