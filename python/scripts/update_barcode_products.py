import csv, json
import requests

X = []
Y = []
with open('update_products.csv', 'rb') as data:
    reader = csv.reader(data, delimiter=',')
    headers = {'content-type' : 'application/x-www-form-urlencoded', 'Bearer' : 'Token Diego'}
    params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
    for line in reader:
        # url = "https://v7-dot-barzinganow.appspot.com/api/product/"
        url = "http://localhost:8080/api/product/"
        url += line[0]
        url += "/bar_code"
        data = {"bar_code": str(line[3])}
        print data
        print requests.put(url, data=data, headers=headers, params=params)