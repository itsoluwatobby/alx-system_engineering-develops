#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    A recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    Arguments:
        subreddit(str) - passed from the command line
        hot_list(array) - passed fromthe command line
    """
    global after

    if not subreddit or not isinstance(subreddit, str):
        print(None)

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=user_agent, params={'after': after},
                            allow_redirects=False)

    if response.status_code == 200:
        _data = response.json().get("data").get("after")
        if _data is not None:
            after = _data
            recurse(subreddit, hot_list)
        _titles = response.json().get("data").get("children")
        for title_ in _titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
