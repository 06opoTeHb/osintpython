#Required imports for all of the below to work
import requests
import csv
import os

def reddit(term,sub,sort):
  #Determine if a subreddit was entered. If so, only the sub will be searched. If not, all of reddit will be searched.
  if (sub == ""):
    url = 'https://www.reddit.com/search/.json?q='+term+'&sort='+sort+'&limit=100'
  else:
    url = 'https://www.reddit.com/r/'+sub+'/search/.json?q='+term+'&restrict_sr=1&sort='+sort+'&limit=100'

  #Create the web request, using user agent of our App ID. This will be temporarily stored as text.
  r = requests.get(url, headers = {'User-agent': 'ERG8JCcVZdzgXw'})
  r.text

  #Convert data to JSON
  data = r.json()

  #Open and write CSV from data searched. This will overwrite any existing CSV with the same search term. File will be saved in the directory this program is run.
  with open('reddit_scrape_'+term+'.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Subreddit", "Source"])
    for child in data['data']['children']:
        writer.writerow([child['data']['title'], child['data']['author'], "r/"+child['data']['subreddit'], "https://reddit.com"+child['data']['permalink']])
  
  #Quick Console Log, not necessary to keep 
  print("Complete!")

#Example Function Call with parameters - Term Searched (String), Subreddit (String, can be an empty string), Sort by (String - relevance, hot, top, new, comments)
reddit("COVID-19","","new")