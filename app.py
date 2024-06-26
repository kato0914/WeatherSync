from flask import Flask, render_template, make_response
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.parse, pytz

app = Flask(__name__)

@app.route('/example')
def example_route():
    response = make_response(render_template('example.html'))
    response.headers['Cache-Control'] = 'public, max-age=3600'  # キャッシュの有効期限を1時間に設定
    return response

def scrape_weather():

    dt_now = datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%m月%d日 %H時%M分現在")
    print(dt_now)


    # 新しいYahoo天気のURL（八代市の場合）
    url = "https://weather.yahoo.co.jp/weather/43/8610/43202.html"

    # ページのHTMLを取得
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 天気情報を抽出
        # city = soup.find('h1', class_='yjw_cityname').text.strip()
        #今日の天気

        yahoo_weather_today = [
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        
        # "曇り" を "くもり" に置換
        for i in range(len(yahoo_weather_today)):
            yahoo_weather_today[i] = yahoo_weather_today[i].replace('曇り', '曇').replace('晴れ', '晴')
    
        print(yahoo_weather_today)

        
        #明日の天気

        yahoo_weather_tomorrow = [
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        
        # "曇り" を "くもり" に置換
        for i in range(len(yahoo_weather_tomorrow)):
            yahoo_weather_tomorrow[i] = yahoo_weather_tomorrow[i].replace('曇り', '曇').replace('晴れ', '晴')
    
        print(yahoo_weather_tomorrow)

        # 今日の気温
        yahoo_temp_today = [
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        print(yahoo_temp_today)

        # 明日の気温
        yahoo_temp_tomorrow = [
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        print(yahoo_temp_tomorrow)

        # 今日の湿度
        yahoo_humidity_today = [
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        print(yahoo_humidity_today)

        # 明日の湿度
        yahoo_humidity_tomorrow = [
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        print(yahoo_humidity_tomorrow)

        # 今日の降水量
        yahoo_precipitation_today = [
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_today > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        print(yahoo_precipitation_today)

        # 明日の降水量
        yahoo_precipitation_tomorrow = [
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td + td + td > small').text,
        soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr + tr + tr + tr > td + td + td + td + td + td + td + td + td > small').text,
        ]
        print(yahoo_precipitation_tomorrow)

        
    # 新しい@niffty天気のURL（八代市の場合）
        url = "https://weather.nifty.com/cs/catalog/weather_pinpoint/catalog_43202_1.htm"

    # ページのHTMLを取得
        response = requests.get(url)
    # if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 天気情報を抽出
        # city = soup.find('h1', class_='yjw_cityname').text.strip()
        #今日の天気
        niftty_weather_today = [
        soup.findAll('img')[8].get('alt'),
        soup.findAll('img')[9].get('alt'),
        soup.findAll('img')[10].get('alt'),
        soup.findAll('img')[11].get('alt'),
        soup.findAll('img')[12].get('alt'),
        soup.findAll('img')[13].get('alt'),
        soup.findAll('img')[14].get('alt'),
        soup.findAll('img')[15].get('alt'),
        ]

        # "曇り" を "くもり" に置換
        for i in range(len(niftty_weather_today)):
            niftty_weather_today[i] = niftty_weather_today[i].replace('くもり', '曇').replace('晴れ', '晴')
    
        print(niftty_weather_today)

        #明日の天気
        niftty_weather_tomorrow = [
        soup.findAll('img')[17].get('alt'),
        soup.findAll('img')[18].get('alt'),
        soup.findAll('img')[19].get('alt'),
        soup.findAll('img')[20].get('alt'),
        soup.findAll('img')[21].get('alt'),
        soup.findAll('img')[22].get('alt'),
        soup.findAll('img')[23].get('alt'),
        soup.findAll('img')[24].get('alt'),
        ]
        
        # "曇り" を "くもり" に置換
        for i in range(len(niftty_weather_tomorrow)):
            niftty_weather_tomorrow[i] = niftty_weather_tomorrow[i].replace('くもり', '曇').replace('晴れ', '晴')
        print(niftty_weather_tomorrow)

        # 新しいお天気ナビゲーターのURL（八代市の場合）
        url = "https://s.n-kishou.co.jp/w/charge/jikei/jikeid.html?ba=43&code=43202&fla=day"

        # ページのHTMLを取得
        response = requests.get(url)
        # if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 天気情報を抽出
        navigater_weather_today = soup.findAll('p',attrs={'class':'box-weather-data-txt'})[0].text

        navigater_weather_today = navigater_weather_today.replace('晴れ', '晴').replace('くもり', '曇')

        navigater_weather_tomorrow = soup.findAll('p',attrs={'class':'box-weather-data-txt'})[1].text

        navigater_weather_tomorrow = navigater_weather_tomorrow.replace('晴れ', '晴').replace('くもり', '曇')
        print(navigater_weather_tomorrow)
        
        # return city, weather, temperature
        return yahoo_weather_today, niftty_weather_today, navigater_weather_today, navigater_weather_tomorrow, yahoo_weather_tomorrow, niftty_weather_tomorrow, yahoo_temp_today, yahoo_temp_tomorrow, yahoo_humidity_today, yahoo_humidity_tomorrow, yahoo_precipitation_today, yahoo_precipitation_tomorrow, dt_now
    else:
        return None, None, None

@app.route('/')
def index():
    # city, yahoo_weather_today_0, temperature = scrape_weather()
    yahoo_weather_today, niftty_weather_today,  navigater_weather_today, navigater_weather_tomorrow, yahoo_weather_tomorrow, niftty_weather_tomorrow, yahoo_temp_today, yahoo_temp_tomorrow, yahoo_humidity_today, yahoo_humidity_tomorrow, yahoo_precipitation_today, yahoo_precipitation_tomorrow, dt_now = scrape_weather()
    # if city and yahoo_weather_today_0 and temperature:
    if yahoo_weather_today and niftty_weather_today and  navigater_weather_today and yahoo_weather_tomorrow and niftty_weather_tomorrow and navigater_weather_tomorrow and yahoo_temp_today and yahoo_temp_tomorrow and yahoo_humidity_today and yahoo_humidity_tomorrow and yahoo_precipitation_today and yahoo_precipitation_tomorrow and dt_now:
        # return render_template('weather.html', city=city, yahoo_weather_today_0=yahoo_weather_today_0, temperature=temperature)
        return render_template('weather.html', yahoo_weather_today=yahoo_weather_today, niftty_weather_today=niftty_weather_today, navigater_weather_today= navigater_weather_today, yahoo_weather_tomorrow=yahoo_weather_tomorrow, yahoo_temp_tomorrow=yahoo_temp_tomorrow, niftty_weather_tomorrow=niftty_weather_tomorrow, navigater_weather_tomorrow=navigater_weather_tomorrow, yahoo_temp_today=yahoo_temp_today, yahoo_humidity_today=yahoo_humidity_today, yahoo_humidity_tomorrow=yahoo_humidity_tomorrow, yahoo_precipitation_today=yahoo_precipitation_today, yahoo_precipitation_tomorrow=yahoo_precipitation_tomorrow, dt_now=dt_now)
    else:
        error_message = "天気情報を取得できませんでした。"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
