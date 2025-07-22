import streamlit as st
from src.recommender import MovieRecommender

# Load Recommender
MOVIES_PATH = 'data/movies.csv'
RATINGS_PATH = 'data/ratings.csv'
recommender = MovieRecommender(MOVIES_PATH, RATINGS_PATH)

# App UI
st.title("🎬Movie Suggestion Engine")
st.markdown("Get similar movies based on your favorite film.")

movie_input = st.text_input("Enter a movie name:", placeholder="e.g., Matrix, Toy Story")

if movie_input:
    movie_title, matched_titles, recommendations = recommender.get_similar_movies(movie_input)

    if matched_titles:
        st.success(f"Showing recommendations for: **{movie_title}**")
        st.write("Other matches:", matched_titles[:5])
        
        if not recommendations.empty:
            st.dataframe(recommendations.style.format({"Correlation": "{:.2f}", "NumRatings": "{:.0f}"}))
        else:
            st.warning("Not enough data to generate recommendations.")
    else:
        st.error("Movie not found. Please try it using another name.")
