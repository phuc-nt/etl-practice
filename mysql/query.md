docker-compose -f docker-compose-mysql.yml up -d



### Cách thực hiện trong MySQL

1. **Kết nối vào MySQL**:

   ```bash
   docker exec -it mysql-source mysql -u root -p
   ```

   Sau đó nhập mật khẩu `root`.

2. **Đếm số nhân viên Nam**:

   ```sql
   USE mydb;

   SELECT COUNT(*) AS male_employee_count
   FROM employees
   WHERE gender = 'Male';
   ```

3. **Liệt kê 10 bản ghi mới nhất theo `hire_date`**:

   ```sql
   USE mydb;

   SELECT *
   FROM employees
   ORDER BY hire_date DESC
   LIMIT 10;
   ```

4. **Liệt kê tên và giới tính của các nhân viên có vị trí là `Product Manager`**:

   ```sql
   USE mydb;

   SELECT name, gender
   FROM employees
   WHERE position = 'Product Manager';
   ```