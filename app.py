from flask import Flask, render_template , request
import requests



from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")


app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')
    
@app.route('/submit', methods =['POST'])
def submit():
    
   
    city = request.form['city'] 
    

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)



    data = response.json()
    if "error" in data:
        return render_template("error.html")
    elif response.status_code == 200:
        
    
        location = data["location"]["name"]
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        condition = data["current"]["condition"]["text"]
        icon = data["current"]["condition"]["icon"]
    
        return render_template(
            "result.html",
            city=city,
            location=location,
            temp=temp,
            humidity=humidity,
            condition=condition,
            icon=icon
        )

    
        

























if __name__ == "__main__":
    app.run(debug=True)