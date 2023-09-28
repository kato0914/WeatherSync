from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_weather():
    # 新しいYahoo天気のURL（八代市の場合）
    url = "https://weather.yahoo.co.jp/weather/43/8610/43202.html"

    # ページのHTMLを取得
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 天気情報を抽出
        # city = soup.find('h1', class_='yjw_cityname').text.strip()
        #今日の天気
        yahoo_weather_today_0 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td > small').text
        yahoo_weather_today_3 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td > small').text
        yahoo_weather_today_6 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td > small').text
        yahoo_weather_today_9 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td > small').text
        yahoo_weather_today_12 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td > small').text
        yahoo_weather_today_15 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td > small').text
        yahoo_weather_today_18 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td + td > small').text
        yahoo_weather_today_21 = soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td + td + td > small').text

        #明日の天気
        yahoo_weather_tomorrow_0 = soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr > td + td > small').text
        
        # return city, weather, temperature
    
    # 新しい@niffty天気のURL（八代市の場合）
        url = "https://weather.nifty.com/cs/catalog/weather_pinpoint/catalog_43202_1.htm"

    # ページのHTMLを取得
        response = requests.get(url)
    # if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 天気情報を抽出
        # city = soup.find('h1', class_='yjw_cityname').text.strip()
        #今日の天気
        niftty_weather_today_0 = soup.findAll('img')[6].get('alt')

        print(niftty_weather_today_0)

        #明日の天気
        # niftty_weather_tomorrow_0 = soup.select_one('#tomorrowWeather > table > tbody > tr + tr > td > img alt')
        
        # return city, weather, temperature
        return yahoo_weather_today_0, yahoo_weather_today_3, yahoo_weather_today_6, yahoo_weather_today_9, yahoo_weather_today_12, yahoo_weather_today_15, yahoo_weather_today_18, yahoo_weather_today_21, niftty_weather_today_0, yahoo_weather_tomorrow_0
    else:
        return None, None, None

@app.route('/')
def index():
    # city, yahoo_weather_today_0, temperature = scrape_weather()
    yahoo_weather_today_0, yahoo_weather_today_3, yahoo_weather_today_6, yahoo_weather_today_9, yahoo_weather_today_12, yahoo_weather_today_15, yahoo_weather_today_18, yahoo_weather_today_21, niftty_weather_today_0, yahoo_weather_tomorrow_0 = scrape_weather()
    # if city and yahoo_weather_today_0 and temperature:
    if yahoo_weather_today_0 and yahoo_weather_today_3 and yahoo_weather_today_6 and yahoo_weather_today_9 and yahoo_weather_today_12 and yahoo_weather_today_15 and yahoo_weather_today_18 and yahoo_weather_today_21 and niftty_weather_today_0 and yahoo_weather_tomorrow_0:
        # return render_template('weather.html', city=city, yahoo_weather_today_0=yahoo_weather_today_0, temperature=temperature)
        return render_template('weather.html', yahoo_weather_today_0=yahoo_weather_today_0, yahoo_weather_today_3=yahoo_weather_today_3, yahoo_weather_today_6=yahoo_weather_today_6, yahoo_weather_today_9=yahoo_weather_today_9, yahoo_weather_today_12=yahoo_weather_today_12, yahoo_weather_today_15=yahoo_weather_today_15, yahoo_weather_today_18=yahoo_weather_today_18, yahoo_weather_today_21=yahoo_weather_today_21, niftty_weather_today_0=niftty_weather_today_0, yahoo_weather_tomorrow_0=yahoo_weather_tomorrow_0)
    else:
        error_message = "天気情報を取得できませんでした。"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
