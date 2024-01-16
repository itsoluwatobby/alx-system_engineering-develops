#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetches the first 10 hot posts from the reddit API
    Arguments:
        subreddit(str) - passed from the command line
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    response = requests.get(url, headers=user_agent, params={'limit': 10})
    result = response.json()

    try:
        data = result.get('data').get('children')
        for res in data:
            print(res.get('data').get('title'))
    except Exception:
        print(None)
