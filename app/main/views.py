from flask import  render_template,redirect,url_for,request
from . import main
from ..models import Sources
from ..requests import get_sources, get_articles


#Views
@main.route('/')
def index():
    
    '''
    
    Views the root page functionality that returns the index page and  it's data
    
    '''
    sources = get_sources()
    print(sources)
    
    title = 'Home - News Updates'
    return render_template('index.html', title = title, sources = sources)

@main.route('/news')
def news():
    
    '''
    Views the news functionality that returns news highlighted details and it's data
    
    '''
    articles = get_articles()
    title = 'Articles - Some of the articles'
    return render_template('news.html', articles=articles, title = title)

