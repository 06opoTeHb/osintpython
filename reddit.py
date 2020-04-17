import requests
import csv
import os

def reddit(term,sub,sort):
  if (sub == ""):
    url = 'https://www.reddit.com/search/.json?q='+term+'&sort='+sort+'&limit=100'
  else:
    url = 'https://www.reddit.com/r/'+sub+'/search/.json?q='+term+'&restrict_sr=1&sort='+sort+'&limit=100'

  r = requests.get(url, headers = {'User-agent': 'ERG8JCcVZdzgXw'})
  r.text

  data = r.json()

  with open('reddit_scrape_'+term+'.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Subreddit", "Source"])
    for child in data['data']['children']:
        writer.writerow([child['data']['title'], child['data']['author'], "r/"+child['data']['subreddit'], "https://reddit.com"+child['data']['permalink']])
    
  print("Complete!")

reddit("COVID-19","","new")