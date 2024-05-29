# FetchAI-News_Summarizer
News query and summarizer made using uagents for the IIT Madras FetchAI hackathohn primarily using the Mediastack API for retrieval


Setup
Usage
API Reference
License
Features

Retrieve news articles based on search queries.
Support for multiple languages using the MediaStack API.
Filter news articles to match the search query.
Event-driven architecture using the uAgents framework.

Requirements

Python 3.7+
MediaStack API key
Libraries: uagents, requests, googletrans

Setup

- Clone the repository:
Copy code:
git clone https://github.com/yourusername/news-retrieval-agent.git
cd news-retrieval-agent
- Install dependencies:
Ensure you have pip installed, then run:
pip install -r requirements.txt
-Set up your MediaStack API key:
Replace the placeholder API key in the search_news function within the script with your actual MediaStack API key:
api_key = "your_mediastack_api_key"

Usage

Run the uAgent:

python news_agent.py
Send queries to the uAgent:

You can interact with the agent by sending requests to its endpoint. Use a tool like curl or a REST client to send queries. Example:

curl -X POST http://127.0.0.1:8000/submit -d '{"query": "technology", "language": "en"}'
API Reference

Request Model
query: str - The search query for fetching news articles.
language: str - The language code for the desired language of the news articles (e.g., en for English, fr for French).
Response Model
headline: str - The headline of the news article.
description: str - A brief description of the news article.
source: str - The source of the news article.
url: str - The URL to the full news article.

This project is licensed under the MIT License. See the LICENSE file for details.
