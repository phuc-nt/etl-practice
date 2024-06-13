from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, year

def main():
    # Tạo Spark session
    spark = SparkSession.builder \
        .appName("Transform Data") \
        .getOrCreate()

    # Đọc dữ liệu từ HDFS
    df = spark.read.parquet("hdfs://127.0.0.1:9000/employees_recent.parquet")

    # Biến đổi dữ liệu
    # Thêm cột "age" cho tuổi dựa trên năm sinh
    transformed_df = df.withColumn("age", year(current_date()) - col("birth_year"))

    # Lọc những nhân viên đã kết hôn
    married_df = transformed_df.filter(col("married") == True)

    # Hiển thị dữ liệu đã biến đổi để kiểm tra
    married_df.show()

    # Ghi dữ liệu đã biến đổi vào HDFS
    married_df.write.mode("overwrite").parquet("hdfs://127.0.0.1:9000/transformed_employees_married.parquet")

    # Đóng Spark session
    spark.stop()

if __name__ == "__main__":
    main()