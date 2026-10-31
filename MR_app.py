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
    
    
# git init -- ti initialise .git file in your laptop/pc (make sure to install git on your laptop)
# git status -- simply tells you which stage you are at this poin in your project.
# git add . -- this create a list of file names you you want to upload, add . means include all files and 
## add "file_name" means on that specific file.
# git commit -m 'message' -- this package or segreagete content of all the file and changes which we just
## create/mentioned using add . command. -m just means a meesage, to remember what kind of upload we had 
## made last time.
# git remote add origin "url"-- add origin URL to connect url of your app from github to your laptop
# git branch -M main -- to create a specific folder or branch with the name as "main" in github, -M means renaiming
# git puch -u origin main -- to push or upload the changed files or changes to the main branch we created.