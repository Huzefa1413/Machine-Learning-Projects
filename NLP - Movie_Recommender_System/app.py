import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=579e066c7690788e44a22d167a7db7ab&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_link(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=579e066c7690788e44a22d167a7db7ab&language=en-US'.format(movie_id))
    data = response.json()
    return data['homepage']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_link = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
        recommended_movies_link.append(fetch_link(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_poster,recommended_movies_link

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Enter your favorite movie to get recommendations:',movies['title'].values)

def render_not_found():
    st.title("404 Not Found")
    st.write("The page you're looking for does not exist.")

if st.button('Recommend'):
    names,posters,link = recommend(selected_movie_name)
    col = st.columns(5) 
    for i in range(5):
        with col[i]:
            st.text(names[i])
            st.image(posters[i])
            if link[i]:
                st.markdown('<a href="{}" rel="noopener noreferrer">View Details</a>'.format(link[i]), unsafe_allow_html=True)