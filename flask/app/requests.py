import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None
# Getting the source base url
base_url = None
#Getting the article base url
article_url=None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['API_BASE_URL']

def get_source(thesource):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(thesource,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_sources = None

        if get_source_response['sources']:
            news_source_list = get_source_response['sources']
            news_sources = process_sources(news_source_list)


    return news_sources

def process_sources(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        sources_list: A list that contain various article sources
    Returns :
        news_sources: A list of source objects
    '''
    news_sources = []
    for source_item in source_list:
      
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        

        if name:
            news_object_sources =Source(id,name,description,url)
            news_sources.append(news_object_sources)

    return news_sources

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    news_article_url = article_url.format(category,api_key)

    with urllib.request.urlopen(news_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)


    return article_results


def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        article_list: A list that articles
    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
      
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        link = article_item.get('url')
        poster = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')


        if author:
            articles_object = Article(author,title,description,link,poster,publishedAt)
            article_results.append(articles_object)

    return article_results   