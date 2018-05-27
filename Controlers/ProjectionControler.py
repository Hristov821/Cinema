from Database_layer.ProjectionModel import ProjectionModel
from .time_utils import is_time
from .time_utils import is_date


class ProjectionExist(Exception):
    pass


class ProjectionControler():

    def __init__(self):
        self.ProjectionModel = ProjectionModel()

    def make_projection(self, MOVIE_ID, TYPE, DATE, TIME):
        if type(MOVIE_ID) is not int:
            raise TypeError('MOVIE_ID MUST BE INT')
        if type(TYPE) is not str:
            raise TypeError('TYPE MUST BE STRING')
        if type(DATE) is not str:
            raise TypeError('DATE MUST BE STRING')
        if type(TIME) is not str:
            raise TypeError('TIME MUST BE STRING')
        if is_date(DATE) is False:
            raise ValueError('DATE IS NOT DATE')
        if is_time(TIME) is False:
            raise ValueError('TIME IS NOT TIME')
        if self.ProjectionModel.check_projection(MOVIE_ID, TYPE, DATE, TIME)[0] > 0:
            raise ProjectionExist('Projection already exists')
        self.ProjectionModel.make_projection(MOVIE_ID, TYPE, DATE, TIME)

    def get_movie_projections(self, movie):
        if type(movie) is not str:
            raise ValueError('MOVIE MUST BE STRING')
        return self.ProjectionModel.get_movie_projections(movie)



    def commit(self):
        self.ProjectionModel.commit()
