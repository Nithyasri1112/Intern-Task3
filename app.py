from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = '9f2b3c8b3e2f44b7a8d1a2b3c4e5f6d7'  # Add any random string

API_KEY = '294612a65dd101ecdbb2468d91468799'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')

        if city:
            params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
            response = requests.get(BASE_URL, params=params)
            
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = "City not found. Please try again!"

    return render_template('index.html', weather=weather_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
