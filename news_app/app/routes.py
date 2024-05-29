# app/routes.py

from flask import Blueprint, render_template, request, jsonify
from .ms_query import search_news, filter_articles
from .ms_translation import translate_text
from .models import User, Post

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    language = request.args.get('language', '')
    raw_articles = search_news(query)
    filtered_news_events = filter_articles(raw_articles, query)

    if language:
        for article in filtered_news_events:
            article['title'] = translate_text(article['title'], language)
            article['description'] = translate_text(article['description'], language)

    return jsonify(filtered_news_events)
