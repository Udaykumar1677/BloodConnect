from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # use your MySQL username
        password="",         # use your MySQL password
        database="bloodconnect"
    )

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Register Donor Page
@app.route('/register_donor', methods=['GET', 'POST'])
def register_donor():
    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        phone = request.form['phone']
        email = request.form['email']
        location = request.form['location']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO donors (name, blood_group, phone, email, location) VALUES (%s, %s, %s, %s, %s)",
                       (name, blood_group, phone, email, location))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/view_donors')
    return render_template('register_donor.html')

# View Donors
@app.route('/view_donors')
def view_donors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_donors.html', donors=donors)

# Request Blood Page
@app.route('/request_blood', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        phone = request.form['phone']
        email = request.form['email']
        location = request.form['location']
        reason = request.form.get('reason')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO requests (name, blood_group, phone, email, location, reason) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, blood_group, phone, email, location, reason))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/view_requests')
    return render_template('request_blood.html')

# View Requests
@app.route('/view_requests')
def view_requests():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM requests")
    requests_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_requests.html', requests=requests_data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
