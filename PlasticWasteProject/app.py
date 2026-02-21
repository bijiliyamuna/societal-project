import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect
import sqlite3
import joblib

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = joblib.load("waste_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add_waste():
    plastic_type = request.form['plastic_type']
    quantity = int(request.form['quantity'])

    # Get image from form
    image = request.files['image']

    # Secure file name
    filename = secure_filename(image.filename)

    # Save image to uploads folder
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    plastic_map = {"PET": 0, "HDPE": 1, "PVC": 2}
    plastic_value = plastic_map.get(plastic_type, 0)

    prediction = model.predict([[plastic_value, quantity]])
    recyclable = "Yes" if prediction[0] == 1 else "No"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO waste (plastic_type, quantity, recyclable) VALUES (?, ?, ?)",
        (plastic_type, quantity, recyclable)
    )
    conn.commit()
    conn.close()

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM waste")
    data = cursor.fetchall()
    conn.close()
    return render_template("dashboard.html", data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)