# 🌦️ Weather App

A simple and responsive weather application built with **Flask** that provides real-time weather information using the **WeatherAPI**.

Users can search for any city and instantly view current weather details including temperature, humidity, weather condition, and weather icons.

🔗 **Live Demo:** https://weather-app-88o6.onrender.com

---

## ✨ Features

* 🔍 Search weather by city name
* 🌡️ Real-time temperature in Celsius
* 💧 Humidity information
* ☁️ Current weather condition
* 🌤️ Dynamic weather icons
* ❌ Invalid city error handling
* 🎨 Clean and simple user interface
* 🔐 Secure API key management using environment variables

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

### 🌤️ Weather Report

![Weather Report](screenshots/result.png)

---

## 🛠️ Tech Stack

### Backend

* 🐍 Python
* 🌶️ Flask
* 🔗 Requests
* 🔑 python-dotenv

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### API

* 🌎 WeatherAPI

### Deployment

* 🚀 Render
* 🐙 GitHub

---

## 📁 Project Structure

```text
weatherapp/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── error.html
│
├── screenshots/
│   ├── home.png
│   └── result.png
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

Follow these steps to run the project locally.

## 1. Clone the repository

```bash
git clone https://github.com/vikassagar-creator/weather-app.git

cd weather-app
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv env

env\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv env

source env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=YOUR_WEATHERAPI_KEY
```

Get your free API key from:

https://www.weatherapi.com/

---

## 5. Run the Application

Start the Flask development server:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📌 How It Works

1. User enters a city name.
2. Flask receives the request.
3. The application sends a request to WeatherAPI.
4. Weather data is processed and displayed.

The application displays:

* 📍 Location
* 🌡️ Temperature
* 💧 Humidity
* ☁️ Weather condition
* 🌤️ Weather icon

If the city does not exist, the application shows an error page.

---

# 📦 Dependencies

Main packages used:

```text
Flask
requests
python-dotenv
Jinja2
gunicorn
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Deployment

This application is deployed using **Render**.

Production server:

```bash
gunicorn app:app
```

The application automatically redeploys whenever changes are pushed to GitHub.

---

# 🔒 Security

* API keys are stored using environment variables.
* `.env` files are excluded using `.gitignore`.
* Sensitive information is never committed to GitHub.

---

# 🔮 Future Improvements

* 📅 7-day weather forecast
* 📍 Automatic user location detection
* 🌙 Dark mode support
* 💨 Wind speed and pressure details
* 🌅 Sunrise and sunset information
* 🔎 Search history
* 📱 Better mobile responsiveness

---

# 👨‍💻 Author

**Vikas Sagar**

GitHub:
https://github.com/vikassagar-creator

---

# 📄 License

This project is open source and available under the **MIT License**.
