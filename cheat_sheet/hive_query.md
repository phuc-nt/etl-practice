### Kiểm tra và truy vấn dữ liệu trong Hive

1. **Mở Hive shell**:

    ```bash
    hive
    ```

2. **Kiểm tra các bảng đã được tạo**:

    ```sql
    SHOW TABLES;
    ```

3. **Kiểm tra dữ liệu trong bảng `hive_employees_married`**:

    ```sql
    SELECT * FROM hive_employees_married LIMIT 10;
    ```

4. **Kiểm tra dữ liệu trong bảng `hive_employees_seniority`**:

    ```sql
    SELECT * FROM hive_employees_seniority LIMIT 10;
    ```

### Thực hiện các truy vấn phân tích

Bây giờ bạn có thể thực hiện các truy vấn phân tích để lấy thông tin từ dữ liệu.

1. **Tính mức lương trung bình theo giới tính từ bảng `hive_employees_married`**:

    ```sql
    SELECT gender, AVG(salary) AS average_salary
    FROM hive_employees_married
    GROUP BY gender;
    ```

2. **Tính mức lương trung bình theo nhóm tuổi từ bảng `hive_employees_married`**:

    ```sql
    SELECT age_group, AVG(salary) AS average_salary
    FROM (
        SELECT *,
               FLOOR(age / 10) * 10 AS age_group
        FROM hive_employees_married
    ) tmp
    GROUP BY age_group;
    ```

3. **Tính tỷ lệ nhân viên có con và không có con từ bảng `hive_employees_married`**:

    ```sql
    SELECT has_children, COUNT(*) AS count
    FROM hive_employees_married
    GROUP BY has_children;
    ```

4. **Tính mức lương trung bình của nhân viên có con so với không có con từ bảng `hive_employees_married`**:

    ```sql
    SELECT has_children, AVG(salary) AS average_salary
    FROM hive_employees_married
    GROUP BY has_children;
    ```

5. **Tính mức lương trung bình theo số thâm niên từ bảng `hive_employees_seniority`**:

    ```sql
    SELECT seniority, AVG(salary) AS average_salary
    FROM hive_employees_seniority
    GROUP BY seniority;
    ```

### Lưu lại kết quả

Bạn cũng có thể lưu lại kết quả của các truy vấn này vào các bảng mới trong Hive để sử dụng sau này.

```sql
CREATE TABLE avg_salary_by_gender AS
SELECT gender, AVG(salary) AS average_salary
FROM hive_employees_married
GROUP BY gender;

CREATE TABLE avg_salary_by_age_group AS
SELECT age_group, AVG(salary) AS average_salary
FROM (
    SELECT *,
           FLOOR(age / 10) * 10 AS age_group
    FROM hive_employees_married
) tmp
GROUP BY age_group;

CREATE TABLE avg_salary_by_seniority AS
SELECT seniority, AVG(salary) AS average_salary
FROM hive_employees_seniority
GROUP BY seniority;
```

Bằng cách này, bạn có thể thực hiện các phân tích và lưu trữ kết quả cho các truy vấn trong tương lai một cách dễ dàng. Nếu bạn cần hỗ trợ thêm hoặc có bất kỳ câu hỏi nào, đừng ngần ngại hỏi tôi!