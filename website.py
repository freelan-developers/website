#!/usr/bin/python
"""
The site entry point.
"""
import yaml
import argparse

from flask import Flask, render_template, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer


DEBUG=True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)

pages = FlatPages(app)

freezer = Freezer(app)

def get_pages(page_type, order_by=None):
    """
    Get all the pages of the given type, eventually ordered by the specified criteria.
    """

    if order_by is not None:
        page_list = sorted(pages, key=lambda p: p.meta.get(order_by, 0))
    else:
        page_list = pages

    return [page for page in page_list if page.meta.get('type') == page_type]

def get_menu(name):
    """
    Load a menu.
    """

    return yaml.load(open('menus/%s.yaml' % name))

@app.route('/')
def home():
    return render_template(
        'home.j2',
        menu=get_menu('main'),
        feature_pages=get_pages('feature', 'index'),
    )

@app.route('/download.html')
def download():
    return render_template(
        'download.j2',
        menu=get_menu('main'),
    )

@app.route('/faq.html')
def faq():
    return render_template(
        'faq.j2',
        menu=get_menu('main'),
    )

@app.route('/get_help.html')
def get_help():
    return render_template(
        'get_help.j2',
        menu=get_menu('main'),
    )

@app.route('/configuration_examples.html')
def configuration_examples():
    return render_template(
        'configuration_examples.j2',
        menu=get_menu('main'),
    )

@app.route('/development.html')
def development():
    return render_template(
        'development.j2',
        menu=get_menu('main'),
    )

@app.route('/contact.html')
def contact():
    return render_template(
        'contact.j2',
        menu=get_menu('main'),
    )

@app.route('/donate.html')
def donate():
    return render_template(
        'donate.j2',
        menu=get_menu('main'),
    )

def main():
    """
    The script entry point.
    """

    parser = argparse.ArgumentParser(description='Freelan website generator.')
    parser.add_argument('--freeze', '-f', action='store_true', help='Freezes the website instead of running it.')

    args = parser.parse_args()

    if args.freeze:
        freezer.freeze()
    else:
        app.run(port=5000, host='0.0.0.0')

if __name__ == '__main__':
    main()
