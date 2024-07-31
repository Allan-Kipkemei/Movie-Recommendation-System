import streamlit as st
import pickle
import pandas as pd


# Load the model
with open('knn_pv.joblib', 'rb') as file:
    model = pickle.load(file)

# Function to get recommendations
def get_recommendations(movie_title, model, movies_df):
    # Assuming model is a function that takes a movie title and returns recommendations
    return model.get_recommendations(movie_title)

# Load movie data
movies_df = pd.read_csv('./datasets/ml-latest-small/movies.csv')  # Update this if your dataset is different

# Streamlit UI
st.title('Movie Recommendation System')

# Input from the user
movie_title = st.text_input('Enter a movie title')

if movie_title:
    recommendations = get_recommendations(movie_title, model, movies_df)
    st.write('Recommended Movies:')
    for rec in recommendations:
        st.write(rec)



