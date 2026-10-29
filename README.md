# 🏏 IPL Data Analytics Dashboard

An interactive IPL data analytics dashboard built using **Flask, a database, and data visualisations** to explore cricket statistics, analyse player performances, and discover insights through dynamic filters.

## 📌 Project Overview

The IPL Data Analytics Dashboard is a web-based application designed to make cricket data easier to explore and understand. It combines a Flask backend, database integration, and interactive visualisations to help users investigate IPL statistics and performance trends.

The dashboard provides a centralised interface for exploring data, comparing performance indicators, and identifying patterns through visual analytics.

## 🎯 Objectives

- Analyse IPL-related cricket data through interactive visualisations.
- Store and retrieve structured data using a database.
- Enable users to filter datasets and explore specific results.
- Present cricket statistics in an accessible, user-friendly dashboard.
- Practise the integration of backend development, database management, and data visualisation.

## ✨ Key Features

- **Interactive Dashboard:** Explore IPL statistics through visual summaries and charts.
- **Database Integration:** Retrieve and display data stored in the project's database.
- **Dynamic Filters:** Narrow down the displayed data using available filter options.
- **Performance Analysis:** Explore player or team statistics supported by the dataset.
- **Visual Data Exploration:** Understand patterns and comparisons through graphical representations.
- **Flask Web Application:** Access the dashboard through a browser-based interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and application logic |
| Flask | Web application backend |
| Database | Structured data storage and retrieval |
| HTML / CSS | Dashboard structure and styling |
| JavaScript | Interactive behaviour, if implemented |
| Data Visualisation Library | Charts and graphical representations |

*Update the table with your exact database, charting library, and frontend technologies.*

## 📊 Dashboard Highlights

The dashboard combines database-backed data exploration with visual reporting.

Depending on the visualisations implemented, the analysis may include:

- Team performance comparisons
- Player statistics and performance trends
- Match-level statistics
- Filter-based exploration of relevant records

The available filters and charts depend on the underlying dataset and current application implementation.

## 🗂️ Project Structure

A typical Flask project structure could look like this:

```text
IPL-Data-Dashboard/
│
├── app.py                  # Flask application entry point
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript and images
├── database/               # Database file or related scripts
├── data/                   # Source datasets, if included
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files excluded from Git
```

*Adjust the structure above to match your actual project files.*

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Git
- The database system required by the project

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If you use Command Prompt instead:

```bat
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Ensure the database is available and configure the required connection settings. If the project uses a local SQLite database, verify that the database file is present or that the application can initialise it.

Add any required environment variables before starting the application.

### 5. Run the application

```bash
python app.py
```

Open the local address shown in the terminal in your browser. A common Flask development address is `http://127.0.0.1:5000/`, although your application may use a different port or route.

## 📈 Skills Demonstrated

- Data analysis and exploration
- Database integration and querying
- Python application development
- Flask backend development
- Data visualisation and dashboard design
- Interactive data filtering
- Data-driven presentation of insights

## 🔮 Future Improvements

Potential enhancements include:

- Adding more detailed player and team performance comparisons
- Introducing additional filters and visualisations
- Improving dashboard responsiveness and usability
- Adding predictive analytics for player performance, if supported by suitable historical data
- Deploying the application so it can be accessed online

## 👨‍💻 Author

**Soham Ghosh**

B.Sc. Data Science graduate (2025), interested in Data Analytics, Data Visualisation, SQL, Python, and Machine Learning.

- **GitHub:** [SohamG27](https://github.com/SohamG27)
- **LinkedIn:** [Soham Ghosh](https://www.linkedin.com/in/soham-ghosh-93b565199/)

---

*This project is part of my ongoing journey to strengthen my practical skills in data analytics, visualisation, and data-driven problem-solving.*
