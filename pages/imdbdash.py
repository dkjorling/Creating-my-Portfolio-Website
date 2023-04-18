import pandas as pd
import numpy as np
import torch
import json
import warnings
from torch.utils.data import DataLoader
from dash import html, dcc, Input, Output, register_page, callback
from dash_bootstrap_templates import load_figure_template

# my imports
import imdb_clean as ic
import Nrl as nrl
from dash_helpers import dashboard_navbar, page_bottom
warnings.filterwarnings('ignore')
###############################################
### load/clean data ###
data = pd.read_csv('assets/box_office_data_final.csv')
data = ic.clean(data)
###############################################
### load/define other necessary data ###
with open('assets/input_dict.json', 'r') as j:
     input_dict = json.loads(j.read())
     
# Release month dict
month_dict = {'January': 'nov_to_jan',
              'February': 'feb_to_apr',
              'March': 'feb_to_apr',
              'April': 'feb_to_apr',
              'May': 'may_to_july',
              'June': 'may_to_july',
              'July': 'may_to_july',
              'August': 'aug_to_oct',
              'September': 'aug_to_oct',
              'October': 'aug_to_oct',
              'November': 'nov_to_jan',
              'December': 'nov_to_jan'}

genre_dict = {'Action': 'Action/Adventure',
              'Adventure': 'Action/Adventure',
              'Crime': 'Thriller',
              'Comedy': 'Comedy',
              'Horror': 'Thriller',
              'Thriller': 'Thriller',
              'Drama': 'Drama',
              'Romance': 'Misc',
              'Fantasy': 'Action/Adventure',
              'Sci-Fi': 'Action/Adventure',
              'Family': 'Misc',
              'Mystery': 'Thriller',
              'Biography': 'Drama',
              'Animation': 'Misc',
              'History': 'Drama',
              'Music': 'Drama',
              'Sport': 'Drama',
              'War': 'Drama',
              'Musical': 'Misc',
              'Western': 'Drama',
              'Film-Noir': 'Misc'}

co_size_dict = {'Small': 'small',
               'Medium': 'medium',
               'Large': 'large',
               'Giant': 'giant'}


### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/imdb/dashboard')
load_figure_template('FLATLY')
###############################################
### Begin Page Layout ###

layout = html.Div(
            children=[
                dashboard_navbar(
                        'imdb',
                        '#e8b20c',
                        'black',
                        '#e8b20c'
                ),
                html.H1(
                    'Movie Box Office Profit Predictor',
                    style = {
                        'textAlign':'center',
                        'color':'#e8b20c',
                        'background-color':'black',
                        'padding':'10px',
                        'font-weight':'bold'
                        }
                ),
                html.Div(
                    children=[
                        html.H5(
                            "Budget",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px'
                            }
                        ),
                        html.H5(
                            "Runtime",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px',
                                'padding':'0px 0px 0px 185px'
                            }
                        ),
                        html.H5(
                            "Release Month",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px',
                                'padding':'0px 0px 0px 45px'
                            }
                        ),
                        html.H5(
                            "Production Co. Size",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px',
                                'padding':'0px 0px 0px 15px'
                            }
                        ),
                        html.H5(
                            "Genre",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px',
                                'padding':'0px 0px 0px 25px'
                            }
                        ),
                    ],
                    style={
                        'text-Align':'left',
                        'padding':'5px 0px 5px 45px'
                    }
                ),
                html.Div(
                    children=[
                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown1',
                            options = ['${:,.2f}'.format(i) for i in range(10000000, 1100000000, 10000000)],
                            value = '$50,000,000',
                            placeholder = 'Enter Budget',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                'width':'240px',
                                'display':'inline-block',
                                'margin':'0px 10px 0px 0px',
                                'textAlign':'left',
                            }
                        ),

                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown2',
                            options = list(range(30, 240, 10)),
                            value = 120,
                            placeholder = 'Runtime',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                'width':'120px',
                                'display':'inline-block',
                                'padding':'0px 10px 0px 0px',
                                'textAlign':'left'
                            }
                        ),

                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown3',
                            options = list(month_dict.keys()),
                            value = 'July',
                            placeholder = 'Release Month',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                'width':'150px',
                                'display':'inline-block',
                                'padding':'0px 10px 0px 0px',
                                'textAlign':'left'
                            }
                        ),

                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown4',
                            options = list(co_size_dict.keys()),
                            value = 'Large',
                            placeholder = 'Company Size',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                'width':'200px',
                                'display':'inline-block',
                                'padding':'0px 10px 0px 0px',
                                'textAlign':'left'
                            }
                        ),
                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown5',
                            options = sorted(list(genre_dict.keys())),
                            value = 'Action',
                            placeholder = 'Enter Genre',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                    'width':'178px',
                                    'display':'inline-block',
                                    'padding':'0px 10px 0px 0px',
                                    'textAlign':'left'
                            }
                        ),
                    ],
                    style={
                        'padding':'5px 0px 5px 45px',
                        'textAlign':'left'
                    }
                ),
                html.Div(
                    children=[
                        html.H5(
                            "First Star Actor/Actress",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px',
                            }
                        ),
                        html.H5(
                            "Second Star Actor/Actress",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px',
                                'padding':'0px 0px 0px 95px'
                            }
                        ),
                        html.H5(
                            "Director",
                            style={
                                'color':'silver',
                                'display':'inline-block',
                                'font-size':'20px',
                                'padding':'0px 0px 0px 65px'
                            }
                        ),
                    ],
                    style={
                        'text-Align':'left',
                        'padding':'5px 0px 5px 45px'
                    }
                ),
                html.Div(
                    children=[    
                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown6',
                            options = ic.sortSur(list(input_dict['st'].keys())),
                            value = 'Emma Stone',
                            placeholder = 'Choose First Star',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                    'width':'300px',
                                    'display':'inline-block',
                                    'padding':'0px 10px 0px 0px',
                                    'textAlign':'left'
                            }
                        ),
                                
                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown7',
                            options = ic.sortSur(list(input_dict['st'].keys())),
                            value = 'Leonardo DiCaprio',
                            placeholder = 'Choose Second Star',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                    'width':'300px',
                                    'display':'inline-block',
                                    'padding':'0px 10px 0px 0px',
                                    'textAlign':'left'
                            }
                        ),
                                
                        html.Div(
                            children = dcc.Dropdown(
                            id = 'dropdown8',
                            options = ic.sortSur(list(input_dict['dir'].keys())),
                            value = 'Christopher Nolan',
                            placeholder = 'Choose Director',
                            style={
                                'border':'1px solid #e8b20c',
                                'border-radius':'0%'
                            }
                            ),
                            style = {
                                    'width':'300px',
                                    'display':'inline-block',
                                    'padding':'0px 10px 0px 0px',
                                    'textAlign':'left'
                            }
                        ),
                    ],
                    style={
                        'padding':'5px 0px 5px 45px',
                        'textAlign':'left'
                    }
                ),
                        
                html.H3(
                    'Your movie will make approximately:\n',
                    style = {
                        'textAlign':'center',
                        'color':'silver',
                        'font-weight':'bold'
                    }
                ),

                html.H3(
                    id = 'prediction1_output',
                    style = {
                        'textAlign':'center',
                        'color':'#e8b20c',
                        'font-weight':'bold',
                        'font-size':'40px'
                    }
                ),
                html.Div(
                    style={
                        'height':'300px',
                    }
                ),
                html.Div(
                    style={
                        'height':'300px',
                        'background-color':'silver'
                    }
                ),
                page_bottom(col1='silver', col2='silver', col3='black'),
            ],
            
            style={
                'background-color':'black',
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
            }
        )
        
        
##################################################################################
### define callbacks ###
   
@callback(
    Output('prediction1_output', 'children'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'),
    Input('dropdown4', 'value'),
    Input('dropdown5', 'value'),
    Input('dropdown6', 'value'),
    Input('dropdown7', 'value'),
    Input('dropdown8', 'value'))

def update_prediction(budget, runtime, release_month, company_size,
                      genre, star1, star2, director):
    """This function takes 8 user-defined inputs and outputs estimated budget through a trained NN"""
    
    numerical_df = pd.DataFrame(np.zeros((1, 5)),
                                columns=['runtime', 'dir_pop', 'wr_pop', 'star_power', 'adj_budget'])
    
    budget = float(budget.replace('$','').replace(',',''))
    #note: must manually scale since no referfence point in data
    numerical_df['runtime'] = (float(runtime) - 110.71) / 19.16
    numerical_df['dir_pop'] = (float(input_dict['dir'][director]) - 5.74) / 5.18
    numerical_df['wr_pop'] = 0.01 # this is avg value
    numerical_df['star_power'] = float(input_dict['st'][star1] + input_dict['st'][star2] + 7) # model uses 3 stars avg val 7
    numerical_df['star_power'] = (numerical_df['star_power'] - 20.95) / 13.50
    numerical_df['adj_budget'] = (float(budget) - 6.876731e+07) / 6.578914e+07
    
    # convert to numpy and scale the numericals
    normalized = numerical_df.values

    
    # one-hot the rest: ratings, genre, rp, cosize in that order
    # ratings
    ratings = np.array([0, 1, 0]).reshape(1, 3)
    
    # genre
    genres = pd.DataFrame(np.zeros((1, 5)), columns = ['Action/Adventure', 'Comedy', 'Drama', 'Misc', 'Thriller'])
    genre_model = genre_dict[genre]
    genres[genre_model] = 1.0
    
    # release period
    rp = pd.DataFrame(np.zeros((1, 4)), columns = ['aug_to_oct', 'feb_to_apr', 'may_to_july', 'nov_to_jan'])
    release_period = month_dict[release_month]
    rp[release_period] = 1.0
    
    # cosize
    cs = pd.DataFrame(np.zeros((1, 4)), columns = ['giant', 'large', 'medium', 'small'])
    cosize = co_size_dict[company_size]
    cs[cosize] = 1

    features = np.concatenate([normalized,
                               ratings,
                               genres.values,
                               rp.values,
                               cs.values],
                             axis=1)
    
    targ = np.random.rand(1, 1)
    
    ### Feed to NN ###
    
    model = torch.load('assets/neural_net.pth')
    
    td = nrl.imdb_Dataset(features, targ)
    dloader = DataLoader(td,
                         batch_size=1,
                         shuffle=False)

    output = nrl.predict(dloader, model=model).numpy()[0][0]
    std = data['gross_profit_adj'].std()
    mean = data['gross_profit_adj'].mean()
    output = (output * std) + mean
    
    return '${:,.2f}'.format(output)

