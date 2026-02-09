
```markdown
# Task 1: Laying the Foundation for Brent Oil Price Change Point Analysis

**Objective:** Define the full data analysis workflow and develop a thorough understanding of the model, the data, and the problem context.


```markdown
## 2. Analysis Workflow

We will analyze Brent crude oil prices from 1987 through 14‑Nov‑2022. Our goal is to identify structural breaks and link them to real world events.

### Step 1: Data Loading and Cleaning
- Load `BrentOilPrices.csv` from `data/`.
- Convert the Date column to `datetime`.
- Sort data chronologically.
- Inspect missing values and outliers.

### Step 2: Exploratory Data Analysis (EDA)
- Plot the raw price series to observe long‑term trends and major fluctuations.
- Compute daily log returns: `log(price_t) − log(price_{t−1})`.
- Plot log returns to observe volatility and clustering.

### Step 3: Compile Structured Event Data
- Use a curated list of major events known to influence oil markets.
- Stored in `data/oil_events.csv` with columns Date, Event, Category, Description.

### Step 4: Time Series Property Analysis
- Investigate trend, stationarity, and volatility structure.
- Use statistical tests (e.g., ADF) where appropriate.

### Step 5: Model Definition
- Define a Bayesian change point model in PyMC.
- Explain priors, likelihood, and switch logic.

### Step 6: Modeling and Interpretation
- Run MCMC inference, check diagnostics, interpret output.
- Compare inferred change points with known events.

### Step 7: Communication
- Prepare results for stakeholders: narrative report, notebooks, and dashboard.

```markdown
## 3. Structured Event Data

In `data/oil_events.csv`, we list key geopolitical and economic events:

| Date       | Event             | Category  | Description                                                                         |
|------------|------------------|-----------|-------------------------------------------------------------------------------------|
| 1990‑08‑02 | Iraq Invades Kuwait | Conflict  | Started the Gulf War and caused a massive price spike.                             |
| 2008‑09‑15 | Lehman Brothers Collapse | Economic  | Global financial crisis led to a sharp drop in demand.                            |
| 2014‑11‑27 | OPEC No‑Cut Decision | Policy    | OPEC refused to cut production, leading to a multi‑year price slump.               |
| 2020‑03‑09 | COVID Price War   | Economic  | Saudi Arabia and Russia price war coincided with global lockdowns.                |
| 2022‑02‑24 | Ukraine Invasion  | Conflict  | Geopolitical tension caused Brent to surge past $100.                             |


```markdown
## 4. Assumptions and Limitations

### Assumptions
- Log returns provide a proxy for stationarity.
- Structural breaks correspond to regime changes in statistical distribution.

### Limitations
- Detecting a change point near an event does not confirm that the event *caused* the shift.
- Some events have effects that are gradual or delayed, not instantaneous.
- Other drivers (macroeconomic variables) are not explicitly modeled.

```markdown
## 5. Understanding the Model and Data

### Time Series Properties
- **Trend:** Long‑term movements reflect demand, supply, and macroeconomics.
- **Stationarity:** Raw prices are non‑stationary; log returns improve stationarity.
- **Volatility:** High volatility often associated with shocks (e.g., 2008, 2020).

### Change Point Models
Bayesian change point models let us infer where structural breaks occur by estimating the posterior distribution over change point location(s). A typical model has:
- Discrete uniform prior for switch point τ
- Regime means before and after τ
- Noise parameter (σ)
- Use of a switching function (e.g., `pm.math.switch`) to select regime means for each time index.

### Expected Outputs
- Estimated change points and credible intervals.
- Posterior distributions for regime means and noise.
- Model Diagnostics (R‑hat, trace plots).

Limitations:
- Identifying correlation in time does not prove causation.
- Unobserved factors may influence results.

```markdown
## 6. Communication Channels

#### Written Report
- PDF/Markdown document summarizing analysis steps and results.

#### Jupyter Notebooks
- Documented code with explanations (`notebooks/`).

#### Interactive Dashboard
- Flask backend + React frontend showing interactive plots.

#### Slides
- Presentation for stakeholders summarizing key findings.

```markdown
## 7. Summary

Task 1 sets the stage for all subsequent analysis. We should now proceed to building the Bayesian change point models (Task 2) and then the interactive dashboard (Task 3).
```

