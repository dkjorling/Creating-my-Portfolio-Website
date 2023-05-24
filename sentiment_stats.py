import pandas as pd
import numpy as np
import datetime as dt
import emoji
import re
import nltk
import json
from nltk import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
eng_stopwords = stopwords.words('english') 
### load data ###

def get_sentiment(sent_df, post_multiplier=2.5):
    """
    This function simply takes in sent df and returns average sentiment
    Parameters:
        post_multiplier: how much more should we weight post vs comment? Default = 2.5
    """
    # get post sentiment score
    try:
        post_sent = sent_df[sent_df['pc'] == 'p']
        post_length = post_sent.shape[0]
        try:
            post_prop_pos = post_sent.sentiment.value_counts().loc['positive'] / post_length
        except:
            post_prop_pos = 0
        try:
            post_prop_neg = post_sent.sentiment.value_counts().loc['negative'] / post_length
        except:
            post_prop_neg = 0
        post_score = post_prop_pos - post_prop_neg
        
    except:
        post_score = 0
    
    try:
        comment_sent =  sent_df[sent_df['pc'] == 'c']
        comment_length = comment_sent.shape[0]
        try:
            comment_prop_pos = comment_sent.sentiment.value_counts().loc['positive'] / comment_length
        except:
            comment_prop_pos = 0
        try:
            comment_prop_neg = comment_sent.sentiment.value_counts().loc['negative'] / comment_length
        except:
            comment_prop_neg = 0
        comment_score = comment_prop_pos - comment_prop_neg 
    
    except:
        comment_score = 0
    
    if (post_score == 0) & (comment_score == 0):
        weighted = 0
    else:
        # get weighted score
        num = (post_score * post_length * post_multiplier) + (comment_score * comment_length)
        denom = (post_length * post_multiplier) + comment_length
        weighted = num / denom

    return weighted

def get_sent_other(player_ref, date):
    sent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
    sent = sent[sent['player_ref'] == player_ref]
    sent = sent[sent['datetime'] <= date]

    weighted = get_sentiment(sent)

    return weighted

def get_trending_sentiment(player_ref, date, n=20, n_comp=None):
    if type(n) != int:
        raise TypeError("Invalid Value Type. Must be int")

    sent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
    sent = sent[sent['player_ref'] == player_ref]
    sent = sent[sent['datetime'] <= date]

    date_dt = dt.datetime.strptime(date, "%Y-%m-%d")
    date_dt_first = date_dt - dt.timedelta(days=n)
    date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
    trend = sent[sent['datetime'] > date_first]
    
    sent_score_last_n = get_sentiment(trend)
    
    comp = sent[sent['datetime'] <= date_first]
    if n_comp != None:
        date_dt2 = dt.datetime.strptime(date_first, "%Y-%m-%d")
        date_dt_first2 = date_dt2 - dt.timedelta(days=n_comp)
        date_first2 = dt.datetime.strftime(date_dt_first2, "%Y-%m-%d")
        comp = comp[comp['datetime'] > date_first2]
    sent_score_comp = get_sentiment(comp) 
    diff = (sent_score_last_n - sent_score_comp) / sent_score_comp
    
    return sent_score_last_n, sent_score_comp, diff

def get_trending_sentiment2(sent, date, n=20, n_comp=None):
    if type(n) != int:
        raise TypeError("Invalid Value Type. Must be int")

    date_dt = dt.datetime.strptime(date, "%Y-%m-%d")
    date_dt_first = date_dt - dt.timedelta(days=n)
    date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
    trend = sent[sent['datetime'] > date_first]
    
    sent_score_last_n = get_sentiment(trend)
    
    comp = sent[sent['datetime'] <= date_first]
    if n_comp != None:
        date_dt2 = dt.datetime.strptime(date_first, "%Y-%m-%d")
        date_dt_first2 = date_dt2 - dt.timedelta(days=n_comp)
        date_first2 = dt.datetime.strftime(date_dt_first2, "%Y-%m-%d")
        comp = comp[comp['datetime'] > date_first2]
    sent_score_comp = get_sentiment(comp) 
    diff = (sent_score_last_n - sent_score_comp) / sent_score_comp
    
    return sent_score_last_n, sent_score_comp, diff



def get_rolling_sentiment_score_df(player_ref, date, n=20):
    sent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
    sent = sent[sent['player_ref'] == player_ref]
    sent = sent[sent['datetime'] <= date]

    cols = ['weighted']
    idx = sorted(list(set(sent['datetime'])))
    dfs = pd.DataFrame(columns=cols, index=idx)

    weighted=[]
    for i in idx:
        start = i - dt.timedelta(days=20)
        s = sent[(sent['datetime'] > start) & (sent['datetime'] <= i) ]
        w = get_sentiment(s)
        weighted.append(w)
    dfs['weighted'] = weighted
        
    return dfs


### functions related to word counts ###
def get_top_players(player_ref):
    df = pd.read_csv("assets/rm_hm_df.csv", index_col=0)
    col_name = player_ref + "_refs"
    df = df[col_name]
    t = df.sort_values(ascending=False)
    
    return t


def get_emoji_dict(player_ref, kind="all"):
    if kind not in ['all', 'positive', 'negative']:
        raise ValueError("Invalid kind, must be one of 'all', 'positive', or 'negative' ")
    # allow for use in TeamDate class as well as PlayerDate
    if player_ref=='team': 
        df = pd.read_csv("assets/all_sents/total_sentiment.csv", index_col=0, parse_dates=['datetime'])
        df['body'] = df.body_pr
        df['body'] = df.body.apply(str)

    else:
        psent = pd.read_csv("assets/all_sents/base.csv", index_col=0, parse_dates=['datetime'])
        df = psent[psent['player_ref'] == player_ref]

    if kind == 'positive':
        df = df[df['sentiment'] == 'positive']
    elif kind == 'negative':
        df = df[df['sentiment'] == 'negative']
    else:
        df = df

    emoji_dict = {}
    for t in df.body:
        matches = emoji.emoji_list(t)
        text_emojis = []
        for i, _ in enumerate(matches):
            text_emojis.append(matches[i]['emoji'])
        unique_text_emojis = list(set(text_emojis))
        for emj in unique_text_emojis:
            if emj not in emoji_dict.keys():
                emoji_dict[emj] = 1
            else:
                emoji_dict[emj] += 1
    x = emoji_dict
    sorted_emoji_dict = sorted(x.items(), key=lambda x:x[1], reverse=True)

    return sorted_emoji_dict


def get_token_dict(player_ref, kind="all"):
    if kind not in ['all', 'positive', 'negative']:
        raise ValueError("Invalid kind, must be one of 'all', 'positive', or 'negative' ")

    if player_ref=='team': 
        df = pd.read_csv("assets/all_sents/total_sentiment.csv", index_col=0, parse_dates=['datetime'])
        df['body'] = df.body_pr
        df['body'] = df.body.apply(str)
    else:
        psent = pd.read_csv("assets/all_sents/base.csv", index_col=0, parse_dates=['datetime'])
        df = psent[psent['player_ref'] == player_ref]

    if kind == 'positive':
        df = df[df['sentiment'] == 'positive']
    elif kind == 'negative':
        df = df[df['sentiment'] == 'negative']
    else:
        df = df
    

    token_dict = {}
    for t in df.body:
        tokenized = word_tokenize(t)
        no_stop = [x for x in tokenized if x not in eng_stopwords]
        for t2 in no_stop:
            if t2 in token_dict.keys():
                token_dict[t2] += 1
            else:
                token_dict[t2] = 1
                
    sorted_token_dict = sorted(token_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_token_dict = [x for x in sorted_token_dict if len(re.findall(r"[a-z]+", x[0])) > 0]
    
    return sorted_token_dict



def get_ytd_player_sent_ranks(date='2023-04-10'):
    with open('assets/entities_with_nicknames.json', 'r') as f:
        entities = json.load(f)
    entities = dict(entities)

    sent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
    sent = sent[sent['datetime'] <= date]
    
    scores = {}
    for k in list(entities.keys())[3:21]:
        fn = entities[k]['full_name']
        df = sent[sent['player_ref'] == fn]
        name =  entities[k]['init_name']
        score = get_sentiment(df)
        scores[name] = score
    
    scores_sorted = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    
    names = [scores_sorted[i][0] for i, z in enumerate(scores_sorted)]
    scores = [scores_sorted[i][1] for i, z in enumerate(scores_sorted)]
    
    return names, scores
        






