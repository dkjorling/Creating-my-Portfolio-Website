import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random
import json
from plotly.subplots import make_subplots
from wordcloud import WordCloud
from plotly.io import templates


# my imports
import dashboards.redditnlp_sentiment_stats as ss


### basic pie chart ###
def basic_pie_chart(player_ref, date):
    sent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
    sent = sent[sent['player_ref'] == player_ref]
    df = sent[sent['datetime'] <= date]
    sentiment_col = df.sentiment
    labels = list(sentiment_col.value_counts().index)
    values = list(sentiment_col.value_counts())
    colors = {'positive':'lightgreen',
                'negative':'lightcoral',
                'neutral':'white'}
    colors = [colors[x] for x in labels]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, showlegend=False)])

    fig.update_traces(hoverinfo='label+percent',
                        textinfo='percent+label',
                        textposition='inside',
                        textfont_size=20,
                        marker=dict(colors=colors,
                                    line=dict(color='#000000',width=2)))
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return fig

### trending sentiment analysis ###
def plot_sentiment_through_time(player_ref, date):
    sent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
    sent = sent[sent['player_ref'] == player_ref]
    sent = sent[sent['datetime'] <= date]
    post_sent = sent[sent['pc'] == 'p']
    comment_sent =  sent[sent['pc'] == 'c']

    ## multiply poss by post_mult and combine post and comment sents w dates
    posts = pd.concat([post_sent, post_sent, post_sent]).reset_index().drop(columns=['index', 'player_ref'])
    posts = posts[['id', 'datetime', 'sentiment']]
    comments = comment_sent[['id', 'datetime', 'sentiment']]
    combined = pd.concat([posts, comments]).set_index('datetime').sort_values('datetime')
    series = pd.Series(combined['sentiment'], index=combined.index)

    # get scores
    co_pos = series[series == 'positive']
    co_neg = series[series == 'negative']
    co_neu = series[series == 'neutral']

    # get index to fillnas
    idx = pd.period_range(min(series.index), max(series.index)).astype('datetime64[ns]') 

    # resample in 3D blocks
    pos_resamp = co_pos.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0).resample('3D').sum()
    neg_resamp = co_neg.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0).resample('3D').sum()
    neu_resamp = co_neu.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0).resample('3D').sum()

    combined_resamp = pd.concat([pos_resamp, neg_resamp, neu_resamp], axis=1)
    combined_resamp.columns = ['positive', 'negative', 'neutral']

    combined_resamp['pos_ratio'] = combined_resamp.positive / (combined_resamp.positive + combined_resamp.negative + combined_resamp.neutral)
    combined_resamp['neg_ratio'] = combined_resamp.negative / (combined_resamp.positive + combined_resamp.negative + combined_resamp.neutral)
    combined_resamp['score'] = combined_resamp.pos_ratio - combined_resamp.neg_ratio


    # Create the figure
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add the positive bars
    fig.add_trace(
        go.Bar(
            x=pos_resamp.index,
            y=pos_resamp,
            name='Positive',
            marker_color='lightgreen',
        ),
        secondary_y=False,
    )

    # Add the negative bars
    fig.add_trace(
        go.Bar(
            x=neg_resamp.index,
            y=-neg_resamp,
            name='Negative',
            marker_color='lightcoral',
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=combined_resamp.index,
            y=combined_resamp['score'],
            name='Score',
            marker_color='#FDB927',
        ),
        secondary_y=True,
    )
    
    custom_template = templates["plotly_dark"]
    custom_template.layout["xaxis"]["showgrid"] = False
    custom_template.layout["yaxis"]["showgrid"] = False

    # Configure the layout
    fig.update_layout(
        title=dict(
            text='Sentiment Through Time'
        ),
        xaxis_title='Date',
        yaxis_title='Number of Impressions',
        barmode='overlay',
        bargap=0,
        barnorm=None,
        height=600,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        template=custom_template,
        plot_bgcolor='#552583',
        paper_bgcolor='#552583',
        yaxis2=dict(showgrid=False, zeroline=False)

    )

    return fig

### wordcloud
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    colors = ['#840DFA', '#FDB927', 'white', '#405ED7', "#FDB927"]
    return random.choice(colors)

def generate_wordcloud(token_dict):
    token_dict = dict(token_dict)
    wordcloud = WordCloud(width=1600,
                            height=400,
                            background_color='#311149',
                            color_func=random_color_func,
                            min_font_size=10).generate_from_frequencies(token_dict)
    #plt.imshow(wordcloud, interpolation='bilinear')
    #plt.axis('off')
    return wordcloud.to_image()


### Top ten words and emojis ###
def plot_top_ten(ent_key, kind='all'):
    with open('assets/entities_with_nicknames.json', 'r') as f:
        entities = json.load(f)
    entities = dict(entities)

    player_ref = entities[ent_key]['full_name']
    names = entities[ent_key]['names']
    tok = ss.get_token_dict(player_ref, kind=kind)
    tok = tok[:50]

    toks = []
    counts = []
    for i, _ in enumerate(tok):
        if tok[i][0] not in names:
            toks.append(tok[i][0])
            counts.append(tok[i][1])

    toks = toks[:10]
    counts = counts[:10]
    toks.reverse()
    counts.reverse()

    fig = go.Figure(
        go.Bar(
            x=counts,
            y=toks,
            orientation='h',
            marker_color='#FDB927'
        )
    )

    fig.update_layout(
        title={
            'text': "Top 10 Frequency Terms",
            'x':0.2,
            'y':0.93
        },
        xaxis=dict(
            title="frequencies",
            showgrid=False,
            showline=False,
        ),
        yaxis=dict(
            tickmode='linear',
            showgrid=False,
            showline=False,
            automargin=True,

        ),
        plot_bgcolor='#552583',
        paper_bgcolor='#552583',
        margin=dict(l=20, r=20, t=50, b=20),
        font=dict(
            color='white',
            family='Montserrat, Helvetica, Arial, sans-serif',
        ),
    )
    return fig


def plot_top_ten_emoji(ent_key, kind='all'):
    with open('assets/entities_with_nicknames.json', 'r') as f:
        entities = json.load(f)
    entities = dict(entities)

    player_ref = entities[ent_key]['full_name']
    emj = ss.get_emoji_dict(player_ref, kind=kind)
    emj = emj[:50]
    
    emjs = []
    counts = []
    for i, _ in enumerate(emj):
        emjs.append(emj[i][0])
        counts.append(emj[i][1])
        
    emjs = emjs[:10]
    counts = counts[:10]
    emjs.reverse()
    counts.reverse()
    
    fig = go.Figure(
            go.Bar(
                x=counts,
                y=emjs,
                orientation='h',
                marker_color='#FDB927'
            )
        )

    fig.update_layout(
        title={
            'text': "Top 10 Frequency Emojis",
            'x':0.2,
            'y':0.93
        },
        xaxis=dict(
            title="frequencies",
            showgrid=False,
            showline=False,
        ),
        yaxis=dict(
            tickmode='linear',
            showgrid=False,
            showline=False,
            automargin=True,
            tickfont=dict(size=20)

        ),
        plot_bgcolor='#552583',
        paper_bgcolor='#552583',
        margin=dict(l=20, r=20, t=50, b=20),
        font=dict(
            color='white',
            family='Montserrat, Helvetica, Arial, sans-serif',
        ),
    )
    return fig


def plot_ytd_player_sent_ranks(date='2023-04-10'):
    names, scores = ss.get_ytd_player_sent_ranks(date=date)
    fig = go.Figure(
            go.Bar(
                x=names,
                y=scores,
                marker_color='#FDB927'
            )
        )

    fig.update_layout(
        title={
            'text': "Player YTD Sentiment",
            'x':0.2,
            'y':0.99
        },
        xaxis=dict(
            showgrid=False,
            showline=False,
        ),
        yaxis=dict(
            #tickmode='linear',
            showgrid=False,
            showline=False,
            automargin=True,
            tickfont=dict(size=20)

        ),
        plot_bgcolor='#552583',
        paper_bgcolor='#552583',
        margin=dict(l=30, r=30, t=50, b=20),
        font=dict(
            color='white',
            family='Montserrat, Helvetica, Arial, sans-serif',
        ),
    )
    return fig

def generate_player_hm():
    with open('assets/entities_with_nicknames.json', 'r') as f:
        entities = json.load(f)
    entities = dict(entities)

    df = pd.read_csv("assets/rm_hm_df.csv", index_col=0)
    df=np.round(df, 3)
    ents = list(entities.keys())[3:21]
    names = [entities[x]['init_name'] for x in ents]
    df.columns = ents
    df.index = ents
    
    heatmap = go.Heatmap(z=df.values,
                     x=df.columns,
                     y=df.index,
                     texttemplate="%{z}",
                     colorscale='YlGnBu',
                     showscale=False,
                     zmax=0.1)

    # Create a Figure object and add the heatmap trace
    fig = go.Figure(data=heatmap)

    fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=10),
            plot_bgcolor='#552583',
            paper_bgcolor='#552583',

    )

    fig.update_xaxes(tickfont=dict(color='white'))
    fig.update_yaxes(tickfont=dict(color='white'))

    return fig