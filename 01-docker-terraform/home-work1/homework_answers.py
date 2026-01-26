import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

print("\n" + "="*80)
print("ZOOMCAMP 2026 - MODULE 1 HOMEWORK ANSWERS")
print("="*80)

# Question 1
print("\n[Q1] pip version in python:3.13")
print("-"*80)
print("Answer: 25.3")
print("(Run: docker run --rm python:3.13 bash -c 'pip --version')")

# Question 2
print("\n[Q2] Docker Compose - hostname:port for pgadmin to connect to postgres")
print("-"*80)
print("Answer: db:5432")

# Question 3 - Count short trips
print("\n[Q3] Short trips (≤ 1 mile) in November 2025")
print("-"*80)
q3 = pd.read_sql("""
SELECT COUNT(*) as count
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2025-11-01' 
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1
""", engine)
q3_answer = q3.iloc[0]['count']
print(f"Answer: {q3_answer:,}")

# Question 4 - Longest trip day
print("\n[Q4] Pickup day with longest trip distance (excluding > 100 miles)")
print("-"*80)
q4 = pd.read_sql("""
SELECT DATE(lpep_pickup_datetime) as pickup_date, MAX(trip_distance) as max_distance
FROM green_taxi_data
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_distance DESC
LIMIT 1
""", engine)
q4_answer = q4.iloc[0]['pickup_date']
q4_distance = q4.iloc[0]['max_distance']
print(f"Answer: {q4_answer}")
print(f"(Max distance: {q4_distance} miles)")

# Question 5 - Largest pickup zone by total_amount (Nov 18)
print("\n[Q5] Largest pickup zone by total_amount on November 18, 2025")
print("-"*80)
q5 = pd.read_sql("""
SELECT z."Zone", SUM(g.total_amount) as total_amount
FROM green_taxi_data g
JOIN taxi_zones z ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_amount DESC
LIMIT 1
""", engine)
q5_answer = q5.iloc[0]['Zone']
q5_total = q5.iloc[0]['total_amount']
print(f"Answer: {q5_answer}")
print(f"(Total amount: ${q5_total:,.2f})")

# Question 6 - Largest tip from East Harlem North
print("\n[Q6] Largest tip from 'East Harlem North' to other zones (Nov 2025)")
print("-"*80)
q6 = pd.read_sql("""
SELECT z_do."Zone", MAX(g.tip_amount) as max_tip
FROM green_taxi_data g
JOIN taxi_zones z_pu ON g."PULocationID" = z_pu."LocationID"
JOIN taxi_zones z_do ON g."DOLocationID" = z_do."LocationID"
WHERE z_pu."Zone" = 'East Harlem North'
  AND g.lpep_pickup_datetime >= '2025-11-01'
  AND g.lpep_pickup_datetime < '2025-12-01'
GROUP BY z_do."Zone"
ORDER BY max_tip DESC
LIMIT 1
""", engine)
q6_answer = q6.iloc[0]['Zone']
q6_tip = q6.iloc[0]['max_tip']
print(f"Answer: {q6_answer}")
print(f"(Tip amount: ${q6_tip})")

# Question 7
print("\n[Q7] Terraform workflow (init → apply → destroy)")
print("-"*80)
print("Answer: terraform init, terraform apply -auto-approve, terraform destroy")

print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"Q1: 25.3")
print(f"Q2: db:5432")
print(f"Q3: {q3_answer:,}")
print(f"Q4: {q4_answer}")
print(f"Q5: {q5_answer}")
print(f"Q6: {q6_answer}")
print(f"Q7: terraform init, terraform apply -auto-approve, terraform destroy")
print("="*80)
print("\nSubmit at: https://courses.datatalks.club/de-zoomcamp-2026/homework/hw1\n")
