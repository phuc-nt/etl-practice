### Table of Contents

- [Table of Contents](#table-of-contents)
- [Bối cảnh](#bối-cảnh)
- [Giới thiệu về Data-Driven](#giới-thiệu-về-data-driven)
- [Lợi ích của Data-Driven cho Công ty](#lợi-ích-của-data-driven-cho-công-ty)
- [Giải pháp ELT (Extract, Load, Transform)](#giải-pháp-elt-extract-load-transform)
- [Các Use Case với các Kiểu Dữ liệu](#các-use-case-với-các-kiểu-dữ-liệu)
- [Công nghệ dự kiến sử dụng](#công-nghệ-dự-kiến-sử-dụng)
- [Kết luận](#kết-luận)

### Bối cảnh

Công ty chúng ta hiện sở hữu nhiều dữ liệu quan trọng, nhưng dữ liệu này bị phân tán và quản lý bởi các team khác nhau, dẫn đến quy trình quản lý dữ liệu chưa thống nhất. Điều này làm giảm hiệu quả trong phân tích dữ liệu và tìm kiếm insight, ảnh hưởng đến khả năng ra quyết định chính xác và kịp thời, cũng như tối ưu hóa hoạt động và phát triển sản phẩm. Để luôn là lựa chọn tốt nhất của công ty mẹ LY tại Nhật Bản, chúng ta cần liên tục cải thiện quy trình và hiệu quả hoạt động.

### Giới thiệu về Data-Driven

Data-driven (dữ liệu hướng dẫn quyết định) là việc sử dụng dữ liệu để đưa ra các quyết định và chiến lược kinh doanh. Trong môi trường này, các quyết định được dựa trên phân tích dữ liệu thực tế thay vì cảm tính.

### Lợi ích của Data-Driven cho Công ty

Áp dụng chiến lược data-driven mang lại những lợi ích sau:

1. **Khám phá và hiểu rõ các insight của công ty:** Phân tích dữ liệu giúp chúng ta nhận diện các cơ hội và thách thức, hiểu rõ hơn về hiệu suất hoạt động, nhu cầu của khách hàng, và xu hướng thị trường, từ đó đưa ra các quyết định chính xác và kịp thời.
2. **Đặt mục tiêu và chiến lược phù hợp:** Sử dụng dữ liệu để xác định các mục tiêu rõ ràng và chiến lược thuyết phục, giúp chúng ta dễ dàng theo dõi tiến độ và kiểm chứng kết quả đạt được.
3. **Dễ dàng áp dụng AI:** Dữ liệu được quản lý và phân tích một cách hiệu quả tạo điều kiện thuận lợi cho việc triển khai các giải pháp AI và machine learning, giúp chúng ta tự động hóa quy trình, dự đoán xu hướng, và cải thiện chất lượng sản phẩm một cách thông minh.

### Giải pháp ELT (Extract, Load, Transform)
![ELT](img/ELT.png)

ELT là phương pháp xử lý dữ liệu phổ biến, bao gồm ba bước chính:

1. **Extract (Trích xuất):** Dữ liệu được trích xuất từ nhiều nguồn khác nhau như cơ sở dữ liệu, hệ thống CRM, web, v.v.
2. **Load (Tải):** Dữ liệu thô được tải trực tiếp vào Data Lake hoặc Data Warehouse.
3. **Transform (Biến đổi):** Quá trình biến đổi diễn ra trong Data Lake hoặc Data Warehouse, giúp làm sạch, lọc, và chuẩn bị dữ liệu cho phân tích.

### Các Use Case với các Kiểu Dữ liệu

**1. Dữ liệu Nhân Viên:**
   - **Trích xuất dữ liệu:** Dữ liệu được trích xuất từ các hệ thống RDBMS, NoSQL.
   - **Tải dữ liệu thô:** Dữ liệu thô được tải vào Data Lake hoặc Data Warehouse.
   - **Biến đổi dữ liệu:** Dữ liệu được làm sạch, tính toán các chỉ số hiệu suất làm việc, tuổi tác, thâm niên, v.v.
   - **Ứng dụng:** Báo cáo hiệu suất, phân tích dữ liệu nhân sự để đề xuất các chương trình đào tạo phù hợp và tối ưu hóa quản lý nhân sự.

**2. Dữ liệu Comment trên PR và Đánh giá Chất lượng Code từ GitHub và SonarQube:**
   - **Trích xuất dữ liệu:** Dữ liệu được trích xuất từ GitHub API và SonarQube API.
   - **Tải dữ liệu thô:** Dữ liệu thô được tải vào Data Lake hoặc Data Warehouse.
   - **Biến đổi dữ liệu:** Dữ liệu được làm sạch, tổng hợp và phân tích các chỉ số như số lượng comment, loại comment (xây dựng, phê bình, câu hỏi), số lỗi và mức độ nghiêm trọng của lỗi.
   - **Ứng dụng:** Phân tích chất lượng code, xu hướng lỗi theo thời gian, cải thiện quy trình review code, và sử dụng machine learning để dự đoán lỗi tiềm ẩn trong code.

**3. Thông tin Dự án trên JIRA:**
   - **Trích xuất dữ liệu:** Dữ liệu được trích xuất từ JIRA API.
   - **Tải dữ liệu thô:** Dữ liệu thô được tải vào Data Lake hoặc Data Warehouse.
   - **Biến đổi dữ liệu:** Dữ liệu được làm sạch, tổng hợp và phân tích các chỉ số như tiến độ dự án, hiệu suất đội ngũ, so sánh estimated effort và actual effort, xác định các điểm nghẽn trong quy trình.
   - **Ứng dụng:** Quản lý dự án hiệu quả, tối ưu hóa quy trình làm việc, phân bổ tài nguyên hợp lý, và dự báo tiến độ dự án.

### Công nghệ dự kiến sử dụng
**HDFS**, **Spark** và **Hive** có thể đảm nhận nhiều vai trò:

1. **Data Lake và Data Warehouse:**
   - **HDFS (Hadoop Distributed File System):** Sử dụng HDFS để tập trung và quản lý dữ liệu thô (Data Lake) và dữ liệu đã biến đổi (Data Warehouse).

2. **Công cụ Trích xuất và Tải dữ liệu:**
   - **Spark:** Sử dụng Apache Spark để trích xuất và tải dữ liệu từ nhiều nguồn khác nhau vào HDFS.

3. **Công cụ Biến đổi dữ liệu:**
   - **Spark:** Sử dụng Spark để thực hiện các tác vụ biến đổi dữ liệu, như làm sạch, tổng hợp và tính toán các chỉ số.
   - **Hive:** Sử dụng Hive để quản lý dữ liệu đã biến đổi và hỗ trợ truy vấn dữ liệu dưới dạng bảng SQL.

4. **Công cụ Phân tích và BI:**
   - **Hive:** Tạo và quản lý bảng dữ liệu trong Hive, hỗ trợ truy vấn dữ liệu lớn.
   - **Spark:** Sử dụng Spark để thực hiện các phân tích dữ liệu phức tạp.
   - **Công cụ BI:** Kết nối với các công cụ phân tích và Business Intelligence như Tableau, Power BI hoặc Looker để tạo báo cáo và dashboard.

5. **AI và Machine Learning:**
   - **Spark MLlib:** Sử dụng thư viện machine learning của Spark để phát triển và triển khai các mô hình AI/ML.
   - **Jupyter Notebooks:** Sử dụng Jupyter Notebooks kết hợp với Spark để thực hiện các phân tích dữ liệu và huấn luyện mô hình machine learning.

### Kết luận

Việc áp dụng giải pháp ELT và chiến lược Data-Driven sẽ giúp:

- Tập trung dữ liệu từ nhiều nguồn và định dạng về một nơi, như Data Lake hoặc Data Warehouse, tạo ra một hệ thống quản lý dữ liệu thống nhất và hiệu quả.
- Dễ dàng lưu trữ, quản lý và phân tích dữ liệu, từ đó khám phá các insight mới, đặt mục tiêu và chiến lược cụ thể, và kiểm chứng kết quả một cách chính xác.
- Tạo điều kiện thuận lợi cho việc triển khai các giải pháp AI và machine learning, giúp tự động hóa quy trình, dự đoán xu hướng, và cải thiện chất lượng sản phẩm.

Đầu tư phát triển hệ thống ELT và có mindset về Data Driven sẽ giúp công ty chúng ta nâng cao hiệu quả hoạt động và cạnh tranh mạnh mẽ hơn trên thị trường. Điều này không chỉ giúp chúng ta hoàn thành tốt các dự án hiện tại mà còn tăng khả năng nhận thêm nhiều dự án từ công ty mẹ LY, khẳng định vị thế là đối tác phát triển phần mềm hàng đầu của LY.