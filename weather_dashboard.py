from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = 'https://api.open-meteo.com/v1/forecast'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        response = requests.get(API_URL, params={
            'latitude': latitude,
            'longitude': longitude,
            'current_weather': True
        })
        weather_data = response.json()['current_weather']
        return render_template('weather.html', weather=weather_data)
    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)