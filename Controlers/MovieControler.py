from Database_layer.MovieModel import MovieModel
from .time_utils import is_date


class FilmExist(Exception):
    pass


class FilmDoesntExist(Exception):
    pass


class MovieControler():
    pass

    def __init__(self):
        self.MovieModel = MovieModel()

    def insert(self, name, raiting):
        if type(name) is not str:
            raise TypeError('Name must be string')
        if type(raiting) not in [int, float]:
            raise TypeError('raiting must be number')
        if raiting <= 0 or raiting > 10:
            raise TypeError('raiting must be between 0 - 10')
        if self.MovieModel.check_movie(name)[0] > 0:
            raise FilmExist('Film Already exist')
        self.MovieModel.create_movie(name, raiting)

    def delete(self, name):
        self.MovieModel.delete((name,))

    def get_all(self):
        return self.MovieModel.get_movies()

    def get_movie_projections_by_date(self, movie, date):
        if type(movie) is not str:
            raise TypeError(" movie must be string")
        if is_date(date) is False:
            raise TypeError('date is not date')
        if self.MovieModel.check_movie(movie)[0] == 0:
            raise FilmDoesntExist("Movie doesnt exist")
        return self.MovieModel.get_movie_projections_by_date(movie, date)


    def commit(self):
        self.MovieModel.commit()