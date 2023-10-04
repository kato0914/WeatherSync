from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import urllib.parse

app = Flask(__name__)

def scrape_weather():

    dt_now = datetime.now().strftime("%Y年%m月%d%日%H時%M分%S秒現在")
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

        yahoo_weather_today = []
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td > small').text)
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td > small').text)
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td > small').text)
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td > small').text)
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td > small').text)
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td > small').text)
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td + td > small').text)
        yahoo_weather_today.append(soup.select_one('#yjw_pinpoint_today > table >tbody > tr + tr > td + td + td + td + td + td + td + td + td > small').text)
        
        # "曇り" を "くもり" に置換
        for i in range(len(yahoo_weather_today)):
            yahoo_weather_today[i] = yahoo_weather_today[i].replace('曇り', '曇').replace('晴れ', '晴')
    
        print(yahoo_weather_today)

        
        #明日の天気

        yahoo_weather_tomorrow = []
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr > td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table > tbody > tr + tr > td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td + td > small').text)
        yahoo_weather_tomorrow.append(soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td + td + td > small').text)
        
        # "曇り" を "くもり" に置換
        for i in range(len(yahoo_weather_tomorrow)):
            yahoo_weather_tomorrow[i] = yahoo_weather_tomorrow[i].replace('曇り', '曇').replace('晴れ', '晴')
    
        print(yahoo_weather_tomorrow)
    # 新しい@niffty天気のURL（八代市の場合）
        url = "https://weather.nifty.com/cs/catalog/weather_pinpoint/catalog_43202_1.htm"

    # ページのHTMLを取得
        response = requests.get(url)
    # if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 天気情報を抽出
        # city = soup.find('h1', class_='yjw_cityname').text.strip()
        #今日の天気
        niftty_weather_today = []
        niftty_weather_today.append(soup.findAll('img')[8].get('alt'))
        niftty_weather_today.append(soup.findAll('img')[9].get('alt'))
        niftty_weather_today.append(soup.findAll('img')[10].get('alt'))
        niftty_weather_today.append(soup.findAll('img')[11].get('alt'))
        niftty_weather_today.append(soup.findAll('img')[12].get('alt'))
        niftty_weather_today.append(soup.findAll('img')[13].get('alt'))
        niftty_weather_today.append(soup.findAll('img')[14].get('alt'))
        niftty_weather_today.append(soup.findAll('img')[15].get('alt'))

        # "曇り" を "くもり" に置換
        for i in range(len(niftty_weather_today)):
            niftty_weather_today[i] = niftty_weather_today[i].replace('くもり', '曇').replace('晴れ', '晴')
    
        print(niftty_weather_today)

        #明日の天気
        niftty_weather_tomorrow = []
        niftty_weather_tomorrow.append(soup.findAll('img')[17].get('alt'))
        niftty_weather_tomorrow.append(soup.findAll('img')[18].get('alt'))
        niftty_weather_tomorrow.append(soup.findAll('img')[19].get('alt'))
        niftty_weather_tomorrow.append(soup.findAll('img')[20].get('alt'))
        niftty_weather_tomorrow.append(soup.findAll('img')[21].get('alt'))
        niftty_weather_tomorrow.append(soup.findAll('img')[22].get('alt'))
        niftty_weather_tomorrow.append(soup.findAll('img')[23].get('alt'))
        niftty_weather_tomorrow.append(soup.findAll('img')[24].get('alt'))
        
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

        navigater_weather_tommorow = soup.findAll('p',attrs={'class':'box-weather-data-txt'})[1].text

        navigater_weather_tommorow = navigater_weather_tommorow.replace('晴れ', '晴').replace('くもり', '曇')
        
        # return city, weather, temperature
        return yahoo_weather_today, niftty_weather_today, navigater_weather_today, navigater_weather_tommorow, yahoo_weather_tomorrow, niftty_weather_tomorrow, dt_now
    else:
        return None, None, None

@app.route('/')
def index():
    # city, yahoo_weather_today_0, temperature = scrape_weather()
    yahoo_weather_today, niftty_weather_today,  navigater_weather_today, navigater_weather_tommorow, yahoo_weather_tomorrow, niftty_weather_tomorrow, dt_now = scrape_weather()
    # if city and yahoo_weather_today_0 and temperature:
    if yahoo_weather_today and niftty_weather_today and  navigater_weather_today and yahoo_weather_tomorrow and niftty_weather_tomorrow and navigater_weather_tommorow and dt_now:
        # return render_template('weather.html', city=city, yahoo_weather_today_0=yahoo_weather_today_0, temperature=temperature)
        return render_template('weather.html', yahoo_weather_today=yahoo_weather_today, niftty_weather_today=niftty_weather_today, navigater_weather_today= navigater_weather_today, yahoo_weather_tomorrow=yahoo_weather_tomorrow, niftty_weather_tomorrow=niftty_weather_tomorrow, navigater_weather_tommorow=navigater_weather_tommorow, dt_now=dt_now)
    else:
        error_message = "天気情報を取得できませんでした。"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
