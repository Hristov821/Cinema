
    # USER_ID INT NOT NULL,
    # PROJECTION_ID INT NOT NULL,
    # ROW INT NOT NULL,
    # COL INT NOT NULL,


class reservation_queries():
    @classmethod
    def make_reservation(cls):
        return """
        INSERT INTO RESERVATION (USER_ID, PROJECTION_ID, ROW,COL)
        VALUES (%s, %s, %s,%s)
        """

    @classmethod
    def check_reservation(cls):
        return """
        SELECT COUNT(*)
        FROM RESERVATION
        WHERE ROW = %s and COL = %s
        and PROJECTION_ID = %s
        """

    @classmethod
    def check_projection(cls):
        return """
        SELECT COUNT(*)
        FROM RESERVATION
        WHERE PROJECTION_ID = %s
        """
        
    @classmethod
    def get_all_taken_seats(cls):
        return """
        SELECT ROW , COL
        FROM RESERVATION
        WHERE PROJECTION_ID = %s
        AND USER_ID is NOT NULL
        """
