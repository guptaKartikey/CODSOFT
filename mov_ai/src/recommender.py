import pandas as pd

class MovieRecommender:
    def __init__(self, movies_path, ratings_path):
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        self.data = pd.merge(self.ratings, self.movies, on="movieId")
        self.user_movie_matrix = self.data.pivot_table(index='userId', columns='title', values='rating')

    def get_similar_movies(self, movie_title, min_ratings=10):
       matched_titles = [title for title in self.user_movie_matrix.columns if movie_title.lower() in title.lower()]
       if not matched_titles:
         return None, None, []
    
       movie_title = matched_titles[0]
    
       target_ratings = self.user_movie_matrix[movie_title]
       similarity = self.user_movie_matrix.corrwith(target_ratings)

       corr_df = pd.DataFrame(similarity, columns=['Correlation'])
       corr_df.dropna(inplace=True)

       rating_counts = self.data.groupby('title')['rating'].count()
       corr_df = corr_df.join(rating_counts.rename("NumRatings"))

       recommendations = corr_df[corr_df['NumRatings'] >= min_ratings].sort_values('Correlation', ascending=False)
       return movie_title, matched_titles, recommendations.head(10)
