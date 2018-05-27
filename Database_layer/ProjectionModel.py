from .Connector import Connector
from .projection_queris import projection_queris


class ProjectionModel():

    def __init__(self):

        self.conn = Connector()

    def make_projection(self, MOVIE_ID, TYPE, DATE, TIME):
        self.conn.execute_query(
            projection_queris.make_projection(), (MOVIE_ID, TYPE, DATE, TIME))

    def check_projection(self, MOVIE_ID, TYPE, DATE, TIME):
        return self.conn.get(projection_queris.check_projection(),
                             (MOVIE_ID, TYPE, DATE, TIME))

    def get_movie_projections(self, movie):
        return self.conn.all(projection_queris.get_movie_projections(), (movie,))

    def commit(self):
        self.conn.commit()
