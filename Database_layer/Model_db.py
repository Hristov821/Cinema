
from Connector import Connector
from movie_queris import movie_queries
from make_reservation_querie import reservation_queries
from user_queris import user_queries

class MovieModel():
    def __init__(self):
         self.conn = Connector()

    # @classmethod
    # def get_connector_and_cursor(cls):
    #     conn = psycopg2.connect("dbname='cinemadb' user='hristo'")
    #     cursor = conn.cursor()
    #     return(conn, cursor)

    # @classmethod
    # def format_tables(cls, table_colums, table_values):
    #     table = PrettyTable()
    #     for i in zip(table_colums, table_values):
    #         table.add_column(i[0], i[1])
    #     return table

    @classmethod
    def get_movies_and_rating(cls):
        conn, cursor = cls.get_connector_and_cursor()
        names = []
        ratings = []
        for i in cursor.execute(movie_queries.show_movies()):
            names.append(i[0])
            ratings.append(i[1])
        conn.close()
        return (names, ratings)

    @classmethod
    def movies_by_date(cls, date):
        conn, cursor = cls.get_connector_and_cursor()
        movie = []
        date = []
        time = []
        for i in cursor.execute(movie_queries.show_movie_projections()):
            movie.append(i[0])
            date.append(i[1])
            time.append(i[2])
        conn.close()
        return (movie, date, time)

    # @classmethod
    # def insert_user(cls, username, password, salt):
    #     conn, cursor = cls.get_connector_and_cursor()

    #     cursor.execute(user_queries.insert_user(),
    #                    (username, password, salt))
    #     conn.commit()
    #     conn.close()
    #     return True
