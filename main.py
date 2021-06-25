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
    hits = result['tracks']['hits']
    return render_template('song-results.html', hits=hits, query=songQuery)


@app.route("/recommendations", methods=['POST'])
def postRecommendations():
    key = request.form.get('key')
    result = shazam.get_recommendations(key)
    if 'tracks' in result:
        tracks = result['tracks']
        return render_template('recommendations.html', tracks=tracks)
    else:
        message="No results found"
        return render_template('search.html', message=message)
