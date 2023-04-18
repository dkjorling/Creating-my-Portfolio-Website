import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
import warnings
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from dash import Dash, html, dcc, Input, Output, register_page, callback
from dash_bootstrap_templates import load_figure_template

# my imports
import imdb_clean as ic
import warnings
warnings.filterwarnings('ignore')
###############################################
### load/clean data ###
data = pd.read_csv('assets/box_office_data_final.csv')
data = ic.clean(data)
sentiment = ic.sentiment(data)
###############################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__)
load_figure_template('LUMEN')
###############################################
### Begin Page Layout ###

layout = html.Div([
    html.Div(
        children = dcc.Dropdown(
        id = 'dropdown1',
        options = ['From'] + sorted(data['year'].unique()),
        value = 'From'),
        style = {'width':'33%', 'display':'inline-block'}
    ),

    html.Div(
        children = dcc.Dropdown(
        id = 'dropdown2',
        options = ['To'] + sorted(data['year'].unique()),
        value = 'To'),
        style = {'width':'34%', 'display':'inline-block'}
    ),

    html.Div(
        children = dcc.Dropdown(
        id = 'dropdown3',
        options = ['All Genres'] + sorted(data['genre'].unique()),
        value = 'All Genres'),
        style = {'width':'33%', 'display':'inline-block'}
    ),

    html.Div(
        children = dcc.Graph(id = 'graph1')
    ),

    html.Div(
        children = [dcc.Graph(id = 'graph2')],
        style = {'width':'50%', 'display':'inline-block'}
    ),

    html.Div(
        children = [dcc.Graph(id = 'graph3')],
        style = {'width':'50%', 'display':'inline-block'}
    ),

    html.Div(
        children = [dcc.Graph(id = 'graph4')],
        style = {'width':'33%', 'display':'inline-block'}
    ),

    html.Div(
        children = [dcc.Graph(id = 'graph5')],
        style = {'width':'34%', 'display':'inline-block'}
    ),

    html.Div(
        children = [dcc.Graph(id = 'graph6')],
        style = {'width':'33%', 'display':'inline-block'}
    )
        
])

##################################################################################
### define callbacks ###
@callback(
    Output('graph1', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'))

def update_graph1(year_from, year_to, genre):
    if (year_from == 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data
    if (year_from != 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from)]
    if (year_from == 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] <= year_to)]
    if (year_from == 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to)]
    if (year_from == 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] <= year_to) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to) &
                             (data['genre'] == genre)]
      
    trace = px.histogram(
        x = filtered_data['imDbRating'],
        title = "Distribution of IMDb Ratings",
        labels = {'x':'IMDb Ratings',
                  'count':'Count'}
    )
    
    return trace


@callback(
    Output('graph2', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'))

def update_graph2(year_from, year_to, genre):
    if (year_from == 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = sentiment
    if (year_from != 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = sentiment[(sentiment['year'] >= year_from)]
    if (year_from == 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = sentiment[(sentiment['year'] <= year_to)]
    if (year_from == 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = sentiment[(sentiment['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = sentiment[(sentiment['year'] >= year_from) & (sentiment['year'] <= year_to)]
    if (year_from == 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = sentiment[(sentiment['year'] <= year_to) & (sentiment['genre'] == genre)]
    if (year_from != 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = sentiment[(sentiment['year'] >= year_from) & (sentiment['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = sentiment[(sentiment['year'] >= year_from) & (sentiment['year'] <= year_to) &
                             (sentiment['genre'] == genre)]
    
    trace = px.pie(
        filtered_data, values = 'score', names = 'sentiment', color = 'sentiment',
        color_discrete_map = {'Positive':'lightgreen',
                              'Negative':'red'},
        title = "Plot Sentiment"
    )
        
    return trace


@callback(
    Output('graph3', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'))

def update_graph3(year_from, year_to, genre):
    if (year_from == 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data
    if (year_from != 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from)]
    if (year_from == 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] <= year_to)]
    if (year_from == 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to)]
    if (year_from == 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] <= year_to) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to) &
                             (data['genre'] == genre)]

    '''
    In order to make the line graph, I had to separte the positive plot movies from
    the negative plot movies and then combine the 2 dataframes in long format.
    '''
    
    positive = filtered_data[filtered_data['positive'] > filtered_data['negative']].groupby(
        ['year'])['imDbRating'].mean().reset_index()
    
    negative = filtered_data[filtered_data['positive'] < filtered_data['negative']].groupby(
        ['year'])['imDbRating'].mean().reset_index()
    
    positive['Sentiment'] = 'Positive'
    negative['Sentiment'] = 'Negative'
    
    positive_negative = pd.concat([positive, negative]).reset_index()
        
    trace = px.line(
        x = positive_negative['year'],
        y = positive_negative['imDbRating'],
        color = positive_negative['Sentiment'],
        color_discrete_map = {'Positive':'green',
                              'Negative':'red'},
        title = "IMDb Rating Over Time by Sentiment",
        labels = {'x':'Time',
                  'y':'IMDb Rating'}
    )
    
    return trace


@callback(
    Output('graph4', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'))

def update_graph4(year_from, year_to, genre):
    if (year_from == 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data
    if (year_from != 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from)]
    if (year_from == 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] <= year_to)]
    if (year_from == 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['genres'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to)]
    if (year_from == 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] <= year_to) & (data['genres'] == genre)]
    if (year_from != 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['genres'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to) &
                             (data['genres'] == genre)]
        
    trace = px.bar(
        x = filtered_data['genres'].value_counts().sort_values(ascending=True).tail(10),
        y = filtered_data['genres'].value_counts().sort_values(ascending=True).tail(10).index,
        title = "Most Popular Genres",
        labels = {'x':'Count',
                  'y':'Genre'}
    )
    
    return trace


@callback(
    Output('graph5', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'))

def update_graph5(year_from, year_to, genre):
    if (year_from == 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data
    if (year_from != 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from)]
    if (year_from == 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] <= year_to)]
    if (year_from == 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to)]
    if (year_from == 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] <= year_to) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to) &
                             (data['genre'] == genre)]
    
    '''
    For each movie, the keywords are in a list. Using the .explode() function is a quick way
    to make each row a unique movie-keyword pairing. From there, I removed stop words and
    punctuation.
    '''
    words = filtered_data['keywords'].astype(str).apply(lambda x: x.split(',')).explode().reset_index()

    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~.'''
    words = words[~words['keywords'].isin(word_tokenize(punc))].reset_index().drop(
        'level_0', axis=1)

    trace = px.bar(
        x = words['keywords'].value_counts().head(10).sort_values(),
        y = words['keywords'].value_counts().head(10).sort_values().index,
        title = "Most Popular Keywords",
        labels = {'x':'Count',
                  'y':'Keywords'}
    )
    
    return trace


@callback(
    Output('graph6', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'))

def update_graph6(year_from, year_to, genre):
    if (year_from == 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data
    if (year_from != 'From') & (year_to == 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from)]
    if (year_from == 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] <= year_to)]
    if (year_from == 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre == 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to)]
    if (year_from == 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] <= year_to) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to == 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['genre'] == genre)]
    if (year_from != 'From') & (year_to != 'To') & (genre != 'All Genres'):
        filtered_data = data[(data['year'] >= year_from) & (data['year'] <= year_to) &
                             (data['genre'] == genre)]
        
    trace = px.scatter(
        x = filtered_data['imDbRating'],
        y = filtered_data['metacriticRating']/10,
        title = "Do IMDb and Metacritic Rate the Same?",
        labels = {'x':'IMDb Rating',
                  'y':'Metacritic Rating'}
    )
    
    return trace
