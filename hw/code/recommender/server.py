# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    #title = 
    return render_template('articles.html')


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """

# initialization
#i = sys.argv.index('server:app')
#glove_filename = sys.argv[i+1]
#articles_dirname = sys.argv[i+2]
# glove_filename = '/Users/maneelreddy/Downloads/Data Acquisition/msds692/data/glove.6B.300d.txt'
# articles_dirname = '/Users/maneelreddy/Downloads/Data Acquisition/msds692/data/bbc'

# gloves = load_glove(glove_filename)
# articles = load_articles(articles_dirname, gloves)
app.run(host='0.0.0.0', port=5000)