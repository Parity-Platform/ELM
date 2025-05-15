# Spark ETL Pipeline
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()
df = spark.read.csv("data.csv", header=True)
df_filtered = df.filter(df['energy_usage'] > 100)
df_transformed = df_filtered.withColumn("energy_category", (df_filtered['energy_usage'] / 1000).cast("integer"))
df_transformed.write.parquet("output.parquet")