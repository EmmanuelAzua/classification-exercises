
import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
from env import username, password, host
import os


def get_connection(db, user=username, host=host, password=password):
    '''
    This function makes a connection with and pulls from the CodeUp database. It 
    takes the database name as its argument, pulls other login info from env.py.
    Make sure you save this as a variable or it will print out your sensitive user
    info as plain text. 
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# these functions below will pull dbs as dataframes from the codeup database if it hasnt already
# if it has, it will write a cache. 
def get_titanic_data():
    '''
    This function pulls the titanic db into a dataframe if it doesnt exist, or it will cache 
    the titanic data into a .csv file. 
    '''
    filename = 'titanic.csv'
    if os.path.isfile(filename):
        titanic_df = pd.read_csv(filename, index_col=0)
        return titanic_df
    else:
        titanic_df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        titanic_df.to_csv(filename, mode = 'w+')
        return titanic_df
    
def get_iris_data():
    ''' This function pulls the iris db into a dataframe, or caches it as a .csv if it hasnt been already.
    '''
    filename = 'iris.csv'
    if os.path.isfile(filename):
        iris_df = pd.read_csv(filename, index_col=0)
        return iris_df
    else:
        iris_df = pd.read_sql('SELECT * FROM measurements JOIN species USING(species_id);', get_connection('iris_db'))
        iris_df.to_csv(filename)
        return iris_df

def telco_churn_data():
    '''
    This function pulls the telco_churn dataset and turns it into a python-ready dataframe,
    '''
    # Wrap the process of creating a SQL query into python function structure
    sql_query = '''select *
    from customers
    join contract_types using(contract_type_id)
    join internet_service_types using(internet_service_type_id)
    join payment_types using(payment_type_id)'''
    # Returns the SQL dataset as a python-ready dataframe
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df


def churn_data_csv(cached = False):
    '''
    This function pulls in the telco_churn database, saves it as a csv file, and returns a pandas dataframe
    '''
    if cached == False or os.path.isfile('telco_churn.csv') == False:
        df = telco_churn_data()
        df.to_csv('telco_churn_df.csv')
    else:
        df = pd.read_csv('telco_churn_df.csv', index_col=0)
    return df