import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import math
import time

# Load a sample open dataset (NYC Taxi Trips)
csv = "yellow_tripdata_2019-01.csv"
df = pd.read_csv(csv, nrows=100000)  # Load first 100k rows for demo

# Simulate an expensive row-wise operation
def expensive_operation(row):
    # Example: complex computation per row
    return math.sqrt(row['trip_distance'] ** 2 + row['total_amount'] ** 2)

# ------------------ Single-threaded ------------------
start = time.time()
results_single = df.apply(expensive_operation, axis=1)
end = time.time()
print("Single-threaded execution time:", end - start, "seconds")

# ------------------ Multithreaded using ThreadPoolExecutor ------------------
# Split DataFrame into chunks
n_chunks = 5
chunks = [df.iloc[i:i + len(df)//n_chunks] for i in range(0, len(df), len(df)//n_chunks)]

def process_chunk(chunk):
    return chunk.apply(expensive_operation, axis=1)

start = time.time()
with ThreadPoolExecutor(max_workers=n_chunks) as executor:
    results_chunks = list(executor.map(process_chunk, chunks))

# Combine results
results_parallel = pd.concat(results_chunks)
end = time.time()
print("Multithreaded execution time:", end - start, "seconds")


# Create passenger group
df["passenger_group"] = df["passenger_count"].apply(lambda x: min(x,4))

# 1. Revenue by passenger group
revenue_analysis = df.groupby("passenger_group")["total_amount"].sum().reset_index()
revenue_analysis.columns = ["passenger_group", "total_revenue"]

# 2. Tip amount (average and max) by passenger group
tip_analysis = df.groupby("passenger_group").agg({"tip_amount": ["mean", "max"]}).reset_index()
tip_analysis.columns = ["passenger_group", "avg_tip", "max_tip"]

# 3. Trip count by passenger group
trip_analysis = df.groupby("passenger_group").size().reset_index()
trip_analysis.columns = ["passenger_group", "trip_count"] 

print("Revenue by passenger group:")
print(revenue_analysis)
print("\nTip amount by passenger group:")
print(tip_analysis)
print("\nTrip count by passenger group:")
print(trip_analysis)
