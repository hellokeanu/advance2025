import json
import pandas as pd
import requests
import urllib
from urllib.parse import urlencode, unquote, quote_plus
from urllib.request import urlopen

pd.set_option('display.width', 5000)
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)

Key='835f42a79d2e4e18a5d684b7f97aeedc'
HourlyPresent='/current'
BasicUrl='https://api.weatherbit.io/v2.0'
Hours = 48

def weatherbittest(LAT,LNG):
    params = '?' + urlencode({quote_plus("lat"): str(LAT),
                              quote_plus("lon"): str(LNG),
                              quote_plus("key"): Key,
                              quote_plus("include"): 'minutely'})
    FinalURL = BasicUrl + HourlyPresent + unquote(params)
    req = urllib.request.Request(FinalURL)
    response_body = urlopen(req).read()
    data = json.loads(response_body)

    DF = pd.DataFrame.from_dict(data['data'])

    return DF

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    LAT = 35.002707049416614
    LNG = 125.73350758529737
    Output=weatherbittest(LAT,LNG)

    print(Output)


