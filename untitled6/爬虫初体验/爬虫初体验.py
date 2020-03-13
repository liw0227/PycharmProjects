import requests

while True:
    city = input('请输入你需要查询天气的城市，退出请按回车。\n')
    url = f'http://wthrcdn.etouch.cn/weather_mini?city={city}'
    if not city:
        break
    try:
        req = requests.get(url)
    except:
        print('查询失败。')
        break
    dict_city = req.json()
    city_data = dict_city.get('data')
    if city_data:
        city_forecast = city_data['forecast'][0]
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print(f'末能查询该城市{city}')
