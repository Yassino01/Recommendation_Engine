import pandas as pd
import numpy as np


PATH_DATA = "../data/"

# load csv file
def load_data(PATH=PATH_DATA):
    users = pd.read_csv(PATH+"users.csv")
    movies= pd.read_csv(PATH+"movies.csv")
    ratings=pd.read_csv(PATH+"ratings.csv")
    
    return users,movies,ratings
    

# Split ratings train/test depending on users.
def split(data, n_user_test,seed = 42):
    np.random.seed(seed)
    df = data.copy()

    unique_user = df['user_id'].unique().astype(int)
    np.random.shuffle(unique_user)
    test_user = unique_user[:n_user_test]
    train_user = unique_user[n_user_test:]
    
    mask_train = df['user_id'].isin(train_user)
    mask_test = df['user_id'].isin(test_user)
    return df[mask_train], df[mask_test]
  