import requests
from flask import Flask, render_template, request
from config import API_KEY

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error_message = None
    if request.method == 'POST':
        city_name = request.form.get('city')
        if city_name:
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ja"
            
            response = requests.get(api_url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = f"「{city_name}」が見つからないか、APIに問題が発生しました。"
        else:
            error_message = "都市名を入力してください。"

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)