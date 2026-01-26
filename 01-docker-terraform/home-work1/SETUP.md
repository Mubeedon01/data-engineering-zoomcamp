# Module 1 Homework - Instructions

## ✅ Project Complete

Your homework project is now fresh and ready to start!

### 📂 Files Created:
- `docker-compose.yml` - Docker setup
- `load_data.py` - Data loading script
- `homework_answers.py` - Query runner
- `README.md` - Quick reference
- `.gitignore` - Ignore CSV/GZ files

---

## 🚀 Step-by-Step Instructions

### Step 1: Start Docker Containers
```bash
docker-compose up -d
```

### Step 2: Wait for PostgreSQL
```bash
sleep 20
```

### Step 3: Load Data
```bash
python load_data.py
```
This will:
- Download green taxi data (Oct 2019)
- Download taxi zone lookup
- Load both into PostgreSQL with proper data types

### Step 4: Get Your Answers
```bash
python homework_answers.py
```

---

## 📋 The 7 Questions

| # | Question | Answer Type |
|---|----------|------------|
| 1 | pip version | Multiple choice |
| 2 | Docker networking | Multiple choice |
| 3 | Trip segmentation | Multiple choice |
| 4 | Longest trip date | Multiple choice |
| 5 | Top 3 zones | Multiple choice |
| 6 | Largest tip zone | Multiple choice |
| 7 | Terraform workflow | Multiple choice |

---

## 📊 Access Data

**pgAdmin (Web UI)**
- URL: http://localhost:8080
- Email: admin@admin.com
- Password: admin

**PostgreSQL Direct**
- Host: localhost:5433
- DB: ny_taxi
- User: postgres
- Password: postgres

---

## 🔄 Reset Project (if needed)
```bash
docker-compose down -v
rm -f *.csv *.gz
```

---

## ✍️ Submit Your Work
https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1

Include:
- Your GitHub repo link
- All 7 answers from homework_answers.py

---

**Ready? Run the quick start above!** 🎯
