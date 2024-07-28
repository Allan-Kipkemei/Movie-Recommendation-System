import streamlit as st
import pandas as pd
from recommendation import popularity_recommendation, user_user_recommendation, item_item_recommendation, content_based_recommendation

# Load data
merged_data = pd.read_csv('path/to/your/merged_data.csv')

# Streamlit UI
st.title('Movie Recommendation System')

option = st.selectbox(
    'Select Recommendation Method',
    ('Popularity-Based', 'User-User Collaborative Filtering', 'Item-Item Collaborative Filtering', 'Content-Based')
)

if option == 'Popularity-Based':
    top_n = st.slider('Number of Recommendations', 1, 20, 10)
    recommendations = popularity_recommendation(merged_data, top_n)
    st.write(f'Top {top_n} Popular Movies:')
    for movie in recommendations:
        st.write(movie)

elif option == 'User-User Collaborative Filtering':
    user_id = st.number_input('User ID', min_value=1, step=1)
    top_n = st.slider('Number of Recommendations', 1, 20, 10)
    if st.button('Recommend'):
        recommendations = user_user_recommendation(merged_data, user_id, top_n)
        st.write(f'Top {top_n} Recommendations for User {user_id}:')
        for movie in recommendations:
            st.write(movie)

elif option == 'Item-Item Collaborative Filtering':
    movie_title = st.text_input('Movie Title')
    top_n = st.slider('Number of Recommendations', 1, 20, 10)
    if st.button('Recommend'):
        recommendations = item_item_recommendation(merged_data, movie_title, top_n)
        st.write(f'Top {top_n} Movies Similar to {movie_title}:')
        for movie in recommendations:
            st.write(movie)

elif option == 'Content-Based':
    movie_title = st.text_input('Movie Title')
    top_n = st.slider('Number of Recommendations', 1, 20, 10)
    if st.button('Recommend'):
        recommendations = content_based_recommendation(merged_data, movie_title, top_n)
        st.write(f'Top {top_n} Movies Similar to {movie_title}:')
        for movie in recommendations:
            st.write(movie)
