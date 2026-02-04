from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pandas as pd
import pickle
import requests

@st.cache_resource
def generate_similarity():
    emb = pickle.load(open('movie_embeddings.pkl', 'rb'))
    similarity = cosine_similarity(emb)
    return similarity

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=bf5c70a746c427d3eaa97b42ac5e406a&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# main pipeline
def recommend(movie, similarity, k = 5):
    try:
        index = movies[movies['title'] == movie].index[0]         
        distances = similarity[index]
        
        sorted_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:k+1]
        # print(sorted_list)

        rec_list = []
        rec_posters = []
        for i in sorted_list:
            rec_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
            rec_list.append((movies.iloc[i[0]].title, i[1]))

        return rec_list, rec_posters
    except:
        st.write("Movie not found in dataset")


st.title("Content-based Movie Recommender")

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

option = st.selectbox(
    'Which movie do you like?',
    movies_list) 

num = st.slider('Select number of recommendations', 1, 20, 5)

selected_movie = option
selected_movie_index = movies[movies['title'] == option].index[0]

if st.button('Show Recommendations'):
    # similarity = pickle.load(open('similarity_st.pkl', 'rb'))
    similarity = generate_similarity()
    recommendations, recommendation_posters = recommend(selected_movie, similarity, num)
    st.write("Top 5 recommendations for:", selected_movie)

    cols = st.columns(3)
    for i in range(len(recommendations)):
        with cols[i % 3]:
            st.subheader(recommendations[i][0])
            st.image(recommendation_posters[i])
     