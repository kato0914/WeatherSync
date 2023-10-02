from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

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
        yahoo_weather_tomorrow_3 = soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td > small').text
        yahoo_weather_tomorrow_6 = soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td > small').text
        yahoo_weather_tomorrow_9 = soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td > small').text
        yahoo_weather_tomorrow_12 = soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td > small').text
        yahoo_weather_tomorrow_15 = soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td > small').text
        yahoo_weather_tomorrow_18 = soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td + td > small').text
        yahoo_weather_tomorrow_21 = soup.select_one('#yjw_pinpoint_tomorrow > table >tbody > tr + tr > td + td + td + td + td + td + td + td + td > small').text
        
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
        niftty_weather_today_0 = soup.findAll('img')[8].get('alt')
        niftty_weather_today_3 = soup.findAll('img')[9].get('alt')
        niftty_weather_today_6 = soup.findAll('img')[10].get('alt')
        niftty_weather_today_9 = soup.findAll('img')[11].get('alt')
        niftty_weather_today_12 = soup.findAll('img')[12].get('alt')
        niftty_weather_today_15 = soup.findAll('img')[13].get('alt')
        niftty_weather_today_18 = soup.findAll('img')[14].get('alt')
        niftty_weather_today_21 = soup.findAll('img')[15].get('alt')

        print(niftty_weather_today_0)

        #明日の天気
        niftty_weather_tomorrow_0 = soup.findAll('img')[16].get('alt')
        niftty_weather_tomorrow_3 = soup.findAll('img')[17].get('alt')
        niftty_weather_tomorrow_6 = soup.findAll('img')[18].get('alt')
        niftty_weather_tomorrow_9 = soup.findAll('img')[19].get('alt')
        niftty_weather_tomorrow_12 = soup.findAll('img')[20].get('alt')
        niftty_weather_tomorrow_15 = soup.findAll('img')[21].get('alt')
        niftty_weather_tomorrow_18 = soup.findAll('img')[22].get('alt')
        niftty_weather_tomorrow_21 = soup.findAll('img')[23].get('alt')
        
        # 新しいお天気ナビゲーターのURL（八代市の場合）
        url = "https://s.n-kishou.co.jp/w/charge/jikei/jikeid.html?ba=43&code=43202&fla=day"

        # ページのHTMLを取得
        response = requests.get(url)
        # if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 天気情報を抽出
        navigater_weather_today = soup.findAll('p',attrs={'class':'box-weather-data-txt'})[0].text
        navigater_weather_tommorow = soup.findAll('p',attrs={'class':'box-weather-data-txt'})[1].text
        
        # 気象庁のURL（八代市の場合）
        url = "https://www.jma.go.jp/bosai/forecast/#area_type=class20s&area_code=4320200"
        # ページのHTMLを取得
        response = requests.get(url)
        # if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 天気情報を抽出
        # kisyoutyou_weather_today = soup.find('td', class_="forecast-sentence").text

        
        # return city, weather, temperature
        return yahoo_weather_today_0, yahoo_weather_today_3, yahoo_weather_today_6, yahoo_weather_today_9, yahoo_weather_today_12, yahoo_weather_today_15, yahoo_weather_today_18, yahoo_weather_today_21, niftty_weather_today_0, niftty_weather_today_3, niftty_weather_today_6, niftty_weather_today_9, niftty_weather_today_12, niftty_weather_today_15, niftty_weather_today_18, niftty_weather_today_21,  navigater_weather_today, yahoo_weather_tomorrow_0, yahoo_weather_tomorrow_3, yahoo_weather_tomorrow_6, yahoo_weather_tomorrow_9, yahoo_weather_tomorrow_12, yahoo_weather_tomorrow_15, yahoo_weather_tomorrow_18, yahoo_weather_tomorrow_21, niftty_weather_tomorrow_0, niftty_weather_tomorrow_3, niftty_weather_tomorrow_6, niftty_weather_tomorrow_9, niftty_weather_tomorrow_12, niftty_weather_tomorrow_15, niftty_weather_tomorrow_18, niftty_weather_tomorrow_21, navigater_weather_tommorow, dt_now
    else:
        return None, None, None

@app.route('/')
def index():
    # city, yahoo_weather_today_0, temperature = scrape_weather()
    yahoo_weather_today_0, yahoo_weather_today_3, yahoo_weather_today_6, yahoo_weather_today_9, yahoo_weather_today_12, yahoo_weather_today_15, yahoo_weather_today_18, yahoo_weather_today_21, niftty_weather_today_0, niftty_weather_today_3, niftty_weather_today_6, niftty_weather_today_9, niftty_weather_today_12, niftty_weather_today_15, niftty_weather_today_18, niftty_weather_today_21,  navigater_weather_today, yahoo_weather_tomorrow_0, yahoo_weather_tomorrow_3, yahoo_weather_tomorrow_6, yahoo_weather_tomorrow_9, yahoo_weather_tomorrow_12, yahoo_weather_tomorrow_15, yahoo_weather_tomorrow_18, yahoo_weather_tomorrow_21, niftty_weather_tomorrow_0, niftty_weather_tomorrow_3, niftty_weather_tomorrow_6, niftty_weather_tomorrow_9, niftty_weather_tomorrow_12, niftty_weather_tomorrow_15, niftty_weather_tomorrow_18, niftty_weather_tomorrow_21, navigater_weather_tommorow, dt_now = scrape_weather()
    # if city and yahoo_weather_today_0 and temperature:
    if yahoo_weather_today_0 and yahoo_weather_today_3 and yahoo_weather_today_6 and yahoo_weather_today_9 and yahoo_weather_today_12 and yahoo_weather_today_15 and yahoo_weather_today_18 and yahoo_weather_today_21 and niftty_weather_today_0 and niftty_weather_today_3 and niftty_weather_today_6 and niftty_weather_today_9 and niftty_weather_today_12 and niftty_weather_today_15 and niftty_weather_today_18 and niftty_weather_today_21 and  navigater_weather_today and yahoo_weather_tomorrow_0 and yahoo_weather_tomorrow_3 and yahoo_weather_tomorrow_6 and yahoo_weather_tomorrow_9 and yahoo_weather_tomorrow_12 and yahoo_weather_tomorrow_15 and yahoo_weather_tomorrow_18 and yahoo_weather_tomorrow_21 and niftty_weather_tomorrow_0 and niftty_weather_tomorrow_3 and niftty_weather_tomorrow_6 and niftty_weather_tomorrow_9 and niftty_weather_tomorrow_12 and niftty_weather_tomorrow_15 and niftty_weather_tomorrow_18 and niftty_weather_tomorrow_21 and navigater_weather_tommorow and dt_now:
        # return render_template('weather.html', city=city, yahoo_weather_today_0=yahoo_weather_today_0, temperature=temperature)
        return render_template('weather.html', yahoo_weather_today_0=yahoo_weather_today_0, yahoo_weather_today_3=yahoo_weather_today_3, yahoo_weather_today_6=yahoo_weather_today_6, yahoo_weather_today_9=yahoo_weather_today_9, yahoo_weather_today_12=yahoo_weather_today_12, yahoo_weather_today_15=yahoo_weather_today_15, yahoo_weather_today_18=yahoo_weather_today_18, yahoo_weather_today_21=yahoo_weather_today_21, niftty_weather_today_0=niftty_weather_today_0, niftty_weather_today_3=niftty_weather_today_3, niftty_weather_today_6=niftty_weather_today_6, niftty_weather_today_9=niftty_weather_today_9, niftty_weather_today_12=niftty_weather_today_12, niftty_weather_today_15=niftty_weather_today_15, niftty_weather_today_18=niftty_weather_today_18, niftty_weather_today_21=niftty_weather_today_21, navigater_weather_today= navigater_weather_today, yahoo_weather_tomorrow_0=yahoo_weather_tomorrow_0, yahoo_weather_tomorrow_3=yahoo_weather_tomorrow_3, yahoo_weather_tomorrow_6=yahoo_weather_tomorrow_6, yahoo_weather_tomorrow_9=yahoo_weather_tomorrow_9, yahoo_weather_tomorrow_12=yahoo_weather_tomorrow_12, yahoo_weather_tomorrow_15=yahoo_weather_tomorrow_15, yahoo_weather_tomorrow_18=yahoo_weather_tomorrow_18, yahoo_weather_tomorrow_21=yahoo_weather_tomorrow_21, niftty_weather_tomorrow_0=niftty_weather_tomorrow_0, niftty_weather_tomorrow_3=niftty_weather_tomorrow_3, niftty_weather_tomorrow_6=niftty_weather_tomorrow_6, niftty_weather_tomorrow_9=niftty_weather_tomorrow_9, niftty_weather_tomorrow_12=niftty_weather_tomorrow_12, niftty_weather_tomorrow_15=niftty_weather_tomorrow_15, niftty_weather_tomorrow_18=niftty_weather_tomorrow_18, niftty_weather_tomorrow_21=niftty_weather_tomorrow_21, navigater_weather_tommorow=navigater_weather_tommorow, dt_now=dt_now)
    else:
        error_message = "天気情報を取得できませんでした。"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
