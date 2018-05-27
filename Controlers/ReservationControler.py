from Database_layer.ReservationModel import ReservationModel


class SeatIsTaken(Exception):
    pass


class ReservationControler():

    def __init__(self):
        self.ReservationModel = ReservationModel()

    def check_seat_taken(self, ROW, COL, PROJECTION_ID):
        if self.ReservationModel.check_reservation(ROW, COL, PROJECTION_ID)[0] > 0:
            return True
        return False

    def projection_exist(self, PROJECTION_ID):
        if self.ReservationModel.check_projection(PROJECTION_ID)[0] > 0:
            return True
        return False

    def make_reservation(self, USER_ID, PROJECTION_ID, ROW, COL):
        if type(USER_ID) is not int:
            raise TypeError('USER_ID MUST BE INT')
        if type(PROJECTION_ID) is not int:
            raise TypeError('PROJECTION_ID MUST BE INT')
        if type(ROW) is not int:
            raise TypeError('ROW MUST BE INT')
        if type(COL) is not int:
            raise TypeError('COL MUST BE INT')
        if ROW > 10 or ROW < 1:
            raise ValueError('row must be between 1 and 10')

        if COL > 10 or COL < 1:
            raise ValueError('col must be between 1 and 10')

        # if self.projection_exist(PROJECTION_ID) is True:
        #     raise ValueError('Projection doesnt exist')

        if self.check_seat_taken(ROW, COL, PROJECTION_ID) is True:
            raise SeatIsTaken('Seat is taken')

        self.ReservationModel.make_reservation(
            USER_ID, PROJECTION_ID, ROW, COL)

    def get_all_taken_seats(self, PROJECTION_ID):
        if type(PROJECTION_ID) is not int:
            raise TypeError('PROJECTION_ID MUST BE INT')
        # if self.projection_exist(PROJECTION_ID) is False:
        #     raise ValueError('Projection doesnt exist')
        return self.ReservationModel.get_all_taken_seats(PROJECTION_ID)



    def commit(self):
        self.ReservationModel.commit()