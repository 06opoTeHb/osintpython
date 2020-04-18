# osint project dashboard
# Developed by Matt Hofmann, Simeon Wilson, and Zachary Fleck
import base64
import tkinter as tk
import requests
import csv
import io

# initialize frame
win = tk.Tk()
win.title("OSINT Dashboard")
win.geometry('300x350')
# make window not resizable
win.resizable(0, 0)
rv = tk.StringVar()
tv = tk.StringVar()

# reddit fields assigned to variables outside of reddittext() method
r1 = tk.Label(win, text="Search")
r2 = tk.Label(win, text="Subreddit")
r3 = tk.Label(win, text="")
r4 = tk.Label(win, text="Sort results by")
r5 = tk.Radiobutton(win, text="Hot", variable=rv, value=1, command=rv.set("Hot"))
r6 = tk.Radiobutton(win, text="New", variable=rv, value=2, command=rv.set("New"))
r7 = tk.Radiobutton(win, text="Top", variable=rv, value=3, command=rv.set("Top"))
r8 = tk.Radiobutton(win, text="Controversial", variable=rv, value=4, command=rv.set("Controversial"))
r9 = tk.Radiobutton(win, text="Rising", variable=rv, value=5, command=rv.set("Rising"))
entryterm = tk.StringVar()
entrysub = tk.StringVar()
e1 = tk.Entry(win, textvariable=entryterm)
e2 = tk.Entry(win, textvariable=entrysub)
submitreddit = tk.Button(win, text="Submit",
                         command=lambda: reddit(str(entryterm.get()), str(entrysub.get()), str(rv.get())))


# reddit text entry field
def reddittext():
    # removes twitter residue
    t1.grid_forget()
    t2.grid_forget()
    t3.grid_forget()
    t4.grid_forget()
    t5.grid_forget()
    e1.grid_forget()
    submittwit.grid_forget()
    # places reddit fields on the window
    r1.grid(row=3, column=1)
    r2.grid(row=4, column=1)
    r3.grid(row=5, column=1)
    r4.grid(row=6, column=1)
    r5.grid(row=7, column=1)
    r6.grid(row=8, column=1)
    r7.grid(row=9, column=1)
    r8.grid(row=10, column=1)
    r9.grid(row=11, column=1)
    e1.grid(row=3, column=2)
    e2.grid(row=4, column=2)
    submitreddit.grid(row=12, column=2)


# twitter fields assigned to variables outside of twittertext() method
t1 = tk.Label(win, text="Search")
entrytweet = tk.StringVar()
te1 = tk.Entry(win, textvariable=entrytweet)
t2 = tk.Label(win, text="")
t5 = tk.Label(win, text="Sort results by")
t3 = tk.Radiobutton(win, text="Latest", variable=tv, value=1, command=tv.set("Latest"))
t4 = tk.Radiobutton(win, text="Top", variable=tv, value=2, command=tv.set("Top"))
t5 = tk.Radiobutton(win, text="Mixed", variable=tv, value=3, command=tv.set("Mixed"))
submittwit = tk.Button(win, text="Submit", command=lambda: twitter(str(entrytweet.get()), str(tv.get())))


# twitter text entry field
def twittertext():
    # removes reddit residue
    r1.grid_forget()
    r2.grid_forget()
    r3.grid_forget()
    r4.grid_forget()
    r5.grid_forget()
    r6.grid_forget()
    r7.grid_forget()
    r9.grid_forget()
    r8.grid_forget()
    e1.grid_forget()
    e2.grid_forget()
    submitreddit.grid_forget()
    # places twitter fields on the window
    t1.grid(row=3, column=1)
    te1.grid(row=3, column=2)
    t2.grid(row=4, column=1)
    t5.grid(row=5, column=1)
    t3.grid(row=6, column=1)
    t4.grid(row=7, column=1)
    t5.grid(row=8, column=1)
    submittwit.grid(row=9, column=2)


# label
label1 = tk.Label(win, text="Please select a site").grid(column=1, row=1)
# reddit button
action = tk.Button(win, text="Reddit", bg='#FF4301', activebackground='#FF4301', command=reddittext)
action.grid(column=1, row=2)
action.config(height='4', width='20')
# twitter button
action2 = tk.Button(win, text="Twitter", bg='#00acee', activebackground='#00acee', command=twittertext)
action2.grid(column=2, row=2)
action2.config(height='4', width='20')


def reddit(term, sub, sort):
    # Determine if a subreddit was entered. If so, only the sub will be searched. If not, all of reddit will be searched
    if sub == "":
        url = 'https://www.reddit.com/search/.json?q=' + term + '&sort=' + sort + '&limit=100'
    else:
        url = 'https://www.reddit.com/r/' + sub + '/search/.json?q=' + term + '&restrict_sr=1&sort=' + sort + '&limit=100'

    # Create the web request, using user agent of our App ID. This will be temporarily stored as text.
    r = requests.get(url, headers={'User-agent': 'ERG8JCcVZdzgXw'})
    r.text

    # Convert data to JSON
    data = r.json()

    # Open and write CSV from data searched. This will overwrite any existing CSV with the same search term. File
    # will be saved in the directory this program is run.
    with io.open('reddit_scrape_' + term + '.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Subreddit", "Source"])
        for child in data['data']['children']:
            writer.writerow([child['data']['title'], child['data']['author'], "r/" + child['data']['subreddit'],
                             "https://reddit.com" + child['data']['permalink']])

    # Quick Console Log, not necessary to keep
    print("Complete!")


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
    with io.open('twitter_scrape_' + term + '.csv', 'w', encoding='utf-8') as file:
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

# show gui
win.mainloop()
