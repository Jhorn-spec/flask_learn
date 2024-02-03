import requests
from flask import Flask, Blueprint
app = Flask(__name__)

from configparser import ConfigParser
config = ConfigParser()
config.read('./config/keys_config.cfg')

API_KEY = config.get('openweather', 'api_key')

# get weather by U.S. zip code
API_URL = ('https://api.openweathermap.org/data/2.5/weather?zip={},us&mode=json&units=imperial&appid={}')

def query_api(zip):
    """submit the API query using variables for ZIP and API_KEY"""
    try:
        # print(API_URL.format(zip, API_KEY))
        data = requests.get(API_URL.format(zip, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data

@app.route('/weather/<zip>')
def result(zip):
    # get the json file from the openweather API
    resp = queri_api(zip)
    # construct a string using the json data for 
    # temperature and description
    try:
        text = resp["name"] +  "temperature is " + str(resp["main"]["temp"]) + " degress Fahrenheit with " + resp["weather"][0]["description"] + "."
    except:
        text = "There was an error.<br>Didi you include a valid U.S. zip code in the URL?"
    return text

if __name__=='__main__':
    app.run(debug=True)