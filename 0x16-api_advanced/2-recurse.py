#!/usr/bin/python3
"""
    queries a list of all top posts on a given Reddit subreddit
"""
import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])

        if children:
            for child in children:
                title = child.get("data", {}).get("title")
                if title:
                    hot_list.append(title)

            after = data.get("data", {}).get("after")
            if after:
                return recurse(subreddit, hot_list=hot_list)

        return hot_list

    else:
        return None
