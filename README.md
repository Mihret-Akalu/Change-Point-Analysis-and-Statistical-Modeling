
```markdown
# 📊 Change Point Analysis and Statistical Modeling of Brent Oil Prices

**Brent crude oil price analysis (1987 – 2022) using Bayesian Change Point Detection, with an interactive dashboard.**

This project identifies structural breaks in Brent oil prices using Bayesian inference (PyMC) and links them to significant geopolitical and economic events. It provides insights for investors, policymakers, and analysts struggling to interpret volatile oil markets.

---

## 🧠 Project Overview

The global oil market is highly volatile — influenced by conflicts, policy decisions, economic shocks, and supply changes. This repository:

- Detects **change points** in Brent oil price time series from **1987 to November 14, 2022**.  
- Uses a **Bayesian statistical model** to quantify regime shifts.  
- Maps identified change points to a curated list of **key historical events**.  
- Serves results via an **interactive dashboard** built with **Flask (backend)** and **React (frontend)**.

---

## 📂 Repository Structure

```

.
├── data/
│   ├── BrentOilPrices.csv         # Daily Brent price data (1987–2022)
│   ├── oil_events.csv             # Major geopolitical & economic events
│   └── change_points.csv          # Estimated change points from model
├── notebooks/
│   ├── 01_task1_foundation.ipynb  # Task 1: Workflow & model understanding
│   ├── 02_EDA.ipynb               # Exploratory Data Analysis
│   ├── 03_single_changepoint.ipynb# Single CP Bayesian model
│   └── 04_multi_changepoint.ipynb # Multiple CP Bayesian model
├── backend/
│   ├── app.py                     # Flask API for dashboard data
│   └── requirements.txt           # Dependencies for backend
├── frontend/
│   ├── package.json               # React app dependencies
│   └── src/
│       └── App.js                 # React frontend code
├── README.md                      # This documentation
└── reports/
└── analysis_report.pdf        # Optional: narrative report

````

---

## 💡 Key Features

### 🧩 Statistical Modeling  
- Bayesian change point analysis with **PyMC**  
- Posterior distributions for regime parameters  
- Model diagnostics (R‑hat, trace plots, credible intervals)  
- Single and multiple change point detection

### 🔍 Exploratory Analysis  
- Log returns to assess stationarity  
- Time series plots with volatility and trend analysis

### 📅 Event Correlation  
- `oil_events.csv` lists at least 10 major historical events  
- Enables association of price shifts with real world events

### 📊 Dashboard Visualizations  
- Flask backend serves price, events, and model outputs  
- React frontend visualizes results with interactive charts

---

## 🚀 Getting Started

### 🧾 Prerequisites

You need:

- Python (≥ 3.8)  
- Node.js and npm (for frontend)

---

## 🐍 Backend Setup (Flask)

1. Navigate to backend folder:
   ```bash
   cd backend
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask API:

   ```bash
   python app.py
   ```

The API will start on `http://localhost:5000`.

---

## ⚛️ Frontend Setup (React)

1. Navigate to frontend folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

The dashboard will open in your browser (usually at `http://localhost:3000`).

---

## 📊 How to Use

1. Start the **backend** (Flask)
2. Start the **frontend** (React)
3. Open the dashboard in your browser
4. Explore:

   * Price trends and volatility
   * Bayesian change points
   * Event overlays
   * Filters and date selectors

---

## 🧪 Example API Endpoints

| Endpoint             | Description                          |
| -------------------- | ------------------------------------ |
| `/api/prices`        | Returns Brent price data             |
| `/api/events`        | Returns curated historical events    |
| `/api/change_points` | Returns estimated change point dates |

---

## 📄 Data Files

### `BrentOilPrices.csv`

Contains daily Brent crude oil prices from **May 20, 1987** to **November 14, 2022**.

### `oil_events.csv`

Contains curated events with:

* Date
* Event name
* Category (e.g., Conflict, Policy, Economic)
* Description

Example:

```
Date,Event,Category,Description
1990-08-02,Iraq Invades Kuwait,Conflict,Started the Gulf War and caused a massive price spike.
2008-09-15,Lehman Brothers Collapse,Economic,Global financial crisis led to a sharp drop in demand.
2020-03-09,COVID Price War,Economic,Saudi Arabia and Russia price war coincided with global lockdowns.
```

---

## 📚 Additional Resources

* Notebooks document code and explanations step by step.
* The `reports/` folder can include a narrative PDF if needed.

---

