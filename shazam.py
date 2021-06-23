import requests
import json


def search(song, page):
    url = "https://shazam.p.rapidapi.com/search"
    queryStr = {"term": song, "locale": "en-US", "offset": page, "limit": "5"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=queryStr)
    return json.loads(res.text)


def get_recommendations(songKey):
    url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    queryStr = {"key": songKey, "locale": "en-US"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=queryStr)
    return json.loads(res.text)
