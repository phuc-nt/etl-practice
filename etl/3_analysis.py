from pyspark.sql import SparkSession
from pyspark.sql.functions import col, floor, avg, count

def main():
    # Khởi tạo Spark session
    spark = SparkSession.builder \
        .appName("Comprehensive Employee Analysis") \
        .getOrCreate()

    # Đọc file Parquet
    df = spark.read.parquet("hdfs://127.0.0.1:9000/transformed_employees_married.parquet")

    # Phân chia nhóm tuổi (mỗi nhóm 10 năm)
    df = df.withColumn("age_group", floor(col("age") / 10) * 10)

    # Phân tích 1: Tính mức lương trung bình theo nhóm tuổi
    average_salary_by_age = df.groupBy("age_group").avg("salary").alias("average_salary")
    print("Average salary by age group:")
    average_salary_by_age.show()

    # Phân tích 2: Tính tỷ lệ nhân viên có con và không có con
    parent_stats = df.groupBy("has_children").agg(count("id").alias("count"))
    print("Employee count by parental status:")
    parent_stats.show()

    # Phân tích 3: Mức lương trung bình của nhân viên có con so với không có con
    average_salary_by_parental_status = df.groupBy("has_children").avg("salary")
    print("Average salary by parental status:")
    average_salary_by_parental_status.show()

    # Đóng Spark session
    spark.stop()

if __name__ == "__main__":
    main()