from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, year

def main():
    # Tạo Spark session với Hive support và cấu hình HDFS
    spark = SparkSession.builder \
        .appName("Transform Data with Hive") \
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

    # Lọc những nhân viên đã kết hôn
    married_df = transformed_df.filter(col("married") == True)

    # Hiển thị dữ liệu đã biến đổi để kiểm tra
    married_df.show()

    # Xóa bảng Hive nếu tồn tại và tạo lại
    spark.sql("DROP TABLE IF EXISTS hive_employees_married")

    # Lưu dữ liệu đã biến đổi vào HDFS dưới dạng ORC
    married_df.write.mode("overwrite").format("orc").save("hdfs://127.0.0.1:9000/hive/warehouse/hive_employees_married")

    # Tạo bảng Hive tham chiếu đến dữ liệu đã lưu trong HDFS
    spark.sql("""
    CREATE EXTERNAL TABLE IF NOT EXISTS hive_employees_married (
        id INT,
        name STRING,
        position STRING,
        salary DOUBLE,
        gender STRING,
        birth_year INT,
        married BOOLEAN,
        has_children BOOLEAN,
        hire_date DATE,
        age INT
    )
    STORED AS ORC
    LOCATION 'hdfs://127.0.0.1:9000/hive/warehouse/hive_employees_married'
    """)

    # Đóng Spark session
    spark.stop()

if __name__ == "__main__":
    main()