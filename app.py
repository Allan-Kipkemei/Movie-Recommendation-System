import streamlit as st
import joblib
import pandas as pd

# Load the model using joblib
model = joblib.load('./movie2.joblib')

# Load the DataFrame using joblib
movies_df = joblib.load('./movies.joblib')

# Function to get recommendations
def final_recommendations(movie_title, model, movies_df):
    # Assuming model has a method or function to get recommendations
    # Adjust this part according to your model's implementation
    # This is a placeholder implementation
    try:
        movie_index = movies_df[movies_df['title'].str.contains(movie_title, case=False, na=False)].index[0]
        distances, indices = model.kneighbors(movies_df.iloc[movie_index, :].values.reshape(1, -1), n_neighbors=6)
        recommendations = [movies_df.iloc[i]['title'] for i in indices.flatten()[1:]]
        return recommendations
    except IndexError:
        return ["No recommendations found. Please try a different movie title."]

# Streamlit UI
st.title('Movie Recommendation System')

# Input from the user
movie_title = st.text_input('Enter a movie title')

if movie_title:
    recommendations = final_recommendations(movie_title, model, movies_df)
    st.write('Recommended Movies:')
    for rec in recommendations:
        st.write(rec)
