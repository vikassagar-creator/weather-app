from flask import Flask, render_template , request
from services.weather_service import fetch_weather,WeatherAPIError
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')
    
@app.route("/submit", methods =['POST'])
def submit():
    city = request.form.get("city"," ").strip()
    if not city:
        return render_template("error.html", message="please enter a city name")
    
    try:
        weather = fetch_weather(city)
    except WeatherAPIError as e:
        return render_template("error.html",message=str(e))


    return render_template(
            "result.html",
            weather=weather
        )


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "False") == "True")