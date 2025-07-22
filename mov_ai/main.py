from src.recommender import MovieRecommender
import streamlit as st
from src.recommender import MovieRecommender
import streamlit as st
  

# Load Recommender
MOVIES_PATH = 'data/movies.csv'
RATINGS_PATH = 'data/ratings.csv'
recommender = MovieRecommender(MOVIES_PATH, RATINGS_PATH)

# App UI
st.title("🎬 Movie Recommendation System")
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
        st.error("Movie not found. Please try another name.")

MOVIES_PATH = 'data/movies.csv'
RATINGS_PATH = 'data/ratings.csv'

recommender = MovieRecommender(MOVIES_PATH, RATINGS_PATH)

print("\nHere are some sample movies you can try:")
print(recommender.user_movie_matrix.columns[:20])

print("\nTry these movies:")
print(recommender.user_movie_matrix.columns[:20])

movie = input("\nEnter a movie you like: ")

try:
    matched_movie, recommendations = recommender.get_similar_movies(movie)
    print(f"\nRecommendations based on: {matched_movie}\n")
    print(recommendations)
except ValueError as e:
    print(e)
