

class movie_queries():

    @classmethod
    def movies(cls):
        return """
        SELECT MOVIE.ID,MOVIE.Name, MOVIE.RAITING FROM MOVIE
        ORDER BY (ID,RAITING)
        """

    @classmethod
    def movie_projections(cls):
        return """
        SELECT MOVIE.NAME,PROJECTION.DATE,PROJECTION.TIME
        FROM PROJECTION
        JOIN MOVIE
        ON PROJECTION.MOVIE_ID = MOVIE.ID
        WHERE PROJECTION.DATE = :DATE AND
        MOVIE.NAME = :MOVIE_NAME
        ORDER BY (PROJECTION.DATE)
        """

    @classmethod
    def create(cls):
        return """
        INSERT INTO movie (name, RAITING)
        VALUES (%s, %s)
        """

    @classmethod
    def delete(cls):
        return """
        DELETE from Movie
        WHERE Name = %s
        """

    @classmethod
    def movie_count(cls):
        return """
        SELECT COUNT(*)
        FROM MOVIE
        WHERE NAME = %s
        """
