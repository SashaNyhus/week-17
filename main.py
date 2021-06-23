from flask import Flask, request, render_template
import shazam


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template('search.html')

@app.route("/song-results", methods=['POST'])
def postSearchResults():
    formData = request.form
    print(formData)
    queryDict = formData.items()
    songQuery = queryDict['query']
    print(songQuery)
    result = shazam.search(songQuery, 0)
    hits = result['tracks']['hits']
    return render_template('song-results.html', hits=hits, query=songQuery)
