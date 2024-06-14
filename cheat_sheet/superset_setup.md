### admin account
Username [admin]: admin
User first name [admin]: Admin
User last name [user]: Phuc
Email [admin@fab.org]: admin@phucnt.org
Password: 
Repeat for confirmation: 

### Hướng dẫn tích hợp Apache Superset với Hive và tạo Dashboard

Dưới đây là hướng dẫn chi tiết về cách cài đặt, cấu hình Apache Superset và kết nối với Hive để tạo Dashboard.

#### Bước 1: Cài đặt Apache Superset

1. **Cài đặt các thư viện cần thiết**:
    ```bash
    pip install apache-superset
    pip install pyhive
    pip install pandas
    pip install sqlalchemy
    pip install apache-superset[superset]
    ```

2. **Khởi tạo cơ sở dữ liệu cho Superset**:
    ```bash
    superset db upgrade
    ```

3. **Tạo tài khoản quản trị viên**:
    ```bash
    export FLASK_APP=superset
    superset fab create-admin
    # Bạn sẽ được yêu cầu nhập thông tin tài khoản quản trị viên
    ```

4. **Tải dữ liệu ví dụ (tùy chọn)**:
    ```bash
    superset load_examples
    ```

5. **Khởi tạo Superset**:
    ```bash
    superset init
    ```

6. **Chạy Superset**:
    ```bash
    superset run -p 8000 --with-threads --reload --debugger
    ```

7. **Truy cập Superset**:
    Mở trình duyệt và truy cập vào `http://localhost:8088`. Đăng nhập với tài khoản quản trị viên bạn đã tạo.

#### Bước 2: Kết nối Superset với Hive

1. **Thêm kết nối dữ liệu**:
    - Sau khi đăng nhập vào Superset, chọn **Sources** từ thanh điều hướng và chọn **Databases**.
    - Chọn **+ Database** để thêm kết nối mới.

2. **Cấu hình kết nối Hive**:
    - Điền thông tin kết nối Hive vào các trường cần thiết:
      - **Database**: Hive
      - **SQLAlchemy URI**: `hive://localhost:10000/default`
      - **Exposed in SQL Lab**: Tích chọn
    - Ví dụ về URI kết nối:
      ```plaintext
      hive://localhost:10000/default
      ```
    - Sau khi điền đầy đủ thông tin, chọn **Test Connection** để kiểm tra kết nối. Nếu kết nối thành công, chọn **Add** để thêm kết nối.

#### Bước 3: Tạo bảng từ dữ liệu Hive

1. **Tạo dataset**:
    - Chọn **Sources** từ thanh điều hướng và chọn **Datasets**.
    - Chọn **+ Dataset** để thêm dataset mới.
    - Chọn **Database** đã kết nối (Hive) và chọn bảng từ danh sách các bảng có sẵn (ví dụ: `hive_employees_married` hoặc `hive_employees_seniority`).

2. **Cấu hình dataset**:
    - Điền tên cho dataset và các thông tin cần thiết khác.
    - Chọn **Save** để lưu dataset.

#### Bước 4: Tạo Dashboard

1. **Tạo biểu đồ (Chart)**:
    - Chọn **Charts** từ thanh điều hướng và chọn **+ Chart**.
    - Chọn dataset đã tạo và chọn loại biểu đồ bạn muốn tạo (ví dụ: Bar Chart, Line Chart, Pie Chart, ...).
    - Cấu hình biểu đồ bằng cách chọn các trường và thiết lập các thông số cần thiết.

2. **Lưu biểu đồ**:
    - Sau khi cấu hình xong biểu đồ, chọn **Save** và điền tên cho biểu đồ.

3. **Tạo dashboard**:
    - Chọn **Dashboards** từ thanh điều hướng và chọn **+ Dashboard**.
    - Điền tên cho dashboard và chọn **Save**.
    - Sau khi tạo dashboard, chọn **Edit Dashboard** và kéo thả các biểu đồ đã tạo vào dashboard.

4. **Lưu dashboard**:
    - Sau khi thêm các biểu đồ vào dashboard, chọn **Save** để lưu dashboard.

### Tạo Dashboard từ các bảng Hive cụ thể

Dưới đây là ví dụ về cách tạo các biểu đồ và dashboard từ các bảng Hive cụ thể như `hive_employees_married` và `hive_employees_seniority`.

#### Ví dụ: Tạo biểu đồ mức lương trung bình theo giới tính từ bảng `hive_employees_married`

1. **Tạo biểu đồ Bar Chart**:
    - Chọn dataset `hive_employees_married`.
    - Chọn loại biểu đồ **Bar Chart**.
    - Cấu hình biểu đồ:
      - **Metrics**: `AVG(salary)`
      - **Group by**: `gender`
    - Chọn **Run** để xem trước biểu đồ và chọn **Save** để lưu biểu đồ.

#### Ví dụ: Tạo biểu đồ mức lương trung bình theo thâm niên từ bảng `hive_employees_seniority`

1. **Tạo biểu đồ Line Chart**:
    - Chọn dataset `hive_employees_seniority`.
    - Chọn loại biểu đồ **Line Chart**.
    - Cấu hình biểu đồ:
      - **Metrics**: `AVG(salary)`
      - **Group by**: `seniority`
    - Chọn **Run** để xem trước biểu đồ và chọn **Save** để lưu biểu đồ.

#### Tạo Dashboard và thêm biểu đồ

1. **Tạo Dashboard mới**:
    - Chọn **Dashboards** từ thanh điều hướng và chọn **+ Dashboard**.
    - Điền tên cho dashboard (ví dụ: `Employee Analysis`) và chọn **Save**.

2. **Thêm biểu đồ vào Dashboard**:
    - Chọn **Edit Dashboard** và kéo thả các biểu đồ đã tạo vào dashboard.
    - Chọn **Save** để lưu dashboard.

### Tóm tắt

1. **Cài đặt và cấu hình Superset**.
2. **Kết nối Superset với Hive**.
3. **Tạo datasets từ các bảng Hive**.
4. **Tạo biểu đồ và dashboard trong Superset**.

Bằng cách này, bạn có thể tạo các dashboard tương tác để trực quan hóa dữ liệu từ các bảng Hive. Nếu bạn có thêm câu hỏi hoặc cần hỗ trợ, đừng ngần ngại hỏi!