import pandas as pd
import polars as pl
import time

# Download a sample dataset (NYC Taxi Trips small sample)

csv_file = "yellow_tripdata_2019-01.csv"

# ------------------ PANDAS ------------------
start = time.time()
df_pd = pd.read_csv(csv_file, nrows=100000)  # Load first 100k rows
# Example operation: filter and compute average fare
result_pd = df_pd[df_pd['passenger_count'] > 2]['total_amount'].mean()
end = time.time()
print("Pandas result:", result_pd)
print("Pandas execution time:", end - start, "seconds")

# ------------------ POLARS ------------------
start = time.time()
df_pl = pl.read_csv(csv_file, n_rows=100000)
# Example operation: filter and compute average fare
result_pl = df_pl.filter(pl.col('passenger_count') > 2).select(pl.col('total_amount').mean())
end = time.time()
print("Polars result:", result_pl)
print("Polars execution time:", end - start, "seconds")

# Create passenger group
df_pl = df_pl.with_columns(
    pl.when(pl.col("passenger_count") >= 4).then(4)
    .otherwise(pl.col("passenger_count")).alias("passenger_group")
)

# 1. Revenue by passenger group
revenue_analysis = df_pl.group_by("passenger_group").agg(
    pl.col("total_amount").sum().alias("total_revenue")
    ).sort("passenger_group")

# 2. Tip amount (average and max) by passenger group
tip_analysis = df_pl.group_by("passenger_group").agg([
    pl.col("tip_amount").mean().alias("avg_tip"),
    pl.col("tip_amount").max().alias("max_tip")
]).sort("passenger_group")

# 3. Trip count by passenger group
trip_analysis = df_pl.group_by("passenger_group").agg(
    pl.count().alias("trip_count")
).sort("passenger_group")

print("Revenue by passenger group:")
print(revenue_analysis)
print("\nTip amount by passenger group:")
print(tip_analysis)
print("\nTrip count by passenger group:")
print(trip_analysis)
