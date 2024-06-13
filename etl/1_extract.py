from pyspark.sql import SparkSession

# Tạo Spark session
spark = SparkSession.builder \
    .appName("Extract Data") \
    .config("spark.driver.extraClassPath", "lib/mysql-connector-j-8.4.0.jar") \
    .getOrCreate()

# URL kết nối tới MySQL
url = "jdbc:mysql://localhost:3306/mydb"
properties = {"user": "root", "password": "root", "driver": "com.mysql.cj.jdbc.Driver"}

# Đọc dữ liệu từ MySQL
df = spark.read.jdbc(url=url, table="employees", properties=properties)

# Lấy 100 bản ghi gần nhất (giả sử bạn có cột 'hire_date' để sắp xếp)
recent_records = df.orderBy(df.hire_date.desc()).limit(100)

# Ghi 100 bản ghi mới nhất ra HDFS
try:
    recent_records.write.mode("overwrite").parquet("hdfs://127.0.0.1:9000/employees_recent.parquet")
    print("Data written to HDFS successfully.")
except Exception as e:
    print(f"Error writing to HDFS: {e}")