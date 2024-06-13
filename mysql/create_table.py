import mysql.connector

# Kết nối đến MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()

# Tạo cơ sở dữ liệu nếu chưa tồn tại
cursor.execute("CREATE DATABASE IF NOT EXISTS mydb")
cursor.execute("USE mydb")

# Tạo bảng employees với các cột yêu cầu
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    birth_year INT NOT NULL,
    married BOOLEAN NOT NULL,
    has_children BOOLEAN NOT NULL,
    hire_date DATE NOT NULL
)
"""
cursor.execute(create_table_query)

# Đóng kết nối
cursor.close()
conn.close()

print("Table 'employees' created successfully.")