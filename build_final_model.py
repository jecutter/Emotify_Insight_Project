import numpy as np
import pandas as pd
import re 
import sklearn
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import mean_squared_error
from sklearn.utils import resample
from sklearn.pipeline import Pipeline
import os 
import sys 
import pickle
import joblib


#####
# Instrumental Portion
#####

# Read in complete dataset
df_ds = pd.read_csv('Total_Spotify_4Emotion_AllParts.csv')

# Get lyrics for each song in the training dataset
df_ds = df_ds.dropna()
df_ds = df_ds.drop_duplicates(['artist', 'title'])

# Create a linear loudness variable by converting from decibels to gain
df_ds['loudness_linear'] = 10**(df_ds['loudness']/20.)

# Isolate instrumental music
df_inst = df_ds[(df_ds['instrumentalness'] > 0.45) & (df_ds['speechiness'] < 0.33)]

# Reduce the lyrics training set to only include 'happy', 'sad', and 'angry'
df_inst_red = df_inst[df_inst.overall_emotion != 'calm']

# Input features
features = df_inst_red[['danceability', 'energy', 'loudness_linear', 'speechiness',
       'acousticness', 'instrumentalness', 'valence', 'tempo', 'duration_ms']]

# Output labels for emotion classification
labels = df_inst_red[['overall_emotion']]

# Create training/testing split
x_train, x_test, y_train, y_test = train_test_split(features, labels)
print("Using a training dataset of size:", len(x_train))
print("Using a test dataset of size:", len(x_test))

# Scale features which will be used in model fitting
# (for both training and testing datasets)
scale = StandardScaler().fit(x_train)
train_features = scale.transform(x_train)

# Fit the training dataset
clf = LogisticRegression(
    C=0.004832930238571752,
		penalty='l2',
		solver='liblinear',
    random_state = 1)
clf.fit(train_features, y_train.values.ravel())

# Dump model to pickle file
pickle.dump(scale, open('best_inst_scale.pkl', 'wb'))
pickle.dump(clf, open('best_inst_rfc.pkl', 'wb'))


#####
# Lyrical Portion
#####

# Read in full lyrical training set
df_lyrics = pd.read_csv('GeniusLyrics_VocalsOnlySet_FullFinal_withSentScores.csv')

# Reduce the lyrics training set to only include 'happy', 'sad', and 'angry'
df_lyrics_red = df_lyrics[df_lyrics.overall_emotion != 'calm']

# Input features
features = df_lyrics_red[['sent_score', 'danceability', 'energy', 'key', 'loudness_linear', 
            'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
            'valence', 'tempo', 'duration_ms', 'mode', 'time_signature']]

# Output labels for emotion classification
labels = df_lyrics_red[['overall_emotion']]

# Create training/testing split
#x_train, x_test, y_train, y_test = split_by_emotion(features, labels)
x_train, x_test, y_train, y_test = train_test_split(features, labels)
print("Using a training dataset of size:", len(x_train))
print("Using a test dataset of size:", len(x_test))

# Scale features which will be used in model fitting
# (for both training and testing datasets)
scale = StandardScaler().fit(x_train)
train_features = scale.transform(x_train)

# Fit the training dataset
clf = RandomForestClassifier(
    n_estimators=500, 
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=1, 
    random_state = 1)
clf.fit(train_features, y_train.values.ravel())

# Set up pipeline for a Random Forest model
#clf_pipe = Pipeline([
#                    ('scale', StandardScaler()),
#                    ('clf', RandomForestClassifier(random_state=1))
#                    ])
#
#parameters = {
#							'clf__n_estimators' : 2000,
#              'clf__max_depth' : 30,
#              'clf__min_samples_split' : 2,
#              'clf__min_samples_leaf' : 1 
#             }

# Fit the training dataset
#clf_pipe.fit(x_train, y_train.values.ravel())

# Dump model to pickle file
pickle.dump(scale, open('best_lyrical_scale.pkl', 'wb'))
pickle.dump(clf, open('best_lyrical_rfc.pkl', 'wb'))


