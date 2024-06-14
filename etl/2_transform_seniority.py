from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, year, datediff

def main():
    # Tạo Spark session với Hive support và cấu hình HDFS
    spark = SparkSession.builder \
        .appName("Transform Data with Seniority and Hive") \
        .config("spark.sql.warehouse.dir", "hdfs://127.0.0.1:9000/hive/warehouse") \
        .config("spark.hadoop.javax.jdo.option.ConnectionURL", "jdbc:derby:;databaseName=metastore_db;create=true") \
        .config("spark.sql.catalogImplementation", "hive") \
        .config("spark.hadoop.hive.metastore.uris", "thrift://localhost:9083") \
        .enableHiveSupport() \
        .getOrCreate()

    # Đọc dữ liệu từ HDFS
    df = spark.read.parquet("hdfs://127.0.0.1:9000/employees_recent.parquet")

    # Biến đổi dữ liệu
    # Thêm cột "age" cho tuổi dựa trên năm sinh
    transformed_df = df.withColumn("age", year(current_date()) - col("birth_year"))

    # Thêm cột "seniority" cho số thâm niên dựa trên hire_date
    transformed_df = transformed_df.withColumn("seniority", datediff(current_date(), col("hire_date")) / 365)

    # Loại bỏ các cột không cần thiết
    transformed_df = transformed_df.drop("name", "married", "has_children")

    # Hiển thị dữ liệu đã biến đổi để kiểm tra
    transformed_df.show()

    # Xóa bảng Hive nếu tồn tại và tạo lại
    spark.sql("DROP TABLE IF EXISTS hive_employees_seniority")

    # Lưu dữ liệu đã biến đổi vào HDFS dưới dạng ORC
    transformed_df.write.mode("overwrite").format("orc").save("hdfs://127.0.0.1:9000/hive/warehouse/hive_employees_seniority")

    # Tạo bảng Hive tham chiếu đến dữ liệu đã lưu trong HDFS
    spark.sql("""
    CREATE EXTERNAL TABLE IF NOT EXISTS hive_employees_seniority (
        id INT,
        position STRING,
        salary DOUBLE,
        gender STRING,
        birth_year INT,
        hire_date DATE,
        age INT,
        seniority DOUBLE
    )
    STORED AS ORC
    LOCATION 'hdfs://127.0.0.1:9000/hive/warehouse/hive_employees_seniority'
    """)

    # Đóng Spark session
    spark.stop()

if __name__ == "__main__":
    main()