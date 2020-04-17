import requests
import csv
import os
import base64

def twitter(term,sort):
  client_key = '1c6McbsduZTm5pAdvz47Jxrfy'
  client_secret = 'nveWqIYoh92mZssYPcueirD5CbLYzhZLaao2G1pVAhGFYIE1kp'
  key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
  b64_encoded_key = base64.b64encode(key_secret)
  b64_encoded_key = b64_encoded_key.decode('ascii')

  base_url = 'https://api.twitter.com/'
  auth_url = '{}oauth2/token'.format(base_url)

  auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  }

  auth_data = {
    'grant_type': 'client_credentials'
  }

  auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
  access_token = auth_resp.json()['access_token']

  search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
  }
  
  search_params = {
    'q': term,
    'result_type': sort,
    'count': 100
  }

  url = '{}1.1/search/tweets.json'.format(base_url)

  r = requests.get(url, headers=search_headers, params=search_params)
  r.text

  data = r.json()

  with open('twitter_scrape_'+term+'.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Author", "Tweet", "Source"])
    for tweet in data['statuses']:
        writer.writerow([tweet['user']['screen_name'], tweet['text'], "https://twitter.com/i/web/status/"+tweet['id_str']])
    
  url = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
  r = requests.get(url, headers=search_headers)
  r.text

  data = r.json()

  print(data['resources']['search'])

twitter("COVID-19","recent")