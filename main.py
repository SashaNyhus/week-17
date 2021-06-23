from flask import Flask, request, render_template
import shazam


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template('search.html')

@app.route("/song-results", methods=['POST'])
def postSearchResults():
    songQuery = request.form.get('query')
    result = shazam.search(songQuery, 0)
    hits = result['tracks']['hits']
    return render_template('song-results.html', hits=hits, query=songQuery)
