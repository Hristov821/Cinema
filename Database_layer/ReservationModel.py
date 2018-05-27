from .make_reservation_querie import reservation_queries
from .Connector import Connector


class ReservationModel():

    def __init__(self):

        self.conn = Connector()

    def make_reservation(self, USER_ID, PROJECTION_ID, ROW, COL):
        self.conn.execute_query(
            reservation_queries.make_reservation(),
            (USER_ID, PROJECTION_ID, ROW, COL))

    def check_reservation(self, ROW, COL, PROJECTION_ID):
        return self.conn.get(reservation_queries.check_reservation(),
                             (ROW, COL, PROJECTION_ID))

    def get_all_taken_seats(self,PROJECTION_ID):
        return self.conn.all(reservation_queries.get_all_taken_seats(),
                             (PROJECTION_ID,))

    def check_projection(self, PROJECTION_ID):
        return self.conn.get(reservation_queries.check_projection(),
                             (PROJECTION_ID,))

    def commit(self):
        self.conn.commit()