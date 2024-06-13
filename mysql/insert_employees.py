import random
import mysql.connector
from faker import Faker
from datetime import datetime

fake = Faker()
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb"
)
cursor = conn.cursor()

positions = [
    'Software Engineer', 'Data Scientist', 'Product Manager',
    'Designer', 'QA Engineer', 'HR Manager', 'Sales Manager'
]

# Chuyển đổi ngày bắt đầu và kết thúc thành đối tượng datetime
start_date = datetime.strptime('2011-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2011-12-31', '%Y-%m-%d')

for _ in range(300):
    name = fake.name()
    position = random.choice(positions)
    salary = round(random.uniform(50000, 100000), 2)
    gender = random.choice(['Male', 'Female'])
    birth_year = random.randint(1960, 1995)
    married = random.choice([True, False])
    has_children = random.choice([True, False])
    hire_date = fake.date_between(start_date=start_date, end_date=end_date)  # Sử dụng đối tượng datetime

    cursor.execute("""
        INSERT INTO employees (name, position, salary, gender, birth_year, married, has_children, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, position, salary, gender, birth_year, married, has_children, hire_date))

conn.commit()
cursor.close()
conn.close()
print("Inserted into employees table.")