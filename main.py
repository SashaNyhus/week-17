from flask import Flask, request, render_template
import shazam


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    message = "Welcome to Song Search"
    return render_template('search.html', message=message)

@app.route("/song-results", methods=['POST'])
def postSearchResults():
    songQuery = request.form.get('query')
    result = shazam.search(songQuery, 0)
    if 'tracks' in result:
        hits = result['tracks']['hits']
        return render_template('song-results.html', hits=hits, query=songQuery)
    else:
        message="No results found"
        return render_template('whoops.html', message=message)


@app.route("/recommendations", methods=['POST'])
def postRecommendations():
    key = request.form.get('key')
    result = shazam.get_recommendations(key)
    if 'tracks' in result:
        tracks = result['tracks']
        tracks = checkForMissingKeys(tracks)
        return render_template('recommendations.html', tracks=tracks)
    else:
        message="No results found"
        return render_template('whoops.html', message=message)


def checkForMissingKeys(tracksList):
    for result in tracksList:
        if 'images' in result:
            continue
        else:
            result['images'] = {'coverart': "https://cdn.pixabay.com/photo/2013/07/13/11/51/cd-158817_1280.png"}
    return tracksList