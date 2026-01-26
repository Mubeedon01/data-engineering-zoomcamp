import pandas as pd
from sqlalchemy import create_engine
import subprocess
import os

print("\n" + "="*70)
print("MODULE 1 2026 - DATA LOADING SCRIPT")
print("(November 2025 Green Taxi Data)")
print("="*70)

# Database connection
engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

print("\n[STEP 1/3] DOWNLOADING DATA...")
print("-"*70)

# Download parquet data
print("\n[1a] Downloading green taxi data (Nov 2025)...")
parquet_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
parquet_file = 'green_tripdata_2025-11.parquet'

subprocess.run(['wget', '-q', parquet_url], check=True)
print(f"✓ Downloaded: {parquet_file}")

# Download zones
print("\n[1b] Downloading taxi zones...")
zones_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
zones_file = 'taxi_zone_lookup.csv'

subprocess.run(['wget', '-q', zones_url], check=True)
print(f"✓ Downloaded: {zones_file}")

print("\n[STEP 2/3] LOADING DATA INTO DATABASE...")
print("-"*70)

# Load parquet data
print("\n[2a] Loading green taxi data (Parquet format)...")
df_green = pd.read_parquet(parquet_file)

# Convert datetime columns
df_green['lpep_pickup_datetime'] = pd.to_datetime(df_green['lpep_pickup_datetime'])
df_green['lpep_dropoff_datetime'] = pd.to_datetime(df_green['lpep_dropoff_datetime'])

print(f"  ✓ Records: {len(df_green):,}")
print(f"  ✓ Columns: {len(df_green.columns)}")
print(f"  ✓ Date range: {df_green['lpep_pickup_datetime'].min()} to {df_green['lpep_pickup_datetime'].max()}")

df_green.to_sql('green_taxi_data', con=engine, if_exists='replace', index=False)
print("  ✓ Loaded to database")

# Load zones
print("\n[2b] Loading taxi zones...")
df_zones = pd.read_csv(zones_file)
print(f"  ✓ Zones: {len(df_zones)}")

df_zones.to_sql('taxi_zones', con=engine, if_exists='replace', index=False)
print("  ✓ Loaded to database")

print("\n[STEP 3/3] VERIFYING DATA...")
print("-"*70)

# Verify
count_green = pd.read_sql("SELECT COUNT(*) as count FROM green_taxi_data;", engine)
count_zones = pd.read_sql("SELECT COUNT(*) as count FROM taxi_zones;", engine)

print(f"\n✓ green_taxi_data: {count_green.iloc[0,0]:,} records")
print(f"✓ taxi_zones: {count_zones.iloc[0,0]} zones")

print("\n" + "="*70)
print("✅ DATA LOADED SUCCESSFULLY!")
print("="*70)
print("\nNext: Run 'python homework_answers.py' to get your answers!\n")
