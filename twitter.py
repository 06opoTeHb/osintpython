# Required imports for all of the below to work
import requests
import csv
import os
import base64


def twitter(term, sort):
    # These keys are critical for use of our Twitter API. They are converted to base64 so that they can be utilized
    # properly by Twitter
    client_key = '1c6McbsduZTm5pAdvz47Jxrfy'
    client_secret = 'nveWqIYoh92mZssYPcueirD5CbLYzhZLaao2G1pVAhGFYIE1kp'
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    # Our base URL is the root that all requests are made to. The auth url is the utilization of our secure
    # application OATH token.
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)

    # Auth headers will be passed with the requested URL in order to be authorized to utlize the Twitter API
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    # This will reach out to Twitter and request our access token at time of application run.
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    # Search parameters (search term [string], result_type [string - mixed, recent, popular], and count. Maximum
    # allowed is 100 results. )
    search_params = {
        'q': term,
        'result_type': sort,
        'count': 100
    }

    # Our specific requested URL alongside the base URL defined above
    url = '{}1.1/search/tweets.json'.format(base_url)

    # Create the web request, using user agent of our App ID. This will be temporarily stored as text.
    r = requests.get(url, headers=search_headers, params=search_params)
    r.text

    # Convert data to JSON
    data = r.json()

    # Open and write CSV from data searched. This will overwrite any existing CSV with the same search term. File
    # will be saved in the directory this program is run.
    with open('twitter_scrape_' + term + '.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Author", "Tweet", "Source"])
        for tweet in data['statuses']:
            writer.writerow(
                [tweet['user']['screen_name'], tweet['text'], "https://twitter.com/i/web/status/" + tweet['id_str']])

    # This section makes a web request similar to above, but will let us know on the backend how many more requests
    # we are allowed to make within a 15 minute period. Twitter limits us to 450 requests per 15 minutes.
    url = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
    r = requests.get(url, headers=search_headers)
    r.text

    data = r.json()

    # This is the output of how many quests we have left. Not necessary to keep, but good info to have for debugging
    # purposes.
    print(data['resources']['search'])


# Example Function Call with parameters - Term Searched (String), Sort by (String - mixed, recent, popular)
twitter("COVID-19", "recent")
