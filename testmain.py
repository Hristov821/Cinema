from Controlers.MovieControler import MovieControler
from Controlers.ProjectionControler import ProjectionControler
from Controlers.ReservationControler import ReservationControler
from Controlers.ReservationControler import SeatIsTaken
from Controlers.UserControler import UserControler


class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return '{} {}'.format(self.id, self.name)


class Controler():

    def __init__(self):
        self.mv = MovieControler()
        self.pc = ProjectionControler()
        self.rc = ReservationControler()
        self.uc = UserControler()
        self.user = None
#    @user_exists

    def register_user(self, name, password):
        if self.uc.user_exist(name) is True:
            return False
        if self.uc.valid_password(password) is False:
            return False
        self.uc.register_user(name, password)
        return True

    def login_user(self, username, password):
        if self.uc.user_exist(username) is False:
            return False
        user = self.uc.get_user_by_name(username)
        user1 = self.uc.get_user_by_id(user[0])
        if self.uc.check_password(password, user[1], user[2]) is False:
            return False

        self.user = User(id=int(user[0]), name=username)
        return True

    def make_reservation(self, USER_ID, PROJECTION_ID, ROW, COL):
        try:
            self.rc.make_reservation(USER_ID, PROJECTION_ID, ROW, COL)
        except SeatIsTaken:
            return False
        # except Exception as ex:
        #     print(ex)
        #     return False
        return True

    def get_movies(self):
        return self.mv.get_all()

    def get_movie_projections(self, movie):
        return self.pc.get_movie_projections(movie)

    def get_all_taken_seats(self, PROJECTION_ID):
        return self.rc.get_all_taken_seats(PROJECTION_ID)

    def add_movie(self, name, rating):
        self.mv.insert(name, rating)

    def add_projections(self, MOVIE_ID, TYPE, DATE, TIME):
        self.pc.make_projection(MOVIE_ID, TYPE, DATE, TIME)

    def commit(self):
        self.mv.commit()
        self.pc.commit()
        self.rc.commit()
        self.uc.commit()


if __name__ == "__main__":
    controler = Controler()
    # controler.add_movie('Izgubeni dushi', 6.0)
    # controler.add_movie('Izgubeni dushi 2', 6.0)
    # controler.add_movie('Izgubeni dushi 3', 2.0)
    # controler.add_movie('Bavni i spokoini', 2)
    # controler.add_projections(1, "2D", "22-11-2016", "13:30")
    # controler.add_projections(2, '2D', '23-11-2016', '15:30')
    # controler.add_projections(3, '2D', '22-11-2016', '18:30')
    # controler.register_user('IVAN', 'A12*&11111')
    # controler.register_user('IVAN2', '2B*&2222')
    # controler.register_user('IVAN3', 'AK2*&3333')
    # controler.make_reservation(1, 1, 1, 1)
    # controler.make_reservation(2, 1, 2, 2)
    # controler.make_reservation(3, 1, 3, 3)
    # controler.make_reservation(3, 1, 4, 4)
    # controler.make_reservation(3, 1, 5, 5)
    print(controler.get_all_taken_seats(1))
