import pandas as pd
import numpy as np
import json
import re
import datetime as dt
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datetime as dt
import random
import json
import re
from plotly.subplots import make_subplots
from wordcloud import WordCloud
from plotly.io import templates

# my imports
import sentiment_stats as ss

### load data ###
path = "assets/"
# player dict with names and ids 
f = open(path + 'players.json')
player_dict = json.load(f)
# transaction dict with transaction info for players
f = open(path + 'transactions.json')
transactions_dict = json.load(f)
# teams dict contains lakers and teams laker players played for in 2022-23 w id and all game ids
f = open(path + 'teams.json')
team_dict = json.load(f)

def load_json_file(file, path=path):
    f = open(path + file)
    return json.load(f)


def find_nearest_date(df, column, date):
    """
    Given a df with a string date column, returns string date of nearest date that does not go past that date.
    Note: date must be inh '%Y-%m-%d' format
    Parameters:
        df: dataframe to reference
        column: df column to reference
        date: string format date 
    """
    
    dt_date = dt.datetime.strptime(date, "%Y-%m-%d") # define date in dt format
    
    string_dates = list(df[column])
    dates = list(pd.to_datetime(df[column]))
    diffs = [dt_date - x for x in dates]
    idx = diffs.index(min([d for d in diffs if d.days >=0]))
    date = string_dates[idx]
    
    return date

def gmas(stat, stat_df):
    """
    Advanced stats are calculated using number of possessions so simple mean will not \
    calculate proper value. This function takes possessions into account to return the \
    correct average advanced stat
    """
    product = stat_df[stat] * stat_df['POSS']
    mean_stat = product.sum() / stat_df['POSS'].sum()
    return mean_stat


def get_cum_stats_any(df, x=None, n=None, laker_only=False, team=False):
        """
        Returns player's cumulative stats throughout season. /
        Can specify last x games/or n days and also whether to include all stats or laker only
        Parameters:
            x_games: if set, gets cum stats last x games; default=None
            n_days: if set, gets cum stats last n days; default=None
        """
        if (x != None) & (n != None):
            raise ValueError("Can only specify either x games or n days, not both!")
        
        # define stats
        if laker_only:
            df = df[df['TEAM_ABBREVIATION'] == 'LAL']

            
        # drop games with 0 minutes played:
        df = df[~df['MIN'].isna()].reset_index().drop(columns=("index"))
                    
        last_date = df['GAME_DATE'].iloc[-1]
        
        # filter last x games if x specified
        if x != None:
            if type(x) != int:
                raise TypeError("Invalid Value Type. Must be int")
            idx_first = df.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            df = df.iloc[idx_first:]
            
        # filter last n days if n specified
        elif n != None:
            if type(n) != int:
                raise TypeError("Invalid Value Type. Must be int")
            date_dt = dt.datetime.strptime(last_date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            df = df[df['GAME_DATE'] > date_first]
            
        
        # drop columns that are not cumulative
        drop_columns = ['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY',
                        'PLAYER_ID', 'PLAYER_NAME', 'FG_PCT', 'FG3_PCT', 'FT_PCT',
                        'GAME_DATE', 'MATCHUP', 'WL', 'TM_TOV_PCT']
        
        df = df.drop(columns=drop_columns)
        
        
        
        # filter our advanced columns that use special mean function
        adv_cols = list(df.columns[16:36])
        remove = ['AST_TOV', 'NET_RATING', 'E_NET_RATING', 'POSS']
        adv_cols = [x for x in adv_cols if x not in remove]
        
        
        # calculate mean traditional stats
        totals = df.sum(axis=0)
        totals['GAMES'] = df.shape[0]
        totals['FG_PCT'] = totals.FGM / totals.FGA
        totals['FG3_PCT'] = totals.FG3M / totals.FG3A
        totals['FT_PCT'] = totals.FTM / totals.FTA
        
        # calculate mean advanced stats
        for col in adv_cols:
            totals[col] = gmas(col, df)
            
            
        # calc remaining adv stats
        totals.NET_RATING = totals.OFF_RATING - totals.DEF_RATING
        totals.E_NET_RATING = totals.E_OFF_RATING - totals.E_DEF_RATING
        totals.AST_TOV = totals.AST / totals.TO
        
        
        # format data and return
        for i in totals.index:
            if "PCT" in i:
                totals.loc[i] = totals.loc[i] * 100
            elif i == "PIE":
                totals.loc[i] = totals.loc[i] * 100
        return totals.round(1)
    
    
def get_per_game_stats_any(df, x=None, n=None, laker_only=False, team=False):
    cum_stats = get_cum_stats_any(df=df, x=x, n=n, laker_only=laker_only)

    divide_col_index = list(cum_stats.index[:16])
    divide_col_index.append("POSS") 
    divide_col_index.append("MIN") 

    for idx in divide_col_index:
        name = idx + "_PG"
        cum_stats[name] = cum_stats[idx] / cum_stats.GAMES
        cum_stats.drop(index=idx, inplace=True)

    per_game = cum_stats

    return per_game.round(1)

def get_per_m_minutes_stats_any(df, m=36, x=None, n=None, laker_only=False, team=False):
    cum_stats = get_cum_stats_any(df=df, x=x, n=n)

    divide_col_index = list(cum_stats.index[:16])
    divide_col_index.append("POSS") 
    divide_col_index.append("MIN") 
    total_min = cum_stats.MIN

    for idx in divide_col_index:
        name = idx + "_P{}M".format(m)
        cum_stats[name] = cum_stats[idx] / total_min * m
        cum_stats.drop(index=idx, inplace=True)

    per_minutes = cum_stats

    return per_minutes.round(1)
        
def get_per_p_possessions_stats_any(df, p=100, x=None, n=None, laker_only=False, team=False):
    cum_stats = get_cum_stats_any(df=df, x=x, n=n)

    divide_col_index = list(cum_stats.index[:16])
    divide_col_index.append("POSS") 
    divide_col_index.append("MIN") 
    total_poss = cum_stats.POSS

    for idx in divide_col_index:
        name = idx + "_P{}P".format(p)
        cum_stats[name] = cum_stats[idx] / total_poss * p
        cum_stats.drop(index=idx, inplace=True)

    per_possessions = cum_stats

    return per_possessions.round(1)

def get_cum_stats_any_team(df, x=None, n=None):
    if (x != None) & (n != None):
            raise ValueError("Can only specify either x games or n days, not both!")
    # get last date
    last_date = df['GAME_DATE'].iloc[-1]

    # filter last x games if x specified
    if x != None:
        if type(x) != int:
            raise TypeError("Invalid Value Type. Must be int")
        idx_first = df.shape[0] - x
        if idx_first < 0:
            idx_first = 0
        df = df.iloc[idx_first:]

    # filter last n days if n specified
    elif n != None:
        if type(n) != int:
            raise TypeError("Invalid Value Type. Must be int")
        date_dt = dt.datetime.strptime(last_date, "%Y-%m-%d")
        date_dt_first = date_dt - dt.timedelta(days=n)
        date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
        df = df[df['GAME_DATE'] > date_first]

    # drop columns that are not cumulative
    drop_columns = ['GAME_DATE', 'MATCHUP', 'WL', 'W', 'L', 'W_PCT',
                   'GAME_ID', 'TEAM_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION',
                    'TEAM_CITY', 'FG_PCT', 'FG3_PCT', 'FT_PCT',
                   ]
    df = df.drop(columns=drop_columns)

    # filter our advanced columns that use special mean function
    adv_cols = list(df.columns[17:])
    remove = ['AST_TOV', 'NET_RATING', 'E_NET_RATING', 'POSS']
    adv_cols = [x for x in adv_cols if x not in remove]


    # calculate mean traditional stats
    totals = df.sum(axis=0)
    totals['GAMES'] = df.shape[0]
    totals['FG_PCT'] = totals.FGM / totals.FGA
    totals['FG3_PCT'] = totals.FG3M / totals.FG3A
    totals['FT_PCT'] = totals.FTM / totals.FTA

    # calculate mean advanced stats
    for col in adv_cols:
        totals[col] = gmas(col, df)

    # calc remaining adv stats
    totals.NET_RATING = totals.OFF_RATING - totals.DEF_RATING
    totals.E_NET_RATING = totals.E_OFF_RATING - totals.E_DEF_RATING
    totals.AST_TOV = totals.AST / totals.TO

    for i in totals.index:
        if "PCT" in i:
            totals.loc[i] = totals.loc[i] * 100
        elif i == "PIE":
            totals.loc[i] = totals.loc[i] * 100


    return totals.round(1)
    
def get_per_game_stats_any_team(df, x=None, n=None):
    cum_stats = get_cum_stats_any_team(df=df, x=x, n=n)

    divide_col_index = list(cum_stats.index[:17])
    divide_col_index.append("POSS")

    for idx in divide_col_index:
        name = idx + "_PG"
        cum_stats[name] = cum_stats[idx] / cum_stats.GAMES
        cum_stats.drop(index=idx, inplace=True)

    per_game = cum_stats

    return per_game.round(1)
        
def get_per_p_possessions_stats_any_team(df, p=100, x=None, n=None):
    cum_stats = get_cum_stats_any_team(df=df, x=x, n=n)

    divide_col_index = list(cum_stats.index[:17])
    divide_col_index.append("POSS")
    total_poss = cum_stats.POSS

    for idx in divide_col_index:
        name = idx + "_P{}P".format(p)
        cum_stats[name] = cum_stats[idx] / total_poss * p
        cum_stats.drop(index=idx, inplace=True)

    per_possessions = cum_stats

    return per_possessions.round(1)


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    """
    Used in generate_wordcloud method.
    """
    colors = ['#552583', '#FDB927', 'white', '#405ED7', "#FDB927"]
    return random.choice(colors)




################################# Team Date Class ###########################################

class TeamDate():
    """
    Create team date object. Note this is only valid for the 2022-23 season and only teams \
    where Laker players played on during the season. 
    """
    # set data path
    path = "assets/"
    
    def __init__(self, abb, date="2023-04-10"):
        self._set_abb(abb)
        self._set_date(date)
        self._set_stats(abb, date)
        self._set_common_info()
        self._set_full_name()
        self._set_current_seed()
        self.id = load_json_file("teams.json", path=path)[abb]['id']
        self.game_ids = load_json_file("teams.json", path=path)[abb]['game_ids']
        self._set_entities()
        self._set_token_dict()
        self._set_sentiment_df()
    
    def _set_abb(self, abb):
        if abb in load_json_file("teams.json", path=path).keys():
            self.abb = abb
        else:
            raise ValueError("Invalid Team Abbreviation, try again")
        
    def _set_date(self, date):
        match = re.findall(r"\d{4}-\d{2}-\d{2}", date)
        if len(match) == 1:
            if date < "2022-10-18":
                self.date = "beginning"
            else:
                self.date = date
        else:
            raise ValueError("Invalid Date Format; must be '%Y-%m-%d'")
        
    def _set_stats(self, abb, date):
        if self.date == "beginning":
            self.stats = "Date is prior to season started and therefore no stats exist"
            
        else:
            stats = pd.read_csv(path + "full_team_data_{}.csv".format(abb),
                                index_col=0,
                                parse_dates=['GAME_DATE'])
            stats['GAME_ID'] = '00' + stats['GAME_ID'].astype(str) 
            self.stats = stats[stats['GAME_DATE'] <= self.date]
            self.stats['MIN'] = [int(x[:3]) for x in self.stats['MIN']]
        
    def _set_common_info(self):
        tic_df = pd.read_csv(path + "common_team_info.csv", index_col=0)
        ci = tic_df[tic_df['TEAM_ABBREVIATION'] == self.abb]
        
        self.common_info = ci
        
    def _set_full_name(self):
        ci = self.common_info
        full_name = ci['TEAM_CITY'] + " " + ci['TEAM_NAME']
        self.full_name = full_name[0]        
        
    def _set_current_seed(self):
        seeding = pd.read_csv(path + "seedings_data_{}.csv".format(self.abb), index_col=0)
        ci = self.common_info
        conf = ci['TEAM_CONFERENCE'].values[0]
        if self.date < '2022-10-18':
            self.current_seed = "No current seed! Season hasn't started!"
        elif self.date > '2023-04-09':
            team_seeding = seeding[seeding['DATE'] == '2023-04-09']
            seed = team_seeding.RANK.values[0]
            self.current_seed = conf + " Seed " + str(seed)
        else:
            team_seeding = seeding[seeding['DATE'] == self.date]
            seed = team_seeding.RANK.values[0]
            self.current_seed = conf + " Seed " + str(seed)

    def _set_entities(self):
        with open(path + 'entities_with_nicknames.json', 'r') as f:
            entities = json.load(f)
        entities = dict(entities)
        self.entities = entities

    def _set_token_dict(self):
        with open('assets/token_dicts/post_plus_comment_body_tokenize.json', 'r') as f:
            token_dict = json.load(f)
        self.token_dict = dict(token_dict)
        
    def _set_sentiment_df(self):
        tsent = pd.read_csv("assets/all_sents/total_sentiment.csv", index_col=0, parse_dates=['datetime'])
        tsent = tsent[tsent['datetime'] <= self.date]
        self.sentiment_df = tsent

    def _set_fo_sent_df(self):
        fosent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
        fosent = fosent[(fosent['player_date'] == 'jeanie_buss') | (fosent['player_date'] == 'rob_pelinka') | (fosent['player_date'] == 'darvin_ham')]
        self.fo_sent = fosent


########################################## GET TEAM STATS###################################################        
    def get_record(self, x=None, n=None):
        """
        Returns current record or record over last x games or record over last n days.
        """
        # make sure both x and n are not specified
        if (x != None) & (n != None):
            raise ValueError("Can only specify either x games or n days, not both!")
        
        stats=self.stats
        
        if x != None:
            if type(x) != int:
                raise TypeError("Invalid number, must be int")
                
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            stats = stats.iloc[idx_first:]
            
            wins = 0
            losses = 0
            for i, row in stats.iterrows():
                if row.WL == 'W':
                    wins += 1
                else:
                    losses += 1
            return "{}-{}".format(wins, losses)
        
        elif n != None:
            if type(n) != int:
                raise TypeError("Invalid number, must be int")
            
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            stats = stats[stats['GAME_DATE'] > date_first]
            print(stats.shape[0])
            
            if len(stats) == 0:
                raise ValueError("No Data available between selected dates")
            
            wins = 0
            losses = 0
            for i, row in stats.iterrows():
                if row.WL == 'W':
                    wins += 1
                else:
                    losses += 1
            return "{}-{}".format(wins, losses)
        
        else:
            if self.date == "beginning":
                return "0-0"
            if self.date >= "2023-04-09":
                return "43-39"
            date = find_nearest_date(self.stats, 'GAME_DATE', self.date)
            row = self.stats[self.stats['GAME_DATE'] == date]
            return "{}-{}".format(row.W.values[0], row.L.values[0])
        
    def current_streak(self):
        if self.date == "beginning":
            return "W0"
        else:
            stats = self.stats
            
            stats = stats.sort_values('GAME_DATE', ascending=False)
            row1 = stats.iloc[0]
            win_or_loss = row1.WL
            streak = 0
            
            for _, row in stats.iterrows():
                if (win_or_loss == 'W') & (row.WL == 'W'):
                    streak += 1
                elif (win_or_loss == 'L') & (row.WL == 'L'):
                    streak += 1
                else:
                    break
            return win_or_loss + str(streak)
        
    def get_cum_stats(self, x=None, n=None):
        """
        Returns team's cumulative stats throughout season. Can specify last x games/or n days
        Parameters:
            x_games: if set, gets cum stats last x games; default=None
            n_days: if set, gets cum stats last n days; default=None
        """
        # make sure both x and n are not specified
        if (x != None) & (n != None):
            raise ValueError("Can only specify either x games or n days, not both!")
        
        # define stats
        stats = self.stats
        
        # filter last x games if x specified
        if x != None:
            if type(x) != int:
                raise TypeError("Invalid Value Type. Must be int")
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            stats = stats.iloc[idx_first:]
            
        # filter last n days if n specified
        elif n != None:
            if type(n) != int:
                raise TypeError("Invalid Value Type. Must be int")
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            stats = stats[stats['GAME_DATE'] > date_first]
        
        # drop columns that are not cumulative
        drop_columns = ['GAME_DATE', 'MATCHUP', 'WL', 'W', 'L', 'W_PCT',
                       'GAME_ID', 'TEAM_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION',
                        'TEAM_CITY', 'FG_PCT', 'FG3_PCT', 'FT_PCT',
                       ]
        stats = stats.drop(columns=drop_columns)
        
        # filter our advanced columns that use special mean function
        adv_cols = list(stats.columns[17:])
        remove = ['AST_TOV', 'NET_RATING', 'E_NET_RATING', 'POSS']
        adv_cols = [x for x in adv_cols if x not in remove]
        
        
        # calculate mean traditional stats
        totals = stats.sum(axis=0)
        totals['GAMES'] = stats.shape[0]
        totals['FG_PCT'] = totals.FGM / totals.FGA
        totals['FG3_PCT'] = totals.FG3M / totals.FG3A
        totals['FT_PCT'] = totals.FTM / totals.FTA
        
        # calculate mean advanced stats
        for col in adv_cols:
            totals[col] = gmas(col, stats)
        
        # calc remaining adv stats
        totals.NET_RATING = totals.OFF_RATING - totals.DEF_RATING
        totals.E_NET_RATING = totals.E_OFF_RATING - totals.E_DEF_RATING
        totals.AST_TOV = totals.AST / totals.TO
        
        for i in totals.index:
            if "PCT" in i:
                totals.loc[i] = totals.loc[i] * 100
            elif i == "PIE":
                totals.loc[i] = totals.loc[i] * 100
                
                
        return totals.round(1)
    
    def get_per_game_stats(self, x=None, n=None):
        cum_stats = self.get_cum_stats(x=x, n=n)
        
        divide_col_index = list(cum_stats.index[:17])
        divide_col_index.append("POSS")
        
        for idx in divide_col_index:
            name = idx + "_PG"
            cum_stats[name] = cum_stats[idx] / cum_stats.GAMES
            cum_stats.drop(index=idx, inplace=True)
        
        per_game = cum_stats
        
        return per_game.round(1)
        
    
    def get_per_m_minutes_stats(self, m=240, x=None, n=None):
        cum_stats = self.get_cum_stats(x=x, n=n)
        
        divide_col_index = list(cum_stats.index[:17])
        divide_col_index.append("POSS")
        total_min = cum_stats.MIN
        
        for idx in divide_col_index:
            name = idx + "_P{}M".format(m)
            cum_stats[name] = cum_stats[idx] / total_min * m
            cum_stats.drop(index=idx, inplace=True)
        
        per_minutes = cum_stats
        
        return per_minutes.round(1)
        
    def get_per_p_possessions_stats(self, p=100, x=None, n=None):
        cum_stats = self.get_cum_stats(x=x, n=n)
        
        divide_col_index = list(cum_stats.index[:17])
        divide_col_index.append("POSS")
        total_poss = cum_stats.POSS
        
        for idx in divide_col_index:
            name = idx + "_P{}P".format(p)
            cum_stats[name] = cum_stats[idx] / total_poss * p
            cum_stats.drop(index=idx, inplace=True)
        
        per_possessions = cum_stats
        
        return per_possessions.round(1)
    
    def get_trending_pg(self, x=10, x_comp=10, n=None, n_comp=None, full_szn=True):
        ### get latest stats ###
        stats = self.stats
        per_game = self.get_per_game_stats(x=x, n=n)
        
        
        if x != None:
            # get full comp group
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            comp = stats.iloc[:idx_first]
            
            if full_szn:
                x_comp=None
            comp_pg = get_per_game_stats_any_team(comp, x=x_comp)
            
        else:
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            comp = stats[stats['GAME_DATE'] <= date_first]
            
            if full_szn:
                n_comp=None
                
            comp_pg = get_per_game_stats_any_team(comp, n=n_comp)
        
        ### compare groups and return groups and comp ###
        diff = (per_game.values - comp_pg.values) / comp_pg.values * 100
        diff = pd.DataFrame(diff, index=comp_pg.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (per_game.values - comp_pg.values)
        
        return diff, per_game, comp_pg
    
    def get_trending_p100(self, x=10, x_comp=10, n=None, n_comp=None, full_szn=True):
        ### get latest stats ###
        stats = self.stats
        per100 = self.get_per_p_possessions_stats(x=x, n=n, p=100)
        
        if x != None:
            # get full comp group
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            comp = stats.iloc[:idx_first]
            
            if full_szn:
                x_comp=None
            comp_p100 = get_per_p_possessions_stats_any_team(comp, x=x_comp, p=100)
            
        else:
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            comp = stats[stats['GAME_DATE'] <= date_first]
            
            if full_szn:
                n_comp=None
            comp_p100 = get_per_p_possessions_stats_any_team(comp, n=n_comp, p=100)
            
        
        diff = (per100.values - comp_p100.values) / comp_p100.values * 100
        diff = pd.DataFrame(diff, index=comp_p100.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (per100.values - comp_p100.values)
        
        return diff, per100, comp_p100

    def get_rolling_per_game_df(self, n=20):
        stats = self.stats
        cols = get_per_game_stats_any_team(stats).index
        dfpg = pd.DataFrame(columns=cols)

        for i, row in stats.iterrows():
            gd_current = row.GAME_DATE
            start_date = gd_current - dt.timedelta(days=n)
            s = stats[(stats['GAME_DATE'] > start_date) & (stats['GAME_DATE'] <= gd_current)]
            data = list(get_per_game_stats_any_team(s))
            dfpg.loc[i] = data
        
        dfpg.index=stats.index
        dfpg['GAME_DATE'] = stats.GAME_DATE
        
        return dfpg

    def get_rolling_per_100_df(self, n=20):
        stats = self.stats
        cols = get_per_p_possessions_stats_any_team(stats).index
        dfp100 = pd.DataFrame(columns=cols)
        
        for i, row in stats.iterrows():
            gd_current = row.GAME_DATE
            start_date = gd_current - dt.timedelta(days=n)
            s = stats[(stats['GAME_DATE'] > start_date) & (stats['GAME_DATE'] <= gd_current)]
            data = list(get_per_p_possessions_stats_any_team(s))
            dfp100.loc[i] = data
        
        dfp100.index=stats.index
        dfp100['GAME_DATE'] = stats.GAME_DATE
        return dfp100

################################## GET SENTIMENT STATS #####################################
    def get_sentiment(self, post_multiplier=2.5):
        """
        This function simply takes in sent df and returns average sentiment
        Parameters:
            post_multiplier: how much more should we weight post vs comment? Default = 2.5
        """
        # get post sentiment score
        try:
            post_sent = self.sentiment_df[self.sentiment_df['pc'] == 'p']
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
            comment_sent =  self.sentiment_df[self.sentiment_df['pc'] == 'c']
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

    def get_trending_sentiment(self, n=20, n_comp=None):
        if type(n) != int:
            raise TypeError("Invalid Value Type. Must be int")
            
        sent = self.sentiment_df
        date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
        date_dt_first = date_dt - dt.timedelta(days=n)
        date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
        trend = sent[sent['datetime'] > date_first]
        
        sent_score_last_n = ss.get_sentiment(trend)
        
        comp = sent[sent['datetime'] <= date_first]
        if n_comp != None:
            date_dt2 = dt.datetime.strptime(date_first, "%Y-%m-%d")
            date_dt_first2 = date_dt2 - dt.timedelta(days=n_comp)
            date_first2 = dt.datetime.strftime(date_dt_first2, "%Y-%m-%d")
            comp = comp[comp['datetime'] > date_first2]
        sent_score_comp = ss.get_sentiment(comp) 
        diff = (sent_score_last_n - sent_score_comp) / sent_score_comp
        
        return sent_score_last_n, sent_score_comp, diff
    
    def get_mentions_per_day(self):
        df = self.sentiment_df
        df = df[['datetime', 'sentiment']]
        idx = pd.period_range(min(df.datetime), max(df.datetime)).astype('datetime64[ns]') 
        mentions = df.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0)
        
        return mentions.sentiment.mean()
    
    def get_trending_mentions_per_day(self, n=14, n_comp=None):
        if type(n) != int:
            raise TypeError("Invalid Value Type. Must be int")
            
        df = self.sentiment_df
        df = df[['datetime', 'sentiment']]
        idx = pd.period_range(min(df.datetime), max(df.datetime)).astype('datetime64[ns]') 
        mentions = df.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0)
        
        date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
        date_dt_first = date_dt - dt.timedelta(days=n)
        date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
        trend = mentions[mentions.index > date_first] 
        trend = trend.sentiment.mean()
        
        comp = mentions[mentions.index <= date_first]
        if n_comp != None:
            date_dt2 = dt.datetime.strptime(date_first, "%Y-%m-%d")
            date_dt_first2 = date_dt2 - dt.timedelta(days=n_comp)
            date_first2 = dt.datetime.strftime(date_dt_first2, "%Y-%m-%d")
            comp = comp[comp.index > date_first2]
        
        comp = comp.sentiment.mean()
        
        diff = (trend - comp) / comp
        
        return trend, comp, diff
    
    def get_rolling_sentiment_score_df(self, n=20):
        sent = self.sentiment_df
        cols = ['weighted']
        idx = sorted(list(set(sent['datetime'])))
        dfs = pd.DataFrame(columns=cols, index=idx)

        weighted=[]
        for i in idx:
            start = i - dt.timedelta(days=20)
            s = sent[(sent['datetime'] > start) & (sent['datetime'] <= i) ]
            w = ss.get_sentiment(s)
            weighted.append(w)
        dfs['weighted'] = weighted
            
        return dfs
    
    def get_rolling_mentions_df(self, n=20):
        df = self.sentiment_df
        df = df[['datetime', 'sentiment']]
        idx = pd.period_range(min(df.datetime), max(df.datetime)).astype('datetime64[ns]') 
        df = df.set_index('datetime')
        mentions = df.groupby('datetime').count().reindex(idx, fill_value=0)
        cols = ['mentions']
        dfm = pd.DataFrame(columns=cols, index=idx)
        
        ms = []
        for i in idx:
            start = i - dt.timedelta(days=n)
            mm = mentions[(mentions.index > start) &(mentions.index <= i)]
            m = mm.sentiment.mean()
            ms.append(m)
        dfm['mentions'] = ms
        
        return dfm
    
    def get_rolling_team_wpct_df(self, n=20):
        team_stats = self.stats
        idx = pd.period_range(min(team_stats.GAME_DATE), max(team_stats.GAME_DATE)).astype('datetime64[ns]')
        cols = ['wpct']
        dft = pd.DataFrame(columns=cols, index=idx)
        
        ws = []
        for i in idx:
            start = i - dt.timedelta(days=n)
            ww = team_stats[(team_stats.GAME_DATE > start) & (team_stats.GAME_DATE <= i)].reset_index().drop(columns=['index'])
            wins = ww.iloc[-1].W - ww.W[0]
            losses = ww.iloc[-1].L - ww.L[0]
            wpct = wins / (wins + losses)
            ws.append(wpct)
        dft['wpct'] = ws
        
        return dft



################################################ PLOTS AND VISUALIZATIONS ################################################
    def plot_sentiment_through_time(self):
        post_sent = self.sentiment_df[self.sentiment_df['pc'] == 'p']
        comment_sent =  self.sentiment_df[self.sentiment_df['pc'] == 'c']

        ## multiply poss by post_mult and combine post and comment sents w dates
        posts = pd.concat([post_sent, post_sent, post_sent]).reset_index().drop(columns=['index'])
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
        pos_resamp = co_pos.groupby('datetime').count().reindex(idx, fill_value=0).resample('3D').sum()
        neg_resamp = co_neg.groupby('datetime').count().reindex(idx, fill_value=0).resample('3D').sum()
        neu_resamp = co_neu.groupby('datetime').count().reindex(idx, fill_value=0).resample('3D').sum()

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

    def generate_wordcloud(self):
        token_dict = dict(self.token_dict)
        wordcloud = WordCloud(width=1600,
                              height=400,
                              background_color='#311149',
                              color_func=random_color_func,
                              min_font_size=10).generate_from_frequencies(token_dict)
        #plt.imshow(wordcloud, interpolation='bilinear')
        #plt.axis('off')
        return wordcloud.to_image()
        
        
    def basic_pie_chart(self):
        df = self.sentiment_df
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

    def plot_top_ten(self, kind='all'):
        if kind not in ['all', 'positive', 'negative']:
            raise ValueError("Invalid kind, must be in 'all', 'positive', 'negative'")

        if kind == 'all':
            tok = sorted(self.token_dict.items(), key=lambda x:x[1], reverse=True)
        elif kind == 'positive':
            with open("assets/token_dicts/pos.json", "r") as f:
                token_dict = json.load(f)
            tok = sorted(token_dict.items(), key=lambda x:x[1], reverse=True)
        else:
            with open("assets/token_dicts/neg.json", "r") as f:
                token_dict = json.load(f)
            tok = sorted(token_dict.items(), key=lambda x:x[1], reverse=True)

        tok = tok[:50]

        blacklist = [
            'lakers', 'lakers_team', 'lebron_james', 'anthony_davis',
            'russell_westbrook'
        ]
        toks = []
        counts = []
        for i, _ in enumerate(tok):
            if tok[i][0] not in blacklist:
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

    def plot_top_ten_emoji(self, kind='all'):
        if kind not in ['all', 'positive', 'negatives']:
            raise ValueError("Invalid kind, must be in 'all', 'positive', 'negative'")

        if kind == 'all':
            tok = sorted(self.token_dict.items(), key=lambda x:x[1], reverse=True)
        elif kind == 'positive':
            with open("assets/token_dicts/pos.json", "r") as f:
                token_dict = json.load(f)
            tok = sorted(token_dict.items(), key=lambda x:x[1], reverse=True)
        else:
            with open("assets/token_dicts/neg.json", "r") as f:
                token_dict = json.load(f)
            tok = sorted(token_dict.items(), key=lambda x:x[1], reverse=True)

        tok = tok[:50]


        emj = ss.get_emoji_dict(player_ref='team', kind=kind)
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

    def sent_vs_stat(self, stat_col, kind='g'):
        if kind not in ['g', 'p', 't']:
            raise ValueError("Invalid stat type")
            
        adj_cols=[
            'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB',
            'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS', 'POS_PG'
        ]

        ## Load all needed stats ##
        sent = self.get_rolling_sentiment_score_df()

        if kind == 'g':
            stats = self.get_rolling_per_game_df()
            suffix = '_PG'
        elif kind == 'p':
            stats = self.get_rolling_per_100_df()
            suffix = '_P100P'
        else:
            stats = self.get_rolling_team_wpct_df()
            stat_col = 'wpct'
            stats['GAME_DATE'] = stats.index
        
        if stat_col in adj_cols:
            stat_col = stat_col + suffix


        # Create the figure

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(
                y=sent.weighted,
                x=sent.index,
                name='Sentiment',
                line=dict(color='#FDB927')
            ),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(
                x=stats.GAME_DATE,
                y=stats[stat_col],
                name='{}'.format(stat_col),
                line=dict(color='#840DFA')
            ),
            secondary_y=True,
        )
        
        custom_template = templates["plotly_dark"]
        custom_template.layout["xaxis"]["showgrid"] = False
        custom_template.layout["yaxis"]["showgrid"] = False
        
        fig.update_yaxes(title_text="Rolling 20-day MA Sentiment Score", title_font=dict(color='#FDB927'), secondary_y=False)
        fig.update_yaxes(title_text="Rolling 20-day MA {}".format(stat_col), title_font=dict(color='#840DFA'), secondary_y=True)

        fig.update_layout(
                title='Rolling 20-day Sentiment vs {}'.format(stat_col),
                xaxis_title='Date',
                template=custom_template,
                plot_bgcolor='black',
                paper_bgcolor='black',
            )

        return fig

    def sent_vs_stat_corr(self, stat_col, kind='g'):
        if kind not in ['g', 'p', 't']:
            raise ValueError("Invalid stat type")
            
        adj_cols=[
                'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB',
                'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS', 'POS_PG'
            ]

        sent = self.get_rolling_sentiment_score_df()

        if kind == 'g':
            stats = self.get_rolling_per_game_df()
            stats['GAME_DATE'] = stats.GAME_DATE.dt.date
            suffix = '_PG'
        elif kind == 'p':
            stats = self.get_rolling_per_100_df()
            stats['GAME_DATE'] = stats.GAME_DATE.date
            suffix = '_P100P'
        else:
            stats = self.get_rolling_team_wpct_df()
            stat_col = 'wpct'
            stats.loc['2022-10-18'] = 0
            stats.loc['2022-10-19'] = 0

        if stat_col in adj_cols:
            stat_col = stat_col + suffix

        x = stats

        if kind != 't':
            xmin = stats.GAME_DATE.min()
            xmax = stats.GAME_DATE.max()
            y = sent.loc[xmin:xmax]
            date_range = pd.date_range(start=x.GAME_DATE.min(), end=x.GAME_DATE.max(), freq='D')
            x = x.set_index('GAME_DATE')
            new_index = pd.Index(date_range, name='Date')
            x = x.reindex(new_index).ffill()

            corr = y['weighted'].corr(x[stat_col])
        else:
            xmin = stats.index.min()
            xmax = stats.index.max()
            y = sent.loc[xmin:xmax]
            corr = y['weighted'].corr(x[stat_col])
        return corr

        
############################## Player Date Class ############################################        

class PlayerDate():
    # set data path
    path = "assets/"
    def __init__(self, name, date="2023-04-10"):
        self._set_name(name)
        self._set_date(date)
        self._set_pid()
        self._set_transactions()
        self._set_acquired()
        self._set_moved()
        self._set_waived()
        self._set_signed()
        self._set_traded_away()
        self._set_traded_for()
        self._set_other_teams()
        self._set_common_info()
        self._set_stats()
        self._set_laker_stats()
        self._set_non_laker_stats()
        self._set_ent_key()
        self._set_entities()
        self._set_token_dict()
        self._set_sentiment_df()
        self._set_laker_sentiment_df()
        

    def _set_name(self, name):
        if name in load_json_file("players.json", path=path).keys():
            self.name = name
        else:
            raise ValueError("Invalid player name, try again")
    
    def _set_date(self, date):
        match = re.findall(r"\d{4}-\d{2}-\d{2}", date)
        if len(match) == 1:
            if date < "2022-10-18":
                self.date = "beginning"
            else:
                self.date = date
        else:
            raise ValueError("Invalid Date Format; must be '%Y-%m-%d'")
            
    def _set_pid(self):
        players = load_json_file("players.json", path=path)
        self.pid = players[self.name]
    
    def _set_transactions(self):
        transactions = load_json_file("transactions.json", path=path)
        if self.name not in transactions.keys():
            self.transactions = None
        else:
            self.transactions = transactions[self.name]
    
    def _set_acquired(self):
        if self.transactions == None:
            self.acquired = False
        elif self.transactions['date_acquired'] == None:
            self.acquired = False
        else:
            self.acquired = self.transactions['date_acquired']
            
    def _set_moved(self):
        if self.transactions == None:
            self.moved = False
        elif self.transactions['date_moved'] == None:
            self.moved = False
        else:
            self.moved = self.transactions['date_moved']
            self.date = self.moved
            
    def _set_waived(self):
        if self.transactions == None:
            self.waived= False
        elif self.transactions['waived'] == False:
            self.waived = False
        else:
            self.waived = "Waived on {}".format(self.moved)
    
    def _set_signed(self):
        if self.transactions == None:
            self.signed= False
        elif self.transactions['signed'] == False:
            self.signed = False
        else:
            self.signed = "Signed on {}".format(self.acquired)
    
    def _set_traded_away(self):
        if self.transactions == None:
            self.traded_away = False
        elif self.transactions['traded_away'] == False:
            self.traded_away = False
        else:
            self.traded_away = "Traded on {}".format(self.moved)
    
    def _set_traded_for(self):
        if self.transactions == None:
            self.traded_for= False
        elif self.transactions['traded_for'] == False:
            self.traded_for = False
        else:
            self.traded_for = "Traded for on {}".format(self.acquired)
    
    def _set_other_teams(self):
        if self.transactions == None:
            self.other_teams = False
        else:
            self.other_teams = self.transactions['other_teams']
      
    def _set_common_info(self):
        pic_df = pd.read_csv(path + "common_player_info.csv", index_col=0)
        ci = pic_df[pic_df['PERSON_ID'] == self.pid]
        self.common_info = ci
        
    def _set_stats(self):
        if self.date == "beginning":
            self.stats = "Date is prior to season started and therefore no stats exist"
        else:
            stats = pd.read_csv(path + "player_total_total.csv",
                                index_col=0,
                                parse_dates=['GAME_DATE'])
            stats = stats.sort_values('GAME_DATE')
            stats = stats[stats['PLAYER_ID'] == self.pid].reset_index().drop(columns=('index'))
            stats = stats.drop(columns=['Game_ID', 'Team_ID', 'PACE_PER40'])
            stats = stats[stats['GAME_DATE'] <= self.date]
            self.stats = stats
        
    def _set_laker_stats(self):
        if self.transactions == None:
            self.laker_stats = self.stats
        else:
            stats = self.stats
            laker_stats = stats[stats['TEAM_ABBREVIATION'] == 'LAL']
            self.laker_stats = laker_stats.reset_index().drop(columns=('index'))
            
    def _set_non_laker_stats(self):
        if self.transactions == None:
            self.non_laker_stats = None
        
        else:
            stats = self.stats
            non_laker_stats = stats[stats['TEAM_ABBREVIATION'] != 'LAL']
            self.non_laker_stats = non_laker_stats
            
    def _set_ent_key(self):
        with open(path + "name_conv.json", "r") as f:
            name_conv = json.load(f)
        name_conv = dict(name_conv)
        
        self.ent_key = name_conv[self.name]
    
    def _set_entities(self):
        with open(path + 'entities_with_nicknames.json', 'r') as f:
            entities = json.load(f)
        entities = dict(entities)
        
        self.entities = entities[self.ent_key]
    
    def _set_token_dict(self):
        with open('assets/token_dicts/{}_token_dicts.json'.format(self.ent_key), 'r') as f:
            token_dict = json.load(f)
        self.token_dict = dict(token_dict)
        
    def _set_sentiment_df(self):
        psent = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
        psent_filtered = psent[psent['player_ref'] == self.entities['full_name']]
        psent_filtered = psent_filtered[psent_filtered['datetime'] <= self.date]
        self.sentiment_df = psent_filtered.reset_index().drop(columns=['index'])
        
    def _set_laker_sentiment_df(self):
        psent_filtered = self.sentiment_df
        
        if (not self.acquired) & (not self.moved):
            self.laker_sentiment_df = psent_filtered
        
        elif not self.acquired:
            psent_filtered = psent_filtered[psent_filtered['datetime'] <= self.moved]
            self.laker_sentiment_df = psent_filtered.reset_index().drop(columns=['index'])
            
        else:
            psent_filtered = psent_filtered[psent_filtered['datetime'] >= self.acquired]
            self.laker_sentiment_df = psent_filtered.reset_index().drop(columns=['index'])
        
    ################################################ GET PLAYER STATS ################################################
    def get_cum_stats(self, x=None, n=None, laker_only=False):
        """
        Returns player's cumulative stats throughout season. /
        Can specify last x games/or n days and also whether to include all stats or laker only
        Parameters:
            x_games: if set, gets cum stats last x games; default=None
            n_days: if set, gets cum stats last n days; default=None
        """
        if (x != None) & (n != None):
            raise ValueError("Can only specify either x games or n days, not both!")
        
        # define stats
        if laker_only:
            stats = self.laker_stats
        else:
            stats = self.stats
            
        # drop games with 0 minutes played:
        stats = stats[~stats['MIN'].isna()].reset_index().drop(columns=("index"))
        
        # filter last x games if x specified
        if x != None:
            if type(x) != int:
                raise TypeError("Invalid Value Type. Must be int")
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            stats = stats.iloc[idx_first:]
            
        # filter last n days if n specified
        elif n != None:
            if type(n) != int:
                raise TypeError("Invalid Value Type. Must be int")
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            stats = stats[stats['GAME_DATE'] > date_first]
            
        
        # drop columns that are not cumulative
        drop_columns = ['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY',
                        'PLAYER_ID', 'PLAYER_NAME', 'FG_PCT', 'FG3_PCT', 'FT_PCT',
                        'GAME_DATE', 'MATCHUP', 'WL', 'TM_TOV_PCT']
        
        stats = stats.drop(columns=drop_columns)

        # filter our advanced columns that use special mean function
        adv_cols = list(stats.columns[16:36])
        remove = ['AST_TOV', 'NET_RATING', 'E_NET_RATING', 'POSS']
        adv_cols = [x for x in adv_cols if x not in remove]

        # calculate mean traditional stats
        totals = stats.sum(axis=0)
        totals['GAMES'] = stats.shape[0]
        totals['FG_PCT'] = totals.FGM / totals.FGA
        totals['FG3_PCT'] = totals.FG3M / totals.FG3A
        totals['FT_PCT'] = totals.FTM / totals.FTA
        
        # calculate mean advanced stats
        for col in adv_cols:
            totals[col] = gmas(col, stats)

        # calc remaining adv stats
        totals.NET_RATING = totals.OFF_RATING - totals.DEF_RATING
        totals.E_NET_RATING = totals.E_OFF_RATING - totals.E_DEF_RATING
        totals.AST_TOV = totals.AST / totals.TO

        # format data and return
        for i in totals.index:
            if "PCT" in i:
                totals.loc[i] = totals.loc[i] * 100
            elif i == "PIE":
                totals.loc[i] = totals.loc[i] * 100
        return totals.round(1)

    def get_per_game_stats(self, x=None, n=None, laker_only=False):
        cum_stats = self.get_cum_stats(x=x, n=n, laker_only=laker_only)
        
        divide_col_index = list(cum_stats.index[:16])
        divide_col_index.append("POSS") 
        divide_col_index.append("MIN") 
        
        for idx in divide_col_index:
            name = idx + "_PG"
            cum_stats[name] = cum_stats[idx] / cum_stats.GAMES
            cum_stats.drop(index=idx, inplace=True)
        
        per_game = cum_stats
        
        return per_game.round(1)
    
    def get_per_m_minutes_stats(self, m=36, x=None, n=None, laker_only=False):
        cum_stats = self.get_cum_stats(x=x, n=n)
        divide_col_index = list(cum_stats.index[:16])
        divide_col_index.append("POSS") 
        divide_col_index.append("MIN") 
        total_min = cum_stats.MIN
        
        for idx in divide_col_index:
            name = idx + "_P{}M".format(m)
            cum_stats[name] = cum_stats[idx] / total_min * m
            cum_stats.drop(index=idx, inplace=True)
        
        per_minutes = cum_stats
        
        return per_minutes.round(1)
        
    def get_per_p_possessions_stats(self, p=100, x=None, n=None, laker_only=False):
        cum_stats = self.get_cum_stats(x=x, n=n)
        
        divide_col_index = list(cum_stats.index[:16])
        divide_col_index.append("POSS") 
        divide_col_index.append("MIN") 
        total_poss = cum_stats.POSS
        
        for idx in divide_col_index:
            name = idx + "_P{}P".format(p)
            cum_stats[name] = cum_stats[idx] / total_poss * p
            cum_stats.drop(index=idx, inplace=True)
        
        per_possessions = cum_stats
        
        return per_possessions.round(1)
    
    def get_trending_pg(self, x=10, x_comp=10, n=None, n_comp=None, laker_only=False, full_szn=True):
        ### get latest stats ###
        per_game = self.get_per_game_stats(x=x, n=n, laker_only=laker_only)
        
        if laker_only:
            stats = self.laker_stats
        else:
            stats = self.stats
        
        ### get compare group stats for x games ###
        if x != None:
            # get full comp group
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            comp = stats.iloc[:idx_first]
            
            if full_szn:
                x_comp=None
            
            comp_pg = get_per_game_stats_any(comp, x=x_comp)
                
        ### get compare group stats for n days ###      
        else:
            # get full comp group
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            comp = stats[stats['GAME_DATE'] <= date_first]
            
            if full_szn:
                n_comp=None
            
            comp_pg = get_per_game_stats_any(comp, n=n_comp)
            
        
        ### compare groups and return groups and comp ###
        diff = (per_game.values - comp_pg.values) / comp_pg.values * 100
        diff = pd.DataFrame(diff, index=comp_pg.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (per_game.values - comp_pg.values)
        
        return diff, per_game, comp_pg
               
    def get_trending_p36(self, x=10, x_comp=10, n=None, n_comp=None, laker_only=False, full_szn=True):
        ### get latest stats ###
        per36 = self.get_per_m_minutes_stats(x=x, n=n, laker_only=laker_only, m=36)
        
        if laker_only:
            stats = self.laker_stats
        else:
            stats = self.stats
    
        ### get compare group stats for x games ###
        if x != None:
            # get full comp group
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            comp = stats.iloc[:idx_first]
            
            if full_szn:
                x_comp=None
            
            comp_p36 = get_per_m_minutes_stats_any(comp, x=x_comp, m=36)
                
        ### get compare group stats for n days ###      
        else:
            # get full comp group
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            comp = stats[stats['GAME_DATE'] <= date_first]
            
            if full_szn:
                n_comp=None
            
            comp_p36 = get_per_m_minutes_stats_any(comp, n=n_comp, m=36)

        ### compare groups and return comp ###
        diff = (per36.values - comp_p36.values) / comp_p36.values * 100
        diff = pd.DataFrame(diff, index=comp_p36.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (per36.values - comp_p36.values)
        
        return diff, per36, comp_p36
    
    def get_trending_p100(self, x=10, x_comp=10, n=None, n_comp=None, laker_only=False, full_szn=True):
        ### get latest stats ###
        per100 = self.get_per_p_possessions_stats(x=x, n=n, laker_only=laker_only, p=100)
        
        if laker_only:
            stats = self.laker_stats
        else:
            stats = self.stats
        
        ### get compare group stats for x games ###
        if x != None:
            # get full comp group
            idx_first = stats.shape[0] - x
            if idx_first < 0:
                idx_first = 0
            comp = stats.iloc[:idx_first]
            
            if full_szn:
                x_comp=None
            
            comp_p100 = get_per_p_possessions_stats_any(comp, x=x_comp, p=100)
                
        ### get compare group stats for n days ###      
        else:
            # get full comp group
            date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
            date_dt_first = date_dt - dt.timedelta(days=n)
            date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
            comp = stats[stats['GAME_DATE'] <= date_first]
            
            if full_szn:
                n_comp=None
            
            comp_p100 = get_per_p_possessions_stats_any(comp, n=n_comp, p=100)            
        
        ### compare groups and return comp ###
        diff = (per100.values - comp_p100.values) / comp_p100.values * 100
        diff = pd.DataFrame(diff, index=comp_p100.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (per100.values - comp_p100.values)
        
        return diff, per100, comp_p100   
    
    def get_trend_lal_non_lal_pg(self, x=10, xcomp=10, n=None, n_comp=None, full_szn_lal=True, full_szn_other=True):
        """
        Compare laker vs non-laker stats per game. Can compare last x games or n days of each.
        """
        # get lalppg
        if full_szn_lal:
            pglal = self.get_per_game_stats(laker_only=True)
            
        else:
            pglal = self.get_per_game_stats(x=x, n=n, laker_only=True)
            
        # get comp group
        nonlal = self.non_laker_stats
        
        if full_szn_other:
            comp = get_per_game_stats_any(nonlal)
        else:
            comp = get_per_game_stats_any(nonlal, x=xcomp, n=n_comp)
            
        ### compare groups and return groups and comp ###
        diff = (pglal.values - comp.values) / comp.values * 100
        diff = pd.DataFrame(diff, index=comp.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (pglal.values - comp.values)
        
        return diff, pglal, comp
             
    def get_trend_lal_non_lal_p36(self, x=10, xcomp=10, n=None, n_comp=None, full_szn_lal=True, full_szn_other=True):
        """
        Compare laker vs non-laker stats per 36 min. Can compare last x games or n days of each.
        """
        # get lalp36
        if full_szn_lal:
            p36lal = self.get_per_m_minutes_stats(laker_only=True, m=36)
        else:
            p36lal = self.get_per_m_minutes_stats(x=x, n=n, laker_only=True, m=36)
            
        # get comp group
        nonlal = self.non_laker_stats
        
        if full_szn_other:
            comp = get_per_m_minutes_stats_any(nonlal, m=36)
        else:
            comp = get_per_m_minutes_stats_any(nonlal, x=x_comp, n=n_comp, m=36)
            
            
        ### compare groups and return groups and comp ###
        diff = (p36lal.values - comp.values) / comp.values * 100
        diff = pd.DataFrame(diff, index=comp.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (p36lal.values - comp.values)
        
        return diff, p36lal, comp
                
    def get_trend_lal_non_lal_p100(self, x=10, xcomp=10, n=None, n_comp=None, full_szn_lal=True, full_szn_other=True):
        """
        Compare laker vs non-laker stats per 100 poss. Can compare last x games or n days of each.
        """
        # get lalp100
        if full_szn_lal:
            p100lal = self.get_per_p_possessions_stats(laker_only=True, p=100)
        else:
            p100lal = self.get_per_p_possessions_stats(x=x, n=n, laker_only=True, p=100)
        
        # get comp group
        nonlal = self.non_laker_stats
        
        if full_szn_other:
            comp = get_per_p_possessions_stats_any(nonlal, p=100)
        else:
            comp = get_per_p_possessions_stats_any(nonlal, x=x_comp, n=n_comp, p=100)
    
        ### compare groups and return groups and comp ###
        diff = (p100lal.values - comp.values) / comp.values * 100
        diff = pd.DataFrame(diff, index=comp.index, columns=['PERCENT_DIFF'])
        diff['RAW_DIFF'] = (p100lal.values - comp.values)
        
        return diff, p100lal, comp
    
    def get_rolling_per_game_df(self, n=20):
        stats = self.laker_stats
        cols = get_per_game_stats_any(stats).index
        dfpg = pd.DataFrame(columns=cols)

        for i, row in stats.iterrows():
            gd_current = row.GAME_DATE
            start_date = gd_current - dt.timedelta(days=n)
            s = stats[(stats['GAME_DATE'] > start_date) & (stats['GAME_DATE'] <= gd_current)]
            try:
                data = list(get_per_game_stats_any(s))
                dfpg.loc[i] = data
            except:
                if i == 0:
                    dfpg.loc[0] = 0
                else:
                    dfpg.loc[i] = dfpg.loc[i-1]
        
        dfpg.index=stats.index
        dfpg['GAME_DATE'] = stats.GAME_DATE
        
        return dfpg
    
    def get_rolling_per_36_df(self, n=20):
        stats = self.stats
        cols = get_per_m_minutes_stats_any(stats).index
        dfp36 = pd.DataFrame(columns=cols)
        
        for i, row in stats.iterrows():
            gd_current = row.GAME_DATE
            start_date = gd_current - dt.timedelta(days=n)
            s = stats[(stats['GAME_DATE'] > start_date) & (stats['GAME_DATE'] <= gd_current)]
            try:
                data = list(get_per_m_minutes_stats_any(s))
                dfp36.loc[i] = data
            except:
                if i == 0:
                    dfp36.loc[0] = 0
                else:
                    dfp36.loc[i] = dfp36.loc[i-1]
        dfp36.index=stats.index
        dfp36['GAME_DATE'] = stats.GAME_DATE

        return dfp36
    
    def get_rolling_per_100_df(self, n=20):
        stats = self.laker_stats
        cols = get_per_p_possessions_stats_any(stats).index
        dfp100 = pd.DataFrame(columns=cols)
        
        for i, row in stats.iterrows():
            gd_current = row.GAME_DATE
            start_date = gd_current - dt.timedelta(days=n)
            s = stats[(stats['GAME_DATE'] > start_date) & (stats['GAME_DATE'] <= gd_current)]
            try:
                data = list(get_per_p_possessions_stats_any(s))
                dfp100.loc[i] = data
            except:
                if i == 0:
                    dfp100.loc[0] = 0
                else:
                    dfp100.loc[i] = dfp100.loc[i-1]
        dfp100.index=stats.index
        dfp100['GAME_DATE'] = stats.GAME_DATE
        return dfp100
    
################################################ GET SENTIMENT STATS ################################################

    def get_sentiment(self, post_multiplier=2.5):
        """
        This function simply takes in sent df and returns average sentiment
        Parameters:
            post_multiplier: how much more should we weight post vs comment? Default = 2.5
        """
        # get post sentiment score
        try:
            post_sent = self.laker_sentiment_df[self.laker_sentiment_df['pc'] == 'p']
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
            comment_sent =  self.laker_sentiment_df[self.laker_sentiment_df['pc'] == 'c']
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
    
    def get_trending_sentiment(self, n=20, n_comp=None):
        if type(n) != int:
            raise TypeError("Invalid Value Type. Must be int")
            
        sent = self.laker_sentiment_df
        date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
        date_dt_first = date_dt - dt.timedelta(days=n)
        date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
        trend = sent[sent['datetime'] > date_first]
        
        sent_score_last_n = ss.get_sentiment(trend)
        
        comp = sent[sent['datetime'] <= date_first]
        if n_comp != None:
            date_dt2 = dt.datetime.strptime(date_first, "%Y-%m-%d")
            date_dt_first2 = date_dt2 - dt.timedelta(days=n_comp)
            date_first2 = dt.datetime.strftime(date_dt_first2, "%Y-%m-%d")
            comp = comp[comp['datetime'] > date_first2]
        sent_score_comp = ss.get_sentiment(comp) 
        diff = (sent_score_last_n - sent_score_comp) / sent_score_comp
        
        return sent_score_last_n, sent_score_comp, diff
    
    def get_mentions_per_day(self):
        df = self.laker_sentiment_df
        df = df[['datetime', 'sentiment']]
        idx = pd.period_range(min(df.datetime), max(df.datetime)).astype('datetime64[ns]') 
        mentions = df.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0)
        
        return mentions.sentiment.mean()
    
    def get_trending_mentions_per_day(self, n=14, n_comp=None):
        if type(n) != int:
            raise TypeError("Invalid Value Type. Must be int")
            
        df = self.laker_sentiment_df
        df = df[['datetime', 'sentiment']]
        idx = pd.period_range(min(df.datetime), max(df.datetime)).astype('datetime64[ns]') 
        mentions = df.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0)
        
        date_dt = dt.datetime.strptime(self.date, "%Y-%m-%d")
        date_dt_first = date_dt - dt.timedelta(days=n)
        date_first = dt.datetime.strftime(date_dt_first, "%Y-%m-%d")
        trend = mentions[mentions.index > date_first] 
        trend = trend.sentiment.mean()
        
        comp = mentions[mentions.index <= date_first]
        if n_comp != None:
            date_dt2 = dt.datetime.strptime(date_first, "%Y-%m-%d")
            date_dt_first2 = date_dt2 - dt.timedelta(days=n_comp)
            date_first2 = dt.datetime.strftime(date_dt_first2, "%Y-%m-%d")
            comp = comp[comp.index > date_first2]
        
        comp = comp.sentiment.mean()
        
        diff = (trend - comp) / comp
        
        return trend, comp, diff
    
    def get_rolling_sentiment_score_df(self, n=20):
        sent = self.laker_sentiment_df
        cols = ['weighted']
        idx = sorted(list(set(sent.datetime)))
        dfs = pd.DataFrame(columns=cols, index=idx)
        
        weighted=[]
        for i in idx:
            start = i - dt.timedelta(days=n)
            s = sent[(sent['datetime'] > start) & (sent['datetime'] <= i) ]
            w = ss.get_sentiment(s)
            weighted.append(w)
        dfs['weighted'] = weighted
            
        return dfs
    
    def get_rolling_mentions_df(self, n=20):
        df = self.laker_sentiment_df
        df = df[['datetime', 'sentiment']]
        idx = pd.period_range(min(df.datetime), max(df.datetime)).astype('datetime64[ns]') 
        mentions = df.groupby('datetime').count().resample('1D').sum().reindex(idx, fill_value=0)
        cols = ['mentions']
        dfm = pd.DataFrame(columns=cols, index=idx)
        
        ms = []
        for i in idx:
            start = i - dt.timedelta(days=n)
            mm = mentions[(mentions.index > start) &(mentions.index <= i)]
            m = mm.sentiment.mean()
            ms.append(m)
        dfm['mentions'] = ms
        
        return dfm
    
    def get_rolling_team_wpct_df(self, n=20):
        team = TeamDate("LAL", date=self.date)
        team_stats = team.stats
        idx = pd.period_range(min(team_stats.GAME_DATE), max(team_stats.GAME_DATE)).astype('datetime64[ns]')
        cols = ['wpct']
        dft = pd.DataFrame(columns=cols, index=idx)
        
        ws = []
        for i in idx:
            start = i - dt.timedelta(days=n)
            ww = team_stats[(team_stats.GAME_DATE > start) & (team_stats.GAME_DATE <= i)].reset_index().drop(columns=['index'])
            wins = ww.iloc[-1].W - ww.W[0]
            losses = ww.iloc[-1].L - ww.L[0]
            if wins + losses == 0:
                wpct = 0
            else:
                wpct = wins / (wins + losses)
            ws.append(wpct)
        dft['wpct'] = ws
        
        return dft
        
################################################ GET Word-Assoc ################################################
    
    def get_top_players(self):
        player_ref = self.entities['full_name']
        return ss.get_top_players(player_ref)
    
    def get_emoji_dict(self, kind='all'):
        player_ref = self.entities['full_name']
        return ss.get_emoji_dict(player_ref, kind=kind)
        
    def get_token_dict(self, kind='all'):
        player_ref = self.entities['full_name']
        return ss.get_token_dict(player_ref, kind=kind)
            
################################################ PLOTS AND VISUALIZATIONS ################################################
    def plot_sentiment_through_time(self):
        post_sent = self.laker_sentiment_df[self.laker_sentiment_df['pc'] == 'p']
        comment_sent =  self.laker_sentiment_df[self.laker_sentiment_df['pc'] == 'c']

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


    
    def generate_wordcloud(self):
        token_dict = self.token_dict
        wordcloud = WordCloud(width=1600,
                              height=400,
                              background_color='#311149',
                              color_func=random_color_func,
                              min_font_size=10).generate_from_frequencies(token_dict)
        #plt.imshow(wordcloud, interpolation='bilinear')
        #plt.axis('off')
        return wordcloud.to_image()
        
        
    def basic_pie_chart(self):
        df = self.laker_sentiment_df
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

#        fig.update_layout(
#            title={
#                'text' : "Sentiment Pie Chart".format(self.name),
#                'x':0.5,
#                'xanchor': 'center'
#                },
#            font_family="Courier New",
#            title_font_size=24
 #       )

        return fig

    def plot_top_ten(self, kind='all'):
        player_ref = self.entities['full_name']
        names = self.entities['names']
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

    def plot_top_ten_emoji(self, kind='all'):
        player_ref = self.entities['full_name']
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
    
    def sent_vs_stat_corr(self, stat_col, kind='g'):
        if kind not in ['g', 'm', 'p', 't']:
            raise ValueError("Invalid stat type")
            
        adj_cols=[
            'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB',
            'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS',
        ]

        sent = self.get_rolling_sentiment_score_df()

        if kind == 'g':
            stats = self.get_rolling_per_game_df()
            suffix = '_PG'
        elif kind == 'm':
            stats = self.get_rolling_per_36_df()
            suffix = '_P36M'
        elif kind == 'p':
            stats = self.get_rolling_per_100_df()
            suffix = '_P100P'
        else:
            stats = self.get_rolling_team_wpct_df()
            stat_col = 'wpct'
            stats.loc['2022-10-18'] = 0
            stats.loc['2022-10-19'] = 0

        if stat_col in adj_cols:
            stat_col = stat_col + suffix

        x = stats

        if kind != 't':
            xmin = stats.GAME_DATE.min()
            xmax = stats.GAME_DATE.max()
            y = sent.loc[xmin:xmax]
            date_range = pd.date_range(start=x.GAME_DATE.min(), end=x.GAME_DATE.max(), freq='D')
            x = x.set_index('GAME_DATE')
            new_index = pd.Index(date_range, name='Date')
            x = x.reindex(new_index).ffill()

            corr = y['weighted'].corr(x[stat_col])
        else:
            xmin = stats.index.min()
            xmax = stats.index.max()
            y = sent.loc[xmin:xmax]
            corr = y['weighted'].corr(x[stat_col])
        return corr




    def sent_vs_stat(self, stat_col, kind='g'):
        if kind not in ['g', 'm', 'p', 't']:
            raise ValueError("Invalid stat type")
            
        adj_cols=[
            'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB',
            'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS',
        ]

        ## Load all needed stats ##
        mentions = self.get_rolling_mentions_df()
        team = self.get_rolling_team_wpct_df()
        sent = self.get_rolling_sentiment_score_df()

        if kind == 'g':
            stats = self.get_rolling_per_game_df()
            suffix = '_PG'
        elif kind == 'm':
            stats = self.get_rolling_per_36_df()
            suffix = '_P36M'
        elif kind == 'p':
            stats = self.get_rolling_per_100_df()
            suffix = '_P100P'
        else:
            stats = self.get_rolling_team_wpct_df()
            stat_col = 'wpct'
            stats['GAME_DATE'] = stats.index
        
        if stat_col in adj_cols:
            stat_col = stat_col + suffix


        # Create the figure

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(
                y=sent.weighted,
                x=sent.index,
                name='Sentiment',
                line=dict(color='#FDB927')
            ),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(
                x=stats.GAME_DATE,
                y=stats[stat_col],
                name='{}'.format(stat_col),
                line=dict(color='#840DFA')
            ),
            secondary_y=True,
        )
        
        custom_template = templates["plotly_dark"]
        custom_template.layout["xaxis"]["showgrid"] = False
        custom_template.layout["yaxis"]["showgrid"] = False
        
        fig.update_yaxes(title_text="Rolling 20-day MA Sentiment Score", title_font=dict(color='#FDB927'), secondary_y=False)
        fig.update_yaxes(title_text="Rolling 20-day MA {}".format(stat_col), title_font=dict(color='#840DFA'), secondary_y=True)

        fig.update_layout(
                title='Rolling 20-day Sentiment vs {}'.format(stat_col),
                xaxis_title='Date',
                template=custom_template,
                plot_bgcolor='black',
                paper_bgcolor='black',
            )

        return fig

############################################################################################
def get_rolling_team_wpct_df(n=20, date='2023-04-10'):
    team = TeamDate("LAL", date=date)
    team_stats = team.stats
    idx = pd.period_range(min(team_stats.GAME_DATE), max(team_stats.GAME_DATE)).astype('datetime64[ns]')
    cols = ['wpct']
    dft = pd.DataFrame(columns=cols, index=idx)
    
    ws = []
    for i in idx:
        start = i - dt.timedelta(days=n)
        ww = team_stats[(team_stats.GAME_DATE > start) & (team_stats.GAME_DATE <= i)].reset_index().drop(columns=['index'])
        wins = ww.iloc[-1].W - ww.W[0]
        losses = ww.iloc[-1].L - ww.L[0]
        if wins + losses == 0:
            wpct = 0
        else:
            wpct = wins / (wins + losses)
        ws.append(wpct)
    dft['wpct'] = ws
    
    return dft

def sent_vs_wpct_corr(player_ref, date):
    sent = ss.get_rolling_sentiment_score_df(player_ref=player_ref, date=date)
    wpct = get_rolling_team_wpct_df(date=date)
    wpct.loc['2022-10-18'] = 0
    wpct.loc['2022-10-19'] = 0

    xmin = wpct.index.min()
    xmax = wpct.index.max()
    y = sent.loc[xmin:xmax]
    corr = y['weighted'].corr(wpct['wpct'])

    return corr

def sent_vs_wpct(player_ref, date):
    sent = ss.get_rolling_sentiment_score_df(player_ref=player_ref, date=date)
    wpct = get_rolling_team_wpct_df(date=date)
    wpct.loc['2022-10-18'] = 0
    wpct.loc['2022-10-19'] = 0

    # Create the figure
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            y=sent.weighted,
            x=sent.index,
            name='Sentiment',
            line=dict(color='#FDB927')
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=wpct.index,
            y=wpct['wpct'],
            name='{}'.format('wpct'),
            line=dict(color='#840DFA')
        ),
        secondary_y=True,
    )
    
    custom_template = templates["plotly_dark"]
    custom_template.layout["xaxis"]["showgrid"] = False
    custom_template.layout["yaxis"]["showgrid"] = False
    
    fig.update_yaxes(title_text="Rolling 20-day MA Sentiment Score", title_font=dict(color='#FDB927'), secondary_y=False)
    fig.update_yaxes(title_text="Rolling 20-day MA {}".format('wpct'), title_font=dict(color='#840DFA'), secondary_y=True)

    fig.update_layout(
            title='Rolling 20-day Sentiment vs {}'.format('wpct'),
            xaxis_title='Date',
            template=custom_template,
            plot_bgcolor='black',
            paper_bgcolor='black',
        )

    return fig













        
        
        
        
        
    
    
    