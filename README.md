# ♻️ Smart Plastic Waste Management System (AI + Full Stack Project)

An intelligent web-based system that uses **Machine Learning (CNN-based AI)** to classify waste materials from images and help promote **environmental sustainability through automation and analytics**.

This project combines:
- 🧠 Artificial Intelligence (CNN Image Classification)
- 🌐 Full Stack Web Development (Flask)
- 🎨 Modern UI/UX Design (Glassmorphism SaaS Dashboard)
- 📊 Real-time Waste Tracking System

---

# 🚀 Project Overview

The Smart Plastic Waste Management System is designed to:

- Classify waste images into categories using AI
- Track recyclable vs non-recyclable waste
- Store data in a database
- Display analytics in a modern dashboard
- Promote eco-friendly awareness using technology

This system acts as a **mini AI-powered environmental analytics platform**.

---

# 🧠 AI / Machine Learning Component

The system uses a **Convolutional Neural Network (CNN)** based on **MobileNetV2 (Transfer Learning)** for image classification.

### 🔍 Model Features:
- Image-based waste classification
- Trained on waste datasets (plastic, paper, glass, metal)
- Uses deep feature extraction (CNN layers)
- Provides prediction + confidence score

### 📦 Model Input:
- 224x224 RGB images

### 📤 Output:
- Waste category prediction
- Confidence score (%)

### 🧪 Example Predictions:
- Plastic Bottle → Plastic (97%)
- Newspaper → Paper (95%)
- Glass Bottle → Glass (93%)

---

# 🗂️ Dataset

The model is trained using publicly available waste image datasets.




---

# 🏗️ System Architecture

User Upload Image
↓
Flask Backend (app.py)
↓
CNN Model (MobileNetV2)
↓
Prediction Engine
↓
SQLite Database Storage
↓
Dashboard Visualization (HTML/CSS/JS)



---

# 💻 Tech Stack

### 🖥️ Frontend
- HTML5
- CSS3 (Glassmorphism UI)
- Vanilla JavaScript

### ⚙️ Backend
- Python
- Flask

### 🧠 AI Model
- TensorFlow / Keras
- MobileNetV2 (Transfer Learning)

### 🗄️ Database
- SQLite3

---

# 📁 Project Structure

project/
│
├── app.py # Flask backend
├── ml_model.py # CNN model loader & prediction
├── database.py # SQLite database logic
├── utils.py # Image preprocessing
│
├── waste_model.h5 # Trained CNN model
│
├── templates/
│ ├── index.html # Upload page
│ ├── dashboard.html # Analytics dashboard
│ └── landing.html # Landing page
│
├── static/
│ ├── css/
│ └── js/
│
├── dataset/ # Training dataset
└── README.md




---

# 🔥 Features

### 🧠 AI Features
- CNN-based image classification
- Real-time prediction
- Confidence scoring system

### 🌿 Environmental Impact
- Waste classification automation
- Recycling awareness system
- Smart environmental tracking

### 🌐 Web Features
- Modern landing page UI
- Interactive dashboard
- Form-based waste submission
- Real-time database updates

### 📊 Dashboard Features
- Total waste logs
- Recyclable vs non-recyclable tracking
- Latest submissions
- Clean analytics UI

---

# ⚙️ How It Works

1. User uploads waste image
2. Flask backend receives request
3. Image is processed using CNN model
4. Model predicts waste type
5. Result is stored in SQLite database
6. Dashboard displays updated analytics

---
# 🌍 Future Improvements

- 🌐 Deploy on cloud (Render / AWS)
- 📱 Mobile app integration
- 📸 Real-time camera detection
- 🧠 Upgrade to YOLO object detection
- 📊 Advanced analytics dashboard (charts + graphs)
- 🔐 Authentication system

---

# ⚠️ Limitations

- Requires dataset quality for accurate predictions  
- SQLite is not scalable for large production traffic  
- CNN model is lightweight (not industrial-scale yet)  
- No real-time video processing yet  

---

# 🎯 Project Goal

To demonstrate how **AI + Web Development** can be combined to build a smart environmental monitoring system that helps improve recycling awareness and waste management efficiency.

---

# 👨‍💻 Author

Developed as a Full Stack + AI learning project focused on:

- Machine Learning  
- Web Development  
- Environmental Technology  

---

# 📜 License

This project is for educational purposes only.
