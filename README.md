# 💻 Chromebook Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mr-adonis-jimenez-chromebook-sales-forecast-dashboard.streamlit.app)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/mr-adonis-jimenez/chromebook-sales-forecast-dashboard)

An interactive **Chromebook Dashboard** developed using Python and Streamlit. The app forecasts future sales for multiple products using the **Prophet** model, supports **auto-refresh retraining**, and integrates seamlessly with **Google Drive (local sync)**, **OneDrive**, **Dropbox**, **Amazon Drive**, **Mega**, **Nextcloud**, **Seafile**, or **Syncthing**

---

## 🧠 Overview

This project demonstrates how to transform a Chromebook into a full data science workstation using Linux (Beta).  
It reads real or sample sales data from a synced Google Drive folder, visualizes historical performance, and generates sales forecasts for selected products — all offline, directly from ChromeOS.

---

## 🌟 Features

✅ **Multi-Product Forecasting** — switch between product lines with dynamic Prophet models  
✅ **Auto-Retrain Every 7 Days** — background scheduler keeps forecasts fresh  
✅ **Offline Google Drive Integration** — reads data locally from Drive sync folder  
✅ **Interactive Visuals** — Plotly charts for sales and forecasts  
✅ **Export Results** — one-click CSV download of predictions  
✅ **100% Chromebook Compatible** — runs inside Linux (Beta) environment  

---

## 🧱 Tech Stack

| Tool | Purpose |
|------|----------|
| **Python 3** | Core programming language |
| **Streamlit** | Web dashboard framework |
| **Prophet** | Forecasting and time series modeling |
| **Plotly** | Interactive data visualization |
| **pandas** | Data wrangling and manipulation |
| **APScheduler** | Automatic retraining scheduler |

---

## 🚀 Live Demo

🔗 **[Launch App on Streamlit Cloud](https://mr-adonis-jimenez-chromebook-sales-forecast-dashboard.streamlit.app)**

If the live demo doesn’t load, clone and run it locally (instructions below).

---

## ⚙️ Run Locally on Chromebook

**Enable Linux (Beta)** on ChromeOS
   
   → Settings → Developers → Turn on Linux.

   # 🧠📊 Fintech / AI Risk Intelligence Platform

---

## 🎯 CORE MISSION

**Purpose:**  
Continuously **measure, predict, and price risk in real time** so capital can be deployed (or pulled back) intelligently.

**How it works:**

- 🔄 **Fuse** streaming market data and internal portfolio data  
- 🧮 **Run** statistical and machine learning models to project downside and upside  
- 🎛️ **Translate** insights into specific actions:
  - Rebalance
  - Hedge
  - Throttle exposure
  - Alert compliance
  - And more...

> This is not just *“dashboarding.”*  
> It is an **automated risk co-pilot** for modern finance. 🤖✈️

---

## 👥 PRIMARY USERS

- 📈 **Portfolio / Trading**  
  > “Can I increase exposure here without blowing VaR?”

- 💧 **Treasury / Liquidity**  
  > “Will we have enough cash under stress?”

- 🛡️ **Compliance / Ops**  
  > “Are we drifting into unacceptable counterparty or credit concentration?”

- 🧩 **Executives / Investors**  
  > “How fragile are we if tomorrow looks like 2008 again?”

---

## 🏗️ DATA ARCHITECTURE

Think of data as **three rivers** 🌊 flowing into **one lake** 💧, then feeding the **model engines** 🚂.

### 📥 Data Sources (Ingestion Layer)

#### 📊 Market Data

- Prices, yields, spreads, implied volatility, order book depth  
- Asset classes:
  - 🏛️ Equities
  - 🪙 Crypto
  - 💱 FX
  - 📉 Rates
  - 🛢️ Commodities
  - 💳 Credit instruments  
- Market microstructure signals:
  - Slippage  
  - Liquidity  
  - Volume spikes  

#### 💼 Portfolio & Exposure Data

- Current positions, sizes, leverage, margin usage  
- Collateral posted / received  
- Counterparties and credit limits  
- P&L history (profit and loss over time) 📈📉  

#### 🌎 Macroeconomic / Structural Data

- Rates decisions, inflation prints, GDP trends  
- Sector fundamentals, earnings, balance sheet quality  
- Regime indicators:
  - Risk-on / risk-off  
  - Liquidity stress  
  - Volatility regime shifts  

#### 🧩 Optional Extensions

- 🧍 **Client Behavioral Data** (brokerage / robo-advisor)
  - Flows in/out  
  - Redemption risk  

- ⛓️ **On-chain Data** (if you touch crypto)
  - Wallet exposure clustering  
  - Bridge risk  
  - Smart contract exploit flags  

---

### ⚙️ Ingestion Mechanics

- ⚡ **Streaming Pipelines**  
  For tick/second-level data (Kafka, Redpanda-style event bus)

- 📦 **Batch ETL (Extract–Transform–Load)**  
  For slower data (macroeconomic releases, earnings)

- 🧹 **Enrichment**  
  Unify tickers / instruments / counterparties so models see **one clean vocabulary**.

---

### 🗄️ Storage Layer

We usually split storage by purpose:

#### 🔥 Hot Store (Real-Time, Low Latency)

- Time-series DB for:
  - Prices  
  - Realized P&L  
  - Realized volatility  
- Position snapshot store with near-real-time holdings

#### 🌤️ Warm Store (Model Training / Reporting)

- 🧬 **Feature Store**  
  Engineered model inputs:
  - 30-day rolling volatility  
  - Correlations  
  - Liquidity scores  

- 📚 **Scenario Library**  
  Historical crisis windows:
  - “COVID crash sequence”  
  - “Rates shock sequence”  
  - Other stress regimes  

#### 🧊 Cold Store (Audit / Regulatory / Forensics)

- Immutable logs of executed decisions, alerts, limit breaches  
- Model versions and parameters used at each timestamp  

> This is what keeps **legal** happy later. ⚖️

---

### 🔐 Security Basics

- 🔑 Role-based access control  
- 🧷 Encryption in transit and at rest  
- 📜 Audit trails on all manual overrides  

> Data architecture here is not cute *“data lake”* marketing.  
> It is **memory + reflex + evidence.**

---

## 🧮 ANALYTICS & MODELING LAYER (THE MATH BRAIN 🧠)

This is where we turn **raw feeds** into **risk forecasts**.  
We use a hybrid of **classical finance math + machine learning**.

---

### 📉 Market Risk Models (Price Moves)

**Goal:**  
> “How bad can this get and how likely is it?” 😬

#### 📌 Value-at-Risk (VaR)

- **Historical VaR**  
  - Replay last *N* days of returns to estimate worst expected daily loss  
  - Confidence level: α (e.g. **99%**)

- **Monte Carlo VaR**  
  - Simulate thousands of future price paths  
  - Use estimated **vol** (volatility) and **corr** (correlation) structure  

#### 📉 Expected Shortfall (ES) / Conditional VaR

Not just “what’s the line?” but:

> “What happens after you’ve already fallen off the cliff?” 🧗‍♂️💥

- ES looks at the **average loss in the worst tail**  
- Regulators increasingly prefer ES because it’s harder to game than VaR  

#### 🌪️ Scenario / Stress Testing

- Rate spike **+** equity drawdown **+** liquidity freeze at the same time  
- Replay known disasters (global financial crisis)  
- Generate disciplined hypotheticals, e.g.:
  - “BTC -40% overnight”  
  - “ETH gas chaos”  
  - “Stablecoin depeg”  
  - “Prime broker haircut”

---

### 📡 Regime Detection Model

- ML classifier (gradient boosted trees / transformer-based time series)  
- Labels current regime as:
  - `normal`  
  - `elevated stress`  
  - `crisis`  

Regime feeds into scaling rules, e.g.:

> “If regime = crisis, cut gross leverage ceiling from 5x to 2x.”

---

### 🧾 Credit / Counterparty Risk Models

**Goal:**  
> “Will someone we depend on fail to pay us?” 🧨

#### 🎯 Probability of Default (PD) Modeling

- Logistic regression or gradient boosted trees  
- Features:
  - Balance sheet health  
  - Market-implied spreads  
  - Rating trajectory  
- For crypto counterparties:
  - Wallet health  
  - Protocol exposure  
  - Dependency map  

#### 📉 Loss Given Default (LGD)

> How much do we lose if they blow up?

- Incorporates:
  - Collateral  
  - Seniority  
  - Liquidation recovery under stress  

#### 💣 Exposure at Default (EAD)

> How much are we on the hook for at the exact worst moment?

---

📌 **Expected Credit Loss**

> **ECL = PD × LGD × EAD**

The platform auto-calculates this at both **counterparty** and **portfolio** level.

---

### 💧 Liquidity Risk Modeling

**Goal:**  
> “Can we exit without lighting ourselves on fire?” 🔥

#### 📊 Market Depth Modeling

- **Slippage curves:**  
  How much price moves if we try to unload X notional in Y minutes  
- **Order book thinning under stress**  
  > Liquidity vanishes exactly when you need it — finance is rude like that.

#### 💰 Liquidity Coverage Forecasting

- Projected cash runway under:
  - Stressed outflows  
  - Margin calls  
- Simulate collateral recalls if primes tighten terms **simultaneously**

---

### 📑 P&L Attribution and Anomaly Detection

**Goal:**  
> “Is what we’re earning consistent with what we think we’re doing?” 🕵️

#### 🧩 P&L Explainability Engine

Breaks total P&L into components:

- Market move  
- FX translation  
- Carry / yield  
- Fees  
- Slippage  

If **unexplained P&L** exceeds a threshold → **trigger alert**.  
> This catches “hidden positions” and fat-finger risk.

#### 🚨 Anomaly / Drift Detection

Use **unsupervised methods** (clustering, isolation forests) to flag behavior that doesn’t match historical patterns:

- Sudden leverage spike  
- Uncharacteristic concentration in one issuer  
- Structural drift in risk profile  

---

### 🔮 Forecasting Models (Forward-Looking Intelligence)

**Goal:**  
> “What’s likely in the next hour / day / week?” ⏱️

#### ⚡ Short-Horizon Volatility Forecasting

- **GARCH-type models**  
  - Classic econometrics for volatility clustering  
- **LSTM / attention-based time series**  
  - For intraday realized vol  

#### 📉 Price Shock Probability Surfaces

- Predict probability of **X% drawdown** in the next **T hours** for each asset  
- Feed these probabilities back into VaR  
- Do **not** assume normal (Gaussian) returns — markets are jumpy and rude 🐘📉  

---

### 🔍 Explainability Layer

This matters for **regulators and executives**. 👩‍⚖️👔

- Every prediction (like **PD = 3.2%**) needs a **why**  
- Use **SHAP-style feature attribution** to show top drivers behind each risk score  

Example output:

> “Counterparty B risk ↑ mainly due to declining collateral quality and leverage > 4.5x vs prior 2.1x.”

This turns **black-box AI** into **defendable, auditable logic**. ✅

---

## 📊 RISK METRICS & OUTPUTS

You win not by having fancy models, but by surfacing the **right numbers at the right moment** so a human can act without guessing.

The platform surfaces, at minimum:

---

### 📉 Portfolio VaR

> **“99% one-day VaR = $8.4M.”**  

Translation:  
There is a **1% chance** that tomorrow’s loss is worse than **$8.4M**.  
Not a promise. A **warning**. ⚠️

### 🧨 Expected Shortfall

> **“Tail loss expectation beyond VaR = $13.2M.”**

---

### 🏦 Leverage and Margin Utilization

- Gross exposure (sum of absolute long + short)  
- Net exposure (long minus short)  
- % of available margin used  

---

### 🎯 Concentration Risk

- Top 5 positions as **% of portfolio risk**, not just % of capital  
- Counterparty exposure vs approved limit  

---

### 💧 Liquidity Health

> “Time to exit 80% of position in Asset X without >2% slippage:  
> ~19 minutes under normal conditions, ~3 hours under stress replay.”

---

### 🌪️ Stress Test Outcomes

> “In **Rates Shock Scenario** (parallel +200 bps move), projected 5-day P&L = **- $4.7M**, liquidity coverage ratio falls to **1.08x** (yellow threshold is **1.2x**).”

---

### 🚨 Early Warnings / Breaches

- **Limit Breach Flags**  
  > “Derivatives desk exceeded BTC single-asset VaR limit by 12%.”

- **Regime Shift Flags**  
  > “Volatility regime changed to *Crisis* at 14:32 UTC.”

- **Model Drift Flags**  
  > “PD model confidence dropped; retraining required.”

> Each of those outputs has an **owner**.  
> An **alert without an owner is theater. 🎭**

---

## 🧭 DECISION / ACTION LAYER

Now we get to the point: **what does the system actually do** with all this?  
Otherwise it’s just pretty charts. 📊✨

We define:

- 🤖 **Automated responses**  
- 🧑‍💼 **Human-in-the-loop responses**

---

### 🤖 Automated Responses

Predefined policies that execute **instantly** when conditions hit.

Examples:

- **Auto-deleveraging**  
  > If portfolio VaR > approved `VaR_limit`, cut gross exposure by X%, prioritizing least liquid / highest tail risk first.

- **Limit Enforcement**  
  > Block new trades that would increase exposure to a counterparty already above risk tolerance.

- **Margin Defense**  
  > Automatically raise internal margin requirements when liquidity regime = `stressed`.

> These are like **circuit breakers**.  
> They prevent “I’ll fix it after lunch” disasters. 🍽️💥

---

### 🧑‍💼 Human-in-the-Loop Responses

These are **escalations**, not auto-actions.

Examples:

- “Counterparty PD crossed red line (PD > 8%). **CRO review required before 16:00.**”  
- “Stablecoin desk stress loss > threshold in **Depeg Scenario**. Treasury needs to confirm backstop liquidity source.”

The platform also needs **workflow logging**:

- Who saw the alert 👀  
- Who approved / blocked the action ✅❌  
- Timestamp ⏰  
- Rationale 📝  

> That audit trail is the lifeline when regulators (or investors, or litigators) ask:  
> **“Why did you keep that exposure?”**

---

## 🏛️ GOVERNANCE, AUDIT, AND CONTROLS

Without this layer the platform can’t run inside a **regulated business**.  
This is where **grown-up supervision** lives. 🧓📋

---

### 🧬 Model Governance

- Every model (VaR engine, PD model, anomaly detector, etc.) is **versioned**  
- Every prediction is tagged with **which version** produced it  
- Retraining, feature changes, or hyperparameter changes are **logged and reviewable**

> This prevents “the AI told us it was safe” defenses.  
> You can prove what logic was live at **10:43 on October 30, 2025.**

---

### 📏 Policy / Limit Framework

- **Firm-wide:**
  - Total allowed VaR  
  - Total leverage ceiling  
  - Global liquidity minimums  

- **Desk-level:**
  - BTC exposure  
  - Tech high-beta equities exposure  
  - Unsecured lending per counterparty  

- **Per-instrument:**
  - Stablecoin concentration  
  - Specific basket limits (for regulatory optics)  

The platform **encodes** these limits and **enforces** them in real time.  
> The rules are not tribal knowledge in someone’s head. 🧠🚫

---

### 🕵️ Compliance / Surveillance Hooks

- **Trade Surveillance:**  
  Sudden behavior outside mandate (rogue trading risk)

- **Suitability:**  
  Are clients in products aligned with their stated risk tolerance?

- **AML / Fraud Hooks:**  
  If applicable, attach patterns, alerts, and workflows.

---

### 📈 Reporting Layer

This is what goes to:

- 🧑‍💼 **Executives:**  
  Summary dashboard + scenario loss ladders  

- 🧑‍⚖️ **Regulators / Auditors:**  
  Evidence of **control**, not just pretty PDFs  

- 💼 **Investors / LPs:**  
  Risk-adjusted performance narrative:  
  > “We made X with max drawdown Y under Z macro regime.”

> Regulators care less about “we are smart” 🤓  
> and more about **“we are disciplined and predictable.”**  
> This layer gives you that story. 📚✅

---

## 💡 VALUE PROPOSITION

This platform:

- 📡 Ingests **live market, portfolio, counterparty, and macro data**  
- 🧮 Estimates **downside risk, tail loss, liquidity stress, and credit fragility** using:
  - Statistical models  
  - Machine learning models  
- 🎛️ Turns those analytics into:
  - Real-time **limits**  
  - Automated **hedging / position controls**  
  - Structured **escalation workflows**  

It produces **audit-ready evidence** of every decision, making it usable not just for:

- Trading **alpha** 📈  
but also for:
- Risk **governance** 🏛️  
- Treasury **stability** 💰  
- Compliance **obligations** 🛡️  
- Investor **reporting** 📑  

---

*Built for a world where markets are chaotic, capital is impatient, and regulators are watching. 👀📉📜*


