# 🏗️ Enterprise Retail Lakehouse

A production-inspired end-to-end Data Engineering project that implements a modern **Medallion Architecture (Bronze, Silver, Gold)** using PySpark and industry-standard engineering practices.

This project demonstrates how enterprise data platforms ingest, validate, transform, and serve analytical datasets while following software engineering best practices.

---

# 📌 Project Status

| Phase | Status |
|--------|--------|
| Day 1 – Project Setup | ✅ Completed |
| Day 2 – Common ETL Framework | ✅ Completed |
| Day 3 – Bronze Ingestion | 🚧 Next |
| Silver Layer | ⏳ Planned |
| Gold Layer | ⏳ Planned |
| Airflow Orchestration | ⏳ Planned |
| Dockerization | ⏳ Planned |
| CI/CD | ⏳ Planned |
| Dashboard | ⏳ Planned |

---

# 🚀 Project Objectives

- Build scalable ETL pipelines using **PySpark**
- Implement a **Bronze, Silver, Gold (Medallion)** architecture
- Develop reusable ETL components
- Apply data quality validation
- Orchestrate pipelines using Apache Airflow
- Store analytical datasets for reporting
- Follow enterprise software engineering practices
- Automate testing and deployment

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Data Processing | Apache Spark (PySpark) |
| Configuration | YAML |
| Version Control | Git & GitHub |
| Data Storage | Parquet |
| Future Database | PostgreSQL / DuckDB |
| Orchestration | Apache Airflow *(Planned)* |
| Containerization | Docker *(Planned)* |
| Data Quality | Great Expectations *(Planned)* |
| Transformation | dbt *(Planned)* |
| CI/CD | GitHub Actions *(Planned)* |

---

# 🏛️ Architecture

```text
                Raw CSV Files
                      │
                      ▼
          Common ETL Framework
     (Config, Logger, Spark, Validators)
                      │
                      ▼
              Bronze Layer
                      │
                      ▼
              Silver Layer
                      │
                      ▼
               Gold Layer
                      │
                      ▼
        Analytics & Dashboards
```

---

# 📁 Current Project Structure

```text
enterprise-retail-lakehouse/
│
├── configs/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── etl/
│   ├── common/
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── file_manager.py
│   │   ├── helpers.py
│   │   ├── logger.py
│   │   ├── spark.py
│   │   └── validators.py
│   │
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── tests/
│   └── test_framework.py
│
├── scripts/
│
└── README.md
```

---

# ✅ Completed Features

## Project Foundation

- Professional project structure
- Python virtual environment
- Git & GitHub repository
- Configuration management
- Modular package organization

---

## Common ETL Framework

### Configuration Framework

- YAML-based configuration
- Centralized configuration loader

### Logging Framework

- Reusable logging utility
- Consistent log formatting

### Spark Framework

- Centralized Spark Session creation
- Configurable application name

### File Management

- File existence validation
- CSV file discovery
- Directory creation helpers

### Validation Framework

- Input file validation
- Foundation for future data quality checks

### Utility Framework

- Shared helper functions
- Custom exception handling

---

# 🧪 Testing

Current test coverage includes:

- Configuration loading
- Logger initialization
- Spark session creation

Run tests:

```bash
python -m tests.test_framework
```

---

# 📊 Data Pipeline (Planned)

```text
CSV Files
     │
     ▼
Schema Validation
     │
     ▼
Bronze Layer
     │
     ▼
Data Cleansing
     │
     ▼
Silver Layer
     │
     ▼
Business Aggregations
     │
     ▼
Gold Layer
     │
     ▼
Dashboard
```

---

# 📅 Roadmap

## ✅ Completed

- Project initialization
- Development environment
- Common ETL framework

## 🚧 In Progress

- Bronze ingestion framework

## 🔜 Upcoming

- Schema validation
- Metadata-driven ingestion
- Silver transformations
- Star schema modeling
- Gold data marts
- Airflow DAGs
- Docker deployment
- GitHub Actions
- Dashboard

---

# 🎯 Learning Outcomes

This project demonstrates:

- Data Engineering
- PySpark
- ETL Design
- Medallion Architecture
- Modular Python Development
- Configuration-Driven Pipelines
- Data Validation
- Logging
- Git Workflow
- Software Engineering Best Practices

---

# 👨‍💻 Author

**Pavan Kalyan Boga**

Data Engineer | PySpark | SQL | AWS | ETL | Data Warehousing

---

# 📄 License

This project is licensed under the MIT License.