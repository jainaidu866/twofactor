from flask import Flask, render_template, request, redirect, url_for, session, flash
import bcrypt
import mysql.connector
import random
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="chintujay",
        database="twofa_app"
    )

def send_otp_email(recipient_email, otp):
    sender = 'jaikumarnaidu123@gmail.com'  # <-- your Gmail address
    sender_password = 'qxebsvucplwnfoxq'  # <-- your 16-letter App Password (no spaces)
    subject = "Your OTP Code"
    message = f"Your OTP code is: {otp}"
    msg = MIMEText(message)
    msg['From'] = sender
    msg['To'] = recipient_email
    msg['Subject'] = subject

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, sender_password)
    server.sendmail(sender, [recipient_email], msg.as_string())
    server.quit()

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users3 WHERE username=%s", (username,))
        if cursor.fetchone():
            flash('Username already exists!')
            cursor.close()
            db.close()
            return render_template('register.html')
        cursor.execute("INSERT INTO users3 (username, password_hash) VALUES (%s, %s)", (username, password_hash))
        db.commit()
        cursor.close()
        db.close()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users3 WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()
        db.close()
        if user and bcrypt.checkpw(password.encode(), user['password_hash'].encode()):
            session['username'] = username
            return redirect(url_for('enter_contact'))
        else:
            flash('Invalid login or password')
    return render_template('login.html')

@app.route('/enter_contact', methods=['GET', 'POST'])
def enter_contact():
    if not session.get('username'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        contact_email = request.form['contact']
        otp = str(random.randint(100000, 999999))
        session['otp'] = otp
        session['contact'] = contact_email
        send_otp_email(contact_email, otp)
        flash('OTP sent to your email. Please check your inbox (and spam folder).')
        return redirect(url_for('verify_otp'))
    return render_template('enter_contact.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        entered_otp = request.form.get('otp')
        if entered_otp == session.get('otp'):
            session['otp_verified'] = True
            flash('OTP verified successfully!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid OTP. Please try again.')
    return render_template('verify_otp.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('otp_verified'):
        return redirect(url_for('enter_contact'))
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
