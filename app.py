import streamlit as st
import pickle
import pandas as pd
import requests


# ---------------- FETCH POSTER ----------------
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)

    try:
        response = requests.get(url, timeout=1)
        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

    except requests.exceptions.RequestException:
        return None

    return None

# ---------------- LOAD DATA ----------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movies_list[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_names.append(
            movies.iloc[i[0]].title
        )

        recommended_movie_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movie_names, recommended_movie_posters


# ---------------- STREAMLIT UI ----------------
st.title('Movie Recommender System')

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):

    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(recommended_movie_names[0])
        if recommended_movie_posters[0]:
            st.image(recommended_movie_posters[0])
        else:
            st.write("Poster unavailable")

    with col2:
        st.write(recommended_movie_names[1])
        if recommended_movie_posters[1]:
            st.image(recommended_movie_posters[1])
        else:
            st.write("Poster unavailable")

    with col3:
        st.write(recommended_movie_names[2])
        if recommended_movie_posters[2]:
            st.image(recommended_movie_posters[2])
        else:
            st.write("Poster unavailable")

    with col4:
        st.write(recommended_movie_names[3])
        if recommended_movie_posters[3]:
            st.image(recommended_movie_posters[3])
        else:
            st.write("Poster unavailable")

    with col5:
        st.write(recommended_movie_names[4])
        if recommended_movie_posters[4]:
            st.image(recommended_movie_posters[4])
        else:
            st.write("Poster unavailable")