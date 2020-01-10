import requests

URL = "https://e-uczelnia.ue.katowice.pl/wsrest/rest/phz/harmonogram/zajecia"
PARAMS = { "idGrupa":"44247", "idNauczyciel":"0", "widok":"STUDENT", "page":"1", "start":"0", "limit":"500" }

response = requests.get(url = URL, params = PARAMS)
print(response.status_code)
print(response.json())

input("Press any key to proceed...")