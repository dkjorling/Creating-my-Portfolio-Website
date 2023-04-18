import pandas as pd
import numpy as np



def clean(data):
    # Turning languages into a binary variable (English or Multilingual/Foreign)
    data['languages'] = np.where(data['languages'] == 'English, None', 'English', data['languages'])
    data['languages'] = np.where(data['languages'] == 'None, English', 'English', data['languages'])
    data['languages'] = np.where(data['languages'] == 'None, French', 'French', data['languages'])
    data['languages'] = np.where(data['languages'].str.contains(','), 'Multilingual', data['languages'])
    data['languages'] = np.where(data['languages'] != 'English', 'Multilingual_Foreign', data['languages'])

    # Splitting genres variable so each row is a unique movie-genre combination
    data = data.set_index([i for i in data.columns if i != 'genres']).apply(
        lambda x: x.str.split(', ').explode()).reset_index()

    data['genre'] = np.where(data['genres'].isin([
    'Drama', 'Comedy', 'Action', 'Adventure', 'Crime',
    'Thriller', 'Romance', 'Horror', 'Mystery', 'Sci-Fi',
    'Fantasy', 'Biography', 'Family', 'Animation']),
    data['genres'], 'Other')

    # Cleaning rating
    data['rating'] = np.where(data['rating'].isin(['PG', 'PG-13', 'R']), data['rating'], 'Other')


    # Creating categorical company size (this mimics what we did in Spring 2022)
    data['company_size_cat'] = 1
    data['company_size_cat'] = np.where((data['company_size'] > 8) & (data['company_size'] <= 44), 2, data['company_size_cat'])

    data['company_size_cat'] = np.where((data['company_size'] > 44) & (data['company_size'] <= 179), 3, data['company_size_cat'])

    data['company_size_cat'] = np.where((data['company_size'] > 179), 4, data['company_size_cat'])

    # Creating categorical release period (this mimics what we did in Spring 2022)
    data['release_period'] = 'Spring'
    data['release_period'] = np.where((data['release_month'] == 'June') |
                                     (data['release_month'] == 'July') |
                                     (data['release_month'] == 'August'),
                                     'Summer', data['release_period'])

    data['release_period'] = np.where((data['release_month'] == 'September') |
                                     (data['release_month'] == 'October') |
                                     (data['release_month'] == 'November'),
                                     'Fall', data['release_period'])

    data['release_period'] = np.where((data['release_month'] == 'December') |
                                     (data['release_month'] == 'January') |
                                     (data['release_month'] == 'February'),
                                     'Winter', data['release_period'])
    
    return data


def sortSur(nameList):
    l2 = []
 
    # create 2d list of names
    for ele in nameList:
        l2.append(ele.split())
    nameList = []
 
    # sort by last name
    for ele in sorted(l2, key=lambda x: x[-1]):
        nameList.append(' '.join(ele))
 
    # return sorted list
    return nameList
