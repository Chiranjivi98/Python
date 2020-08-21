import json
from urllib.request import urlopen
country=input("Enter country name=>")
mykey="43b5dcfef466ffe09b166e133c1e1b48"
url="https://api.openweathermap.org/"
url=url+"data/2.5/weather?appid="
url=url+mykey+f"&q={country}"
response=urlopen(url)
decoded=response.read().decode('utf-8')
data=json.loads(decoded)
for key,value in data.items():
    print(key,value)
