from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bloodconnect'
    )

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Register donor
@app.route('/register_donor', methods=['GET', 'POST'])
def register_donor():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        city = request.form['city']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO donors (name, age, blood_group, contact, city) VALUES (%s, %s, %s, %s, %s)",
                       (name, age, blood_group, contact, city))
        conn.commit()
        conn.close()
        return render_template('thank_you.html', message="Donor registered successfully!")
    return render_template('register_donor.html')

# Request blood
@app.route('/request_blood', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        city = request.form['city']
        reason = request.form['reason']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO requests (patient_name, age, blood_group, contact, city, reason) VALUES (%s, %s, %s, %s, %s, %s)",
                       (patient_name, age, blood_group, contact, city, reason))
        conn.commit()
        conn.close()
        return render_template('thank_you.html', message="Blood request submitted successfully!")
    return render_template('request_blood.html')

# View donors
@app.route('/view_donors')
def view_donors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    conn.close()
    return render_template('view_donors.html', donors=donors)

# View requests
@app.route('/view_requests')
def view_requests():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM requests")
    requests_data = cursor.fetchall()
    conn.close()
    return render_template('view_requests.html', requests=requests_data)

# Required for Render deployment (do not remove)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
