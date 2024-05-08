import csv
import json
import pandas as pd
from accounts.models import Title, Award, Genre, Name, Budget, Rating, TitleGenre
from django.contrib.auth.models import User

#  python manage.py runscript scripts.import_data

# Read CSV file into a DataFrame
csv_movies = '../movies_metadata.csv'
df = pd.read_csv(csv_movies, nrows=10, usecols=['id', 'overview', 'original_title', 'release_date', 'production_companies', 'genres'])
print(df.head())

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
    # Create the Title instance
    title = Title(
        title=row['original_title'],
        release_date=row['release_date'],
        producer=row['production_companies'],
        id=row['id'],
        overview=row['overview']
    )

    genres_json = eval(row['genres'])
    print(genres_json)
    for genre_data in genres_json:
        genre_id = genre_data['id']
        genre_name = genre_data['name']

        # Verificar si el género ya existe en la base de datos
        genre, created = Genre.objects.get_or_create(genre_id=genre_id, defaults={'genre_name': genre_name})
        TitleGenre.objects.create(title=title, genre=genre)

        # Si el género ya existe, actualiza el nombre si es necesario
        if not created and genre.genre_name != genre_name:
            genre.genre_name = genre_name
            genre.save()

    title.save()

csv_ratings = '../ratings_small.csv'
df = pd.read_csv(csv_ratings, nrows=10)
print(df.head())

for index, row in df.iterrows():
    # Create the Title instance
    rating = Rating(
        rating_value=row['rating'],
        movie_id=row['movieId'],
        user_id=row['userId'],
    )
    #to save the current title
    rating.save()

print("CSV data has been loaded into the Django database.")
