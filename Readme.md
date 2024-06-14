# Toàn cảnh Quy trình ETL sử dụng Hadoop, Spark và Hive

## 1. Extract (Trích xuất dữ liệu)

Trong bước này, dữ liệu được trích xuất từ **Data Source** (MySQL) và lưu trữ vào **Data Lake** (HDFS).

- **Kết nối MySQL và Trích xuất Dữ liệu**: Sử dụng PySpark để kết nối tới cơ sở dữ liệu MySQL và trích xuất bảng `employees`. Dữ liệu sau đó được lưu trữ dưới dạng file Parquet trong HDFS.

## 2. Transform (Biến đổi dữ liệu)

Sau khi dữ liệu được trích xuất và lưu trữ, nó sẽ được biến đổi để phù hợp với các yêu cầu phân tích và lưu trữ.

- **Biến đổi Dữ liệu**: Thực hiện các phép biến đổi trên DataFrame như thêm cột mới (ví dụ: cột `age` dựa trên năm sinh), lọc dữ liệu (ví dụ: chỉ giữ lại các nhân viên đã kết hôn).
- **Lưu Dữ liệu Biến đổi**: Sau khi biến đổi, dữ liệu được lưu trữ lại vào HDFS dưới dạng file ORC. 

## 3. Load (Tải dữ liệu)

Bước cuối cùng là tải dữ liệu vào **Data Warehouse** (Hive) để phân tích và truy vấn.

- **Tạo Bảng Hive**: Tạo bảng Hive liên kết với dữ liệu đã lưu trữ trong HDFS. Bảng này sẽ được sử dụng để thực hiện các truy vấn phân tích dữ liệu.
- **Phân tích Dữ liệu với Hive**: Sử dụng Hive để thực hiện các truy vấn SQL trên dữ liệu đã biến đổi.

### Tích hợp BI Tool

Để trực quan hóa dữ liệu, bạn có thể tích hợp một công cụ BI (Business Intelligence) như Apache Superset, Tableau, Power BI, hoặc bất kỳ công cụ BI nào khác hỗ trợ kết nối với Hive.

## Tổng kết các bước thực hiện:

### Bước 1: Trích xuất Dữ liệu từ MySQL vào HDFS thông qua Spark

1. **Kết nối đến MySQL**: Sử dụng JDBC để kết nối đến cơ sở dữ liệu MySQL.
2. **Trích xuất Dữ liệu**: Trích xuất bảng `employees` từ MySQL.
3. **Lưu Trữ vào HDFS**: Lưu dữ liệu trích xuất vào HDFS dưới dạng file Parquet.

### Bước 2: Biến đổi Dữ liệu với Spark và Lưu trữ trở lại HDFS

1. **Đọc Dữ liệu từ HDFS**: Đọc dữ liệu đã lưu trữ trong HDFS.
2. **Biến đổi Dữ liệu**: Thực hiện các phép biến đổi như thêm cột `age`, lọc nhân viên đã kết hôn.
3. **Lưu Dữ liệu đã Biến đổi vào HDFS**: Lưu dữ liệu đã biến đổi trở lại HDFS dưới dạng file ORC để tối ưu hóa hiệu suất truy vấn trong Hive.

### Bước 3: Sử dụng Hive để Quản lý và Phân tích Dữ liệu

1. **Tạo Bảng Hive từ Dữ liệu HDFS**: Tạo bảng Hive liên kết với dữ liệu đã biến đổi trong HDFS. Đây là bước đưa dữ liệu vào **Data Warehouse**.
2. **Phân tích và Truy vấn Dữ liệu**: Sử dụng Hive để thực hiện các truy vấn phân tích dữ liệu.

## Kết luận

Bằng cách sử dụng Hadoop, Spark và Hive, bạn có thể xây dựng một hệ thống ETL mạnh mẽ và linh hoạt. Quy trình này không chỉ giúp trích xuất và biến đổi dữ liệu từ **Data Source** (MySQL) một cách hiệu quả mà còn cho phép bạn lưu trữ và phân tích dữ liệu lớn trong **Data Lake** (HDFS) và **Data Warehouse** (Hive) một cách dễ dàng. Các công cụ BI có thể được sử dụng để trực quan hóa dữ liệu, tạo ra các bảng điều khiển đẹp mắt và cung cấp những cái nhìn sâu sắc về dữ liệu.

Đúng vậy, ELT (Extract, Load, Transform) là một quy trình xử lý dữ liệu mà trong đó dữ liệu được trích xuất (Extract) từ nguồn, sau đó được tải (Load) trực tiếp vào Data Warehouse mà không qua trung gian như Data Lake. Sau khi dữ liệu đã được nạp vào Data Warehouse, các phép biến đổi (Transform) sẽ được thực hiện trực tiếp trên đó để chuẩn bị cho các phân tích và truy vấn.

# Toàn cảnh Quy trình ELT

## 1. Extract (Trích xuất dữ liệu)

Trong bước này, dữ liệu được trích xuất từ **Data Source** (MySQL).

- **Kết nối MySQL và Trích xuất Dữ liệu**: Sử dụng công cụ ETL để kết nối tới cơ sở dữ liệu MySQL và trích xuất bảng `employees`.

## 2. Load (Tải dữ liệu)

Dữ liệu trích xuất được tải trực tiếp vào **Data Warehouse**.

- **Tải Dữ liệu vào Data Warehouse**: Dữ liệu được tải trực tiếp vào Data Warehouse (ví dụ: Hive) mà không qua bước trung gian như Data Lake. 

## 3. Transform (Biến đổi dữ liệu)

Sau khi dữ liệu đã được tải vào Data Warehouse, các phép biến đổi được thực hiện trên dữ liệu trong Data Warehouse để chuẩn bị cho các phân tích và truy vấn.

- **Biến đổi Dữ liệu trong Data Warehouse**: Thực hiện các phép biến đổi như thêm cột, tính toán, lọc dữ liệu... trực tiếp trên dữ liệu đã được tải vào Data Warehouse.


# So sánh ETL và ELT

## ETL (Extract, Transform, Load)

1. **Extract**: Trích xuất dữ liệu từ nguồn.
2. **Transform**: Biến đổi dữ liệu trong một hệ thống trung gian (như Spark, Hadoop).
3. **Load**: Tải dữ liệu đã biến đổi vào Data Warehouse.

- **Ưu điểm**: Dữ liệu được làm sạch và biến đổi trước khi nạp vào Data Warehouse, giúp tối ưu hóa không gian lưu trữ và hiệu suất truy vấn.
- **Nhược điểm**: Quy trình có thể phức tạp và tốn nhiều tài nguyên do cần có hệ thống trung gian để biến đổi dữ liệu.

## ELT (Extract, Load, Transform)

1. **Extract**: Trích xuất dữ liệu từ nguồn.
2. **Load**: Tải dữ liệu trực tiếp vào Data Warehouse.
3. **Transform**: Biến đổi dữ liệu trực tiếp trong Data Warehouse.

- **Ưu điểm**: Quy trình đơn giản hơn do không cần hệ thống trung gian để biến đổi dữ liệu. Tận dụng được sức mạnh tính toán của Data Warehouse để thực hiện các phép biến đổi.
- **Nhược điểm**: Có thể yêu cầu Data Warehouse mạnh mẽ để xử lý các phép biến đổi phức tạp và khối lượng dữ liệu lớn.

## Kết luận

Tùy thuộc vào nhu cầu và khả năng của hệ thống, bạn có thể chọn giữa ETL và ELT. ETL phù hợp khi bạn cần làm sạch và biến đổi dữ liệu trước khi nạp vào Data Warehouse, trong khi ELT đơn giản hóa quy trình bằng cách tải dữ liệu trực tiếp và thực hiện biến đổi sau trong Data Warehouse.