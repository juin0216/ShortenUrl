import requests

def shorturl(url):
    headers = {'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36'}
    data = {'url' : url, 'multiple' : '0'}
    res = requests.post('https://han.gl/shorten', data=data, headers=headers)

    return res.json()['short']

  //shorturl('https://www.google.com')
