from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

# Initialize Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read data from Glue Catalog
df = spark.read.csv(
    "s3://telecom-data-glue-1237/customer_subscription.csv",
    header=True,
    inferSchema=True
)

# Simple Transformation
df_clean = df.dropDuplicates()

# Write transformed data
df_clean.write.mode("overwrite").parquet(
    "s3://telecom-data-glue-1237/output/"
)

print("ETL Job Completed Successfully")






