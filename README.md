# Enterprise Retail Lakehouse

> 🚀 A production-inspired Data Engineering portfolio project that demonstrates how modern Lakehouse architectures are designed and built using open-source technologies.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![MinIO](https://img.shields.io/badge/Storage-MinIO-red)
![Status](https://img.shields.io/badge/Status-Sprint%201%20Complete-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Table of Contents

- Introduction
- Objectives
- Technology Stack
- Architecture
- Project Structure
- Current Features
- Sprint Progress
- Dataset
- Getting Started
- Future Roadmap
- Learning Goals
- License

---

# Introduction

Enterprise Retail Lakehouse is a personal portfolio project built to simulate how enterprise-scale data engineering platforms are designed and implemented.

Instead of creating a simple ETL pipeline, the goal is to build a complete modern Lakehouse architecture from scratch using industry-standard tools and software engineering best practices.

The project is developed incrementally through multiple sprints, where each sprint introduces new capabilities while maintaining clean architecture, modular code, testing, and documentation.

Current project status:

> **Sprint 1 Completed ✅**

---

# Objectives

This project aims to demonstrate practical knowledge of:

- Modern Data Lakehouse Architecture
- Batch Data Processing
- Object Storage
- Distributed Data Processing
- Metadata Management
- Data Quality Validation
- Workflow Orchestration
- Analytics Engineering
- Software Engineering Best Practices
- Reusable ETL Framework Design

By the end of the project, the platform will support:

- Raw data ingestion
- Bronze, Silver and Gold data layers
- Apache Iceberg tables
- Trino SQL analytics
- Airflow orchestration
- Great Expectations data validation
- dbt transformations
- Analytics-ready datasets

---

# Technology Stack

| Category | Technology |
|------------|-------------|
| Programming Language | Python 3.12 |
| Object Storage | MinIO |
| Containerization | Docker |
| Configuration | YAML |
| Data Source | Kaggle |
| Version Control | Git & GitHub |
| Processing Engine | Apache Spark *(Upcoming)* |
| Lakehouse Format | Apache Iceberg *(Upcoming)* |
| Query Engine | Trino *(Upcoming)* |
| Workflow Orchestration | Apache Airflow *(Upcoming)* |
| Data Quality | Great Expectations *(Upcoming)* |
| Data Transformation | dbt *(Upcoming)* |

---

# Architecture

Current Architecture (Sprint 1)

```
                  Kaggle Dataset
                         │
                         ▼
                Download Pipeline
                         │
                         ▼
        data/raw/olist/<timestamp>/
                         │
                         ▼
                Storage Manager
                         │
                         ▼
                      MinIO
                         │
                         ▼
     raw/olist/<timestamp>/
```

Target Architecture

```
                   Kaggle
                      │
                      ▼
                Raw Data (MinIO)
                      │
                      ▼
             Apache Spark Cluster
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
    Bronze Layer              Metadata
        │
        ▼
    Silver Layer
        │
        ▼
     Gold Layer
        │
        ▼
   Apache Iceberg
        │
        ▼
       Trino
        │
        ▼
 Analytics / Dashboard
```

---

# Project Structure

```
enterprise-retail-lakehouse/

├── airflow/
├── architecture/
├── configs/
│   ├── airflow.yaml
│   ├── config.yaml
│   ├── iceberg.yaml
│   ├── logging.yaml
│   ├── minio.yaml
│   ├── quality.yaml
│   ├── spark.yaml
│   └── trino.yaml
│
├── dashboard/
├── data/
│   ├── raw/
│   └── temp/
│
├── datasets/
├── dbt/
├── docker/
├── docs/
│
├── etl/
│   ├── bronze/
│   ├── common/
│   ├── gold/
│   ├── ingestion/
│   ├── metadata/
│   ├── monitoring/
│   ├── quality/
│   ├── silver/
│   └── storage/
│
├── notebooks/
├── scripts/
├── sql/
├── tests/
├── utils/
│
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# Current Features (Sprint 1)

## Project Foundation

- Professional project structure
- Modular architecture
- Dockerized environment
- Git version control

---

## Configuration Framework

Implemented a centralized configuration framework that automatically loads and merges multiple YAML configuration files.

Configuration modules include:

- Project
- Spark
- MinIO
- Logging
- Airflow
- Iceberg
- Trino
- Data Quality

Example:

```python
config = Config(CONFIG_PATH)

config.get("spark", "app_name")
config.get("minio", "endpoint")
config.get("dataset", "name")
```

---

## Object Storage Layer

Implemented a reusable storage abstraction using MinIO.

Components:

- MinIOClient
- StorageManager

Supported operations:

- Upload files
- Download files
- List objects
- Delete objects
- Validate buckets
- Check object existence

---

## Automated Dataset Ingestion

Implemented an automated ingestion pipeline for the Olist Brazilian E-commerce dataset.

Features:

- Automatic dataset download
- Automatic extraction
- Timestamp-based ingestion folders
- Immutable raw snapshots
- Dataset-aware directory structure

Example:

```
data/raw/

└── olist/
    ├── 2026-07-29_16-30-33/
    ├── 2026-07-30_10-15-44/
    └── ...
```

---

## MinIO Upload Pipeline

Uploads the latest ingestion into MinIO while preserving the dataset hierarchy.

```
enterprise-retail-lakehouse/

raw/

└── olist/
    ├── 2026-07-29_16-30-33/
    ├── 2026-07-30_10-15-44/
    └── ...
```

Each ingestion represents an immutable snapshot, making future auditing and reproducibility possible.

---

# Sprint Progress

| Sprint | Status |
|----------|--------|
| Sprint 1 – Project Foundation | ✅ Completed |
| Sprint 2 – Apache Spark Integration | 🚧 In Progress |
| Sprint 3 – Bronze Layer | ⏳ Planned |
| Sprint 4 – Apache Iceberg | ⏳ Planned |
| Sprint 5 – Silver Layer | ⏳ Planned |
| Sprint 6 – Gold Layer | ⏳ Planned |
| Sprint 7 – Trino Analytics | ⏳ Planned |
| Sprint 8 – Airflow Orchestration | ⏳ Planned |
| Sprint 9 – Data Quality | ⏳ Planned |
| Sprint 10 – dbt & Dashboard | ⏳ Planned |

---

# Dataset

This project uses the publicly available:

**Brazilian E-Commerce Public Dataset by Olist**

The dataset contains information about:

- Customers
- Orders
- Products
- Sellers
- Payments
- Reviews
- Geolocation

making it ideal for demonstrating end-to-end data engineering workflows.

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/<your-username>/enterprise-retail-lakehouse.git

cd enterprise-retail-lakehouse
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start MinIO

```bash
docker compose up -d
```

---

## Download Dataset

```bash
python -m scripts.download_dataset
```

---

## Upload Dataset

```bash
python -m scripts.upload_dataset
```

---

# Future Roadmap

Upcoming milestones include:

- Dockerized Apache Spark Cluster
- Spark Session Factory
- Spark ↔ MinIO Integration
- Bronze Layer
- Metadata Framework
- Apache Iceberg
- Silver Layer
- Gold Layer
- Trino SQL Engine
- Airflow DAGs
- Great Expectations
- dbt Models
- Dashboard
- CI/CD Pipeline

---

# Learning Goals

This project is designed to strengthen hands-on experience with:

- Data Engineering
- Data Lakehouse Architecture
- Distributed Data Processing
- Object Storage
- ETL Design Patterns
- Data Modeling
- Software Engineering
- Containerization
- Testing
- Infrastructure as Code

---

# License

This project is released under the MIT License and is intended for educational and portfolio purposes.