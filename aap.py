from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = "replace_with_a_random_secret"

# MySQL connection config (change passwd if different / use RDS host if used)
db_config = {
    "host": "localhost",
    "user": "flaskuser",
    "password": "StrongPassword123",
    "database": "test_db"
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/insert', methods=['POST'])
def insert_employee():
    name = request.form.get('name')
    dob = request.form.get('date_of_birth') or None
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    qualification = request.form.get('qualification')
    job_stage = request.form.get('job_stage')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO employees
            (name, date_of_birth, email, mobile, qualification, job_stage)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, dob, email, mobile, qualification, job_stage))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Employee added successfully", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    return redirect(url_for('index'))

@app.route('/employees', methods=['GET'])
def employee_list():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees ORDER BY sr_no ASC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        rows = []
        flash(f"DB Error: {str(e)}", "danger")

    return render_template('list.html', employees=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

