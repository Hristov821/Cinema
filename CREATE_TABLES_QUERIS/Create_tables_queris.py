

class create_queries():
    @classmethod
    def create_movie(cls):
        return """
            Create table MOVIE(
            ID SERIAL PRIMARY KEY ,
            Name varchar(255) NOT NULL,
            RAITING real NOT NULL
            )
            """

    @classmethod
    def create_projection(cls):
        return """
            Create table PROJECTION(
            ID SERIAL PRIMARY KEY ,
            MOVIE_ID INT NOT NULL,
            TYPE VARCHAR(255) NOT NULL,
            DATE DATE NOT NULL,
            TIME TIME NOT NULL,
            FOREIGN KEY (MOVIE_ID) 
            REFERENCES MOVIE (ID),
            UNIQUE (MOVIE_ID,TYPE,DATE,TIME)
            )
            """

    @classmethod
    def create_user(cls):
        return """
            CREATE TABLE USERS(
            ID SERIAL PRIMARY KEY,
            USERNAME VARCHAR(255) NOT NULL,
            PASSWORD VARCHAR(600) NOT NULL,
            SALT VARCHAR(255) NOT NULL
            )
            """

    @classmethod
    def create_reservation(cls):
        return """
            CREATE TABLE RESERVATION(
            ID SERIAL PRIMARY KEY,
            USER_ID INT NULL,
            PROJECTION_ID INT NOT NULL,
            ROW INT NOT NULL,
            COL INT NOT NULL,
            FOREIGN KEY(USER_ID) REFERENCES USERS(ID),
            FOREIGN KEY(PROJECTION_ID) REFERENCES PROJECTION(ID),
            CHECK (ROW > 0 and ROW < 11),
            CHECK (COL > 0 AND COL <11),
            UNIQUE (ROW,COL,PROJECTION_ID)
            )
        """
