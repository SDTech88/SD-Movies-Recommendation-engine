import streamlit as st 
import pandas as pd
import pickle 
import joblib


st.title('Movie recomendation engine')

with open("movies.pickel", 'rb') as m:
    db_movies=pickle.load(m) # this has db of movies in it
    
simi = joblib.load('simlarity.joblib')
    
movies_names = db_movies['title'].values

def recommend(name_movie):
    
    movie_index = db_movies[db_movies['title']==name_movie].index[0] 
    
    recommendation = simi[movie_index]  # This will check with every movie and comapre similartity
    
    movie_list = sorted(enumerate(recommendation),reverse=True, key=lambda x:x[1])[1:6]
    
    
    recommended_list = []
    for i in movie_list:
        recommended_list.append(db_movies.iloc[i[0]].title)
    return recommended_list

st_box = st.selectbox('Enter the Movie name', movies_names)

if st.button("Recommend"):
    r = recommend(st_box)
    st.write("The Recomended Movies are...")
    
    for i in r:
        st.write(i)
    
    
    