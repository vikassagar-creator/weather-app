from flask import Flask, render_template , request
import requests
import json


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
        return f'''invalid city
        <p><a class="back" href="/">[ GO BACK ]</a></p>'''
    elif response.status_code == 200:
        
    
        location = data["location"]["name"]
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        condition = data["current"]["condition"]["text"]

    
        return f"""
        <h2>weather report</h2>
        You searched:{city}<br>
        showing result for:{location}<br>
        temperature:{temp}<br>
        humidity:{humidity}<br>
        condition:{condition}
        <p><a class="link-opacity-100-hover" href="/">[ GO BACK ]</a></p>"""

    
        

























if __name__ == "__main__":
    app.run(debug=True)