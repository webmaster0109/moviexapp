import streamlit as st
from imdb import IMDb
import requests

# Function to get movie details from OMDb API
def get_movie_details(movie_title):
    omdb_api_key = "d51dd885"  # Replace with your actual OMDb API key
    omdb_url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={movie_title}"

    response = requests.get(omdb_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display movie details
def display_movie_details(movie):
    with st.expander('Title', expanded=True):
        st.write(f"**Title:** {movie['Title']}")
    with st.expander('Year'):
        st.write(f"**Year:** {movie['Year']}")
    with st.expander('Genre'):
        st.write(f"**Genre:** {movie['Genre']}")
    with st.expander('Director'):
        st.write(f"**Director:** {movie['Director']}")
    with st.expander('IMDb Rating'):
        st.write(f"**IMDb Rating:** {movie['imdbRating']}")
    with st.expander('Movie Plot'):
        st.write(f"**Plot:** {movie['Plot']}")
    if movie['Poster'] != 'N/A':
        st.image(movie['Poster'], caption=movie['Title'], use_column_width=True)
    else:
        st.write('No Poster')

# Streamlit app
def main():
    st.title("Movie Information App")

    # User input for movie title
    movie_title = st.text_input("Enter the movie title:", "Walking Dead")

    if st.button("Search"):
        # Get movie details from OMDb API
        movie_details = get_movie_details(movie_title)

        if movie_details:
            # Display movie details
            display_movie_details(movie_details)
        else:
            st.error("Error fetching movie details. Please check your API key and try again.")

if __name__ == "__main__":
    main()
