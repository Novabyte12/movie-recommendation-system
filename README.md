# 🎬 Movie Recommender System

A Machine Learning based **Movie Recommendation System** that recommends movies similar to the movie selected by the user.

The system uses **Content-Based Filtering** and Natural Language Processing (NLP) techniques to analyze movie information such as genres, keywords, cast, crew, and overview.

---

## 🚀 Live Demo

🔗 **Live App:** https://movie-recommendation-system-6w6rseunfa7manxhefegzh.streamlit.app/

---

## 📌 Features

- 🎥 Search and select a movie
- 🤖 Get recommendations for similar movies
- 🧠 Content-Based Recommendation
- 🔍 Uses NLP and text similarity
- 📊 Processes movie metadata
- ⚡ Fast movie recommendations
- 🌐 Interactive Streamlit web interface

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests

### Machine Learning / NLP
- Content-Based Filtering
- Count Vectorizer
- Cosine Similarity
- Natural Language Processing

### Dataset
- TMDB 5000 Movie Dataset

---

## 🧠 How It Works

The recommendation system works in the following steps:

### 1. Data Collection

The project uses the **TMDB 5000 Movie Dataset**, which contains information about thousands of movies.

Important features include:

- Movie title
- Overview
- Genres
- Keywords
- Cast
- Crew

### 2. Data Preprocessing

The movie metadata is cleaned and combined into a single text-based feature called `tags`.
