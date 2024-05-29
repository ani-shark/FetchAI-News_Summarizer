from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import http.client
import urllib.parse
import json
from googletrans import Translator

# Define Request and Response Models
class Request(Model):
    query: str
    language: str

class Response(Model):
    headline: str
    description: str
    source: str
    url: str

# News search functionality
def search_news(query, categories='-general,-sports', sort='published_desc', limit=10):
    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode({
        'access_key': '0affec6c3b0dc45f76ef99608b54a2b8',
        'keywords': query,
        'categories': categories,
        'sort': sort,
        'limit': limit,
    })

    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    articles = json.loads(data.decode('utf-8'))

    if 'data' not in articles:
        return []

    return articles['data']

def filter_articles(articles, query):
    query_lower = query.lower()
    filtered_articles = []

    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')

        if query_lower in title.lower() or query_lower in description.lower():
            filtered_articles.append({
                'title': title,
                'description': description,
                'url': article.get('url', ''),
                'published_at': article.get('published_at', ''),
                'source': article.get('source', 'Unknown')
            })

    return filtered_articles

# Translation functionality
def translate_text(input_text, target_language):
    translator = Translator()
    translation = translator.translate(input_text, dest=target_language)
    return translation.text

# Create and configure the Agent
SearchAgent = Agent(
    name="SearchAgent",
    port=8000,
    seed="SearchAgent secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(SearchAgent.wallet.address())

@SearchAgent.on_event('startup')
async def agent_details(ctx: Context):
    ctx.logger.info(f'Search Agent Address is {SearchAgent.address}')

@SearchAgent.on_query(model=Request, replies={Response})
async def query_handler(ctx: Context, sender: str, msg: Request):
    ctx.logger.info("Query received")
    try:
        ctx.logger.info(f'Fetching news for query: {msg.query}')
        raw_articles = search_news(msg.query)
        filtered_articles = filter_articles(raw_articles, msg.query)

        if msg.language:
            for article in filtered_articles:
                article['title'] = translate_text(article['title'], msg.language)
                article['description'] = translate_text(article['description'], msg.language)

        if filtered_articles:
            for article in filtered_articles:
                response = Response(
                    headline=article['title'],
                    description=article['description'],
                    source=article['source'],
                    url=article['url']
                )
                await ctx.send(sender, response)
        else:
            await ctx.send(sender, Response(headline="No news found", description="", source="", url=""))
    except Exception as e:
        error_message = f"Error fetching news: {str(e)}"
        ctx.logger.error(error_message)
        await ctx.send(sender, Response(headline="Error", description=error_message, source="", url=""))

if __name__ == "__main__":
    SearchAgent.run()
