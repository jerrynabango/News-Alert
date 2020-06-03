import urllib.request,json
from .models import Sources, updates
from datetime import datetime
from config import Config
#getting api_key
# Sources = sources.Sources
# articles = articles.articles

#getting the api key
api_key = None

#getting the sources and the articles base api url


api_key = Config.NEWS_API_KEY
base_url = Config.SOURCES_BASE_URL
articles_url = Config.ARTICLES_BASE_URL

# get_sources_url = base_url.format(base_url,'70a98de97c2841f7895b69f5d131247e')
    
 
 

def get_sources():
	'''
	Function that gets the json response to our url request
	'''
	# get_sources_url = base_url.format(base_url,'70a98de97c2841f7895b69f5d131247e')
	# print(get_sources_url)

	with urllib.request.urlopen(base_url + '70a98de97c2841f7895b69f5d131247e') as url:
     
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results

  

def process_sources(sources_list):
    
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news source details

    Returns :
        source_results: A list of source objects
        
    '''
    
    source_results = []
    
    for source_item in sources_list:
        
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')
        
        if url:
            source_object = Sources(id,name,description,url,category,country,language)
            source_results.append(source_object)
            
        
    return source_results

def get_articles():
	'''
	Function that processes the articles and returns a list of articles objects
	'''

	with urllib.request.urlopen(articles_url+ '') as url:
		articles_results = json.loads(url.read())


		articles_object = None
		if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])

	return articles_object


def process_articles(articles_list):
	'''
	'''
	articles_object = []
	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	
		


	return articles_object
        