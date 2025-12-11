# Employee Management System (Flask + MySQL + AWS EC2)

This is a simple Employee Management Web Application built using **Python Flask**, **MySQL**, and deployed on **AWS EC2**.  
The app allows users to:

✔ Add new employees  
✔ Store employee data into MySQL  
✔ View all employees in a table format  
✔ Run on a production server using Gunicorn + Nginx  

---

## 🚀 Features

- **Flask Web Application**
- **HTML Form** to insert employee records
- **MySQL Database**
- **Employee List View**
- **AWS EC2 Deployment**
- **Gunicorn + Nginx Production Setup**
- Clean and simple UI

---

## 🏗️ Project Structure
flask_employee/
│── app.py
│── requirements.txt
│── templates/
│ ├── form.html
│ └── list.html
│── venv/
│── .gitignore

Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
Install Requirements
pip install -r requirements.txt
Configure MySQL Database Login:
mysql -u root -p or sudo mysql
Create DB:
CREATE DATABASE test_db;  SHOW DATABASES; USE test_db; SHOW TABLES;
Create table:
CREATE TABLE employees (
    sr_no INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    date_of_birth DATE,
    email VARCHAR(150),
    mobile VARCHAR(20),
    qualification VARCHAR(100),
    job_stage VARCHAR(50)
);
DESCRIBE employees;
Table के सभी Data show       
SELECT * FROM employees;    (mysql -u root -p -e "SELECT * FROM test_db.employees;")
Run Flask App
python app.py


