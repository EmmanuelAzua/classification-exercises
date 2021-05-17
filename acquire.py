
import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
from env import username, password, host
import os

def get_db_url(username, password, host):
    '''This function creates the url that allows access to the
    different Codeup datasets'''
    from env import username, password, host
    url = f'mysql+pymysql://{username}:{password}@{host}/employees'
    return url

# url = get_db_url(username, password, host)

# def get_titanic_data():
#     '''
#     This function reads in the titanic data from the Codeup db
#     and returns a pandas DataFrame with all columns.
#     '''
#     import pandas as pd
#     if os.path.isfile('titanic_df.csv'):
#         df = new_titanic_data()
#     else:
#         df = new_titanic_data()
#         df.to_csv('titanic_df.csv')
#     sql_query = 'SELECT * FROM passengers'
#     return pd.read_sql(sql_query, get_db_url('titanic_db'))
    
# def get_iris_data():
#     '''
#     This function reads in the titanic data from the Codeup db
#     and returns a pandas DataFrame with all columns.
#     '''
#     sql_query = 'SELECT * FROM species'
#     return pd.read_sql(sql_query, get_db_url('iris_db'))

def get_connection(db, username=username, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

def new_titanic_data():
    '''
    This function reads in the titanic data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = 'SELECT * FROM passengers'
    return pd.read_sql(sql_query, get_connection('titanic_db'))

def get_iris_data():
    '''
    This function reads in the iris data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = '''SELECT *
                FROM species
                JOIN measurements
                USING(species_id)'''
    return pd.read_sql(sql_query, get_connection('iris_db'))


def get_iris_data_csv():
    return pd.read_csv("iris_df.csv")