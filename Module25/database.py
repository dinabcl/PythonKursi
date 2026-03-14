import sqlite3

from Module24.database import connection
from Module24.joinexample import cursor
from models import Movie, MovieCreate

def create_connection():
    connection =  sqlite3.connect('movies.db')
    connection.row_factory = sqlite3.Row
    return connection

def create_tabel():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        create table if not exists movies (
            id integer primary key autoincrement,
            title text not null,
            director text not null
        )
    ''')
    connection.commit()
    connection.close()

create_tabel()

def create_movie(movies: MovieCreate) -> int:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        insert into movies (title, director) values (?,?)
    ''', (movies.title, movies.director))
    connection.commit()
    lastmovie = movies.lastrowid
    connection.close()
    return lastmovie

def read_movies():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        ''' select * from movies'''
    )
    rows = cursor.fetchall()
    connection.close()
    movies = [Movie(id = row[0], title = row[1], director = row[2]) for row in rows]
    return movies

def read_movie(movie_id = int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        select * from movies where id = ?
    ''', (movie_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        print("Nothing was found")
    movie = Movie(id = row['id'], title = row['title'], director = row['director'])
    return movie

def update_movie(movie_id, movie: MovieCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        update movies set title = ?, director = ? where id = ?
    ''', (movie.title, movie.director, movie_id ))
    connection.close()
    updated = cursor.rowcount
    connection.close()
    return  updated > 0

def delete_movie(movie_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('delete from movies where id =?', (movie_id, ))
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0