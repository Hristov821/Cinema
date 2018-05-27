
class projection_queris():

    @classmethod
    def make_projection(cls):
        return """
        INSERT INTO PROJECTION (MOVIE_ID, TYPE, DATE,TIME)
        VALUES (%s, %s, %s,%s)
        """

    @classmethod
    def check_projection(cls):
        return """
        SELECT COUNT(*)
        FROM PROJECTION
        WHERE MOVIE_ID = %s and
        TYPE = %s and DATE = %s
        and TIME = %s
        """


    @classmethod
    def get_movie_projections(cls):
        return """
        SELECT PROJECTION.ID , PROJECTION.DATE,PROJECTION.TIME,PROJECTION.TYPE,COUNT(*)
        FROM 
        PROJECTION 
        JOIN MOVIE
        ON PROJECTION.MOVIE_ID = MOVIE.ID
        JOIN RESERVATION
        ON RESERVATION.PROJECTION_ID = PROJECTION.ID
        WHERE MOVIE.NAME = %s
        GROUP BY(PROJECTION.ID)
        """


    # @classmethod
    # def get_movie_projections(cls):
    #     return """
    #     SELECT PROJECTION.ID , PROJECTION.DATE,PROJECTION.TIME,PROJECTION.TYPE,COUNT(*)
    #     FROM (
    #     select * FROM PROJECTION
    #     JOIN MOVIE
    #     ON PROJECTION.MOVIE_ID = MOVIE.ID
    #     JOIN RESERVATION
    #     ON RESERVATION.PROJECTION_ID = PROJECTION.ID
    #     WHERE MOVIE.NAME = %s
    #     AND RESERVATION.USER_ID = NULL
    #     )
    #     """