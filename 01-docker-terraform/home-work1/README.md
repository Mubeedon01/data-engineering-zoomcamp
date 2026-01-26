# Module 1 Homework - Data Engineering Zoomcamp 2026

## 🎯 Overview

**Dataset**: November 2025 green taxi trips (NEW for 2026!)
**Format**: Parquet (not CSV like previous years)
**Questions**: 7 total (Docker, SQL, Terraform)

---

## 📋 Step-by-Step Setup

### Step 1: Create Project Structure
```bash
cd /workspaces/data-engineering-zoomcamp/01-docker-terraform/home-work1
```

### Step 2: Start Docker & PostgreSQL
```bash
docker-compose up -d
sleep 20
```

### Step 3: Load Data
```bash
python load_data.py
```

### Step 4: Run Queries & Get Answers
```bash
python homework_answers.py
```

---

## 📊 The 7 Questions

### Q1: pip version in python:3.13
- Options: 25.3, 24.3.1, 24.2.1, 23.3.1

### Q2: Docker networking (hostname:port)
- Service name: `db`, Port: `5432`
- Answer: `db:5432`

### Q3: Short trips (≤ 1 mile) in Nov 2025
- Filter: `trip_distance <= 1`
- Count the trips

### Q4: Longest trip pickup day (Nov 2025)
- Exclude trips > 100 miles
- Find the day with longest distance

### Q5: Largest pickup zone by total_amount (Nov 18)
- Group by pickup zone
- Find max total_amount

### Q6: Largest tip from "East Harlem North"
- Filter pickup zone = "East Harlem North"
- Find dropoff zone with max tip

### Q7: Terraform workflow
- Answer: `terraform init, terraform apply -auto-approve, terraform destroy`

---

## 🔗 Submit Here
https://courses.datatalks.club/de-zoomcamp-2026/homework/hw1

---

## 📚 Resources
- Course: https://github.com/DataTalksClub/data-engineering-zoomcamp
- Cohort 2026: /cohorts/2026/
