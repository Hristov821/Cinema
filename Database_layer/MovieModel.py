
from .Connector import Connector
from .movie_queris import movie_queries


class MovieModel():
    def __init__(self):
        self.conn = Connector()

    def create_movie(self, name, rating):
        self.conn.execute_query(movie_queries.create(), (name, rating))

    def get_movies(self):
        return self.conn.all(movie_queries.movies())

    def get_movie_projections_by_date(self, movie, date):
        return self.conn.all(movie_queries.get_movie_projections_by_date,
                             (movie, date))

    def delete(self, name):
        self.conn.execute_query(movie_queries.delete(), (name,))

    def check_movie(self, movie):
        return self.conn.get(movie_queries.movie_count(), (movie,))

    def commit(self):
        self.conn.commit()
    # def movies_by_date(self, date):
    #     return self.conn.all(movie_queries.movie_projections(), (date,))
