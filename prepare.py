import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
from env import username, password, host
import os


def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.survived
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.survived,
    )
    return train, validate, test


    import pandas as pd


# Prepare Iris Data


def prep_iris(df):
    '''
    Takes in DataFrame from iris database and preps it as a DataFrame with prepped data
    '''
    df = df.drop_duplicates()
    df = df.drop(columns=['species_id', 'measurement_id'])
    df = df.rename(columns={'species_name' : 'species'})
    dummy_df = pd.get_dummies(df['species'], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df.drop(columns='species')