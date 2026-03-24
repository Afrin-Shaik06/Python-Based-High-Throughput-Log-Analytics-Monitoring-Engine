# High Throughput Log Analytics & Monitoring System

## 📌 Overview

This project implements a **Distributed Log Analytics and Monitoring System** designed to process large volumes of logs efficiently.

The system demonstrates:

* Distributed log processing
* High-throughput log ingestion
* Real-time monitoring
* Anomaly detection
* Scalable data analytics pipelines

The implementation uses **distributed computing frameworks** and modern monitoring tools.

---

# 🏗 System Architecture

```text
Log Sources
      ↓
Log Ingestion Layer
      ↓
Distributed Processing (Dask / Ray)
      ↓
Log Parsing & Analytics
      ↓
Anomaly Detection
      ↓
Storage (CSV / Elasticsearch)
      ↓
Monitoring Dashboard (Streamlit / Kibana)
```

---

# 🧩 Components

### Log Sources

Servers or applications continuously generate logs.

### Ingestion Layer

Logs are ingested into the system for processing.

### Processing Engine

Logs are parsed, structured, and processed.

### Anomaly Detection

Detects unusual patterns such as spikes in error logs.

### Storage

Processed logs are stored for analytics.

### Monitoring

Dashboards provide visualization and system monitoring.

---

# 📂 Project Structure

```text
distributed-log-pipeline
│
├── milestone-1
│   ├── schemas
│   ├── diagrams
│   ├── docs
│   ├── environment
│   ├── tests
│   ├── dask_app.py
│   ├── ray_app.py
│   └── README.md
│
├── milestone-2
│   ├── data
│   ├── docs
│   ├── processed_logs
│   ├── schemas
│   ├── generate_logs.py
│   ├── ingestion.py
│   ├── processing.py
│   ├── anomaly_detection.py
│   ├── alerting.py
│   ├── dashboard.py
│   ├── realtime_ingestion.py
│   ├── send_logs_to_elasticsearch.py
│   └── README.md
│
└── README.md
```

---

# 🚀 Milestone-1

Milestone-1 focuses on **system design and distributed computation concepts**.

### Deliverables

* System Architecture Diagram
* Data Flow Diagram
* Log Schema Definition
* Anomaly Schema Definition
* Distributed processing with **Dask** and **Ray**

### Run Distributed Processing

Run Dask example:

```bash
python milestone-1/dask_app.py
```

Run Ray example:

```bash
python milestone-1/ray_app.py
```

Run environment tests:

```bash
pytest milestone-1/tests
```

---

# 🚀 Milestone-2

Milestone-2 implements the **complete log analytics pipeline**.

### Features

* Log generation
* Log ingestion pipeline
* Log parsing and processing
* Anomaly detection
* Alerting system
* Real-time log simulation
* Monitoring dashboard
* Elasticsearch integration
* Kibana visualization

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Afrin-Shaik06/Demo.git
cd Demo
```

Install dependencies:

```bash
pip install -r milestone-1/environment/requirements.txt
```

---

# ▶️ Main Execution Steps

### 1️⃣ Generate Sample Logs

```bash
python milestone-2/generate_logs.py
```

---

### 2️⃣ Run Log Processing Pipeline

```bash
python milestone-2/processing.py
```

This will parse logs and generate processed outputs.

---

### 3️⃣ Detect Log Anomalies

```bash
python milestone-2/anomaly_detection.py
```

This identifies abnormal log patterns.

---

### 4️⃣ Start Monitoring Dashboard

```bash
streamlit run milestone-2/dashboard.py
```

Dashboard runs at:

```
http://localhost:8501
```

---

### 5️⃣ Send Logs to Elasticsearch

```bash
python milestone-2/send_logs_to_elasticsearch.py
```

Logs will be available in Elasticsearch.

---

### 6️⃣ Visualize Logs in Kibana

Open:

```
http://localhost:5601
```

Create dashboards to monitor logs.

---

# 📊 Outputs

Processed logs are stored in:

```
milestone-2/processed_logs/output.csv
```

These include:

* log level
* service name
* message
* anomaly flags

---

# 📚 Technologies Used

* Python 3.12
* Dask
* Ray
* Pandas
* Streamlit
* Elasticsearch
* Kibana
* Pytest
* YAML

---

# 👩‍💻 Author

Shaik Mitaigiri Afrin
B.Tech Student
Infosys Springboard Project

High Throughput Log Analytics & Monitoring System
