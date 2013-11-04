#!/usr/bin/python
"""
The site entry point.
"""

from flask import Flask, render_template
from flask_flatpages import FlatPages


DEBUG=True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)

pages = FlatPages(app)

@app.route('/')
def home():
    return render_template('home.j2')

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)

    return render_template('page.j2', page=page)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
