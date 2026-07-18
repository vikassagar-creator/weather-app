from flask import Flask, render_template , request
import requests
import datetime

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')
    
@app.route("/submit", methods =['POST'])
def submit():
    city = request.form['city'] 
    
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)

    data = response.json()
    if "error" in data:
        return render_template("error.html")
    local_time = datetime.datetime.strptime(data["location"]["localtime"], "%Y-%m-%d %H:%M")
    formated_time = local_time.strftime("%a, %d %b %Y %I:%M %p")
    
    weather = {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "region": data["location"]["region"],
        "localtime": formated_time,

        "temperature": data["current"]["temp_c"],
        "feelslike": data["current"]["feelslike_c"],
        "condition": data["current"]["condition"]["text"],
        "icon": data["current"]["condition"]["icon"],

        "humidity": data["current"]["humidity"],
        "wind_speed": data["current"]["wind_kph"],
        "pressure": data["current"]["pressure_mb"],
        "visibility": data["current"]["vis_km"],
        "uv_index": data["current"]["uv"],
        "cloud": data["current"]["cloud"],
    }
    return render_template(
            "result.html",
            weather=weather
        )









if __name__ == "__main__":
    app.run(debug=True)