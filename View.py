from testmain import Controler
import getpass
import os


class View():

    def __init__(self):
        self.controler = Controler()

    def print_room(self, projection_id):
        taken_seats = self.controler.get_all_taken_seats(projection_id)
        print(end='  ')
        for i in range(1, 11):
            print(i, end='  ')
        print()
        for i in range(1, 11):
            print(i, end='  ')
            for j in range(1, 11):
                if (i, j) in taken_seats:
                    print('X ', end=' ')
                else:
                    print('. ', end=' ')
            print()

    def print_movies(self):
        self.clear()
        for i in self.controler.get_movies():
            print('[{}] - {} ({})'.format(i[0], i[1], i[2]))

    def print_movie_projections(self, movie):
        self.clear()
        if len(self.controler.get_movie_projections(movie)) == 0:
            return False
        for i in self.controler.get_movie_projections(movie):
            print('[{}] {}-{} ({}) - Avalible_spots {}'.format(i[0],
                                                               i[1], i[2], i[3], 100 - i[4]))
        return True

    def clear(self):
        os.system('cls||clear')

    def user_logged(self):
        if self.controler.user == None:
            return False
        return True

    def register_user(self):
        username = input('Username = ')
        password = getpass.getpass('Password')
        while self.controler.register_user(username, password) is False:
            print('User Exist')
            username = input('Username = ')
            password = getpass.getpass('Password')
            self.clear()
        self.clear()

        self.finalize()
        self.controler.login_user(username, password)

    def login(self):
        username = input('Username ')
        password = getpass.getpass('Password')
        while self.controler.login_user(username, password) is False:
            print('Invalid password or username try again ')
            username = input('Username ')
            password = getpass.getpass('Password')

    def finalize(self):
        self.controler.commit()

    def make_reservation(self):
        if self.user_logged() is False:
            self.register_user()
        try:
            num_tickets = int(input('Pick number of tickets  = '))
            projection_id = int(input('Pick projection id'))
        except ValueError:
            print('tickets and id must be int')
            pass
        self.print_room(projection_id)
        while (100 - len(self.controler.get_all_taken_seats(projection_id))) < num_tickets:
            print('Not enoght seats')
            num_tickets = int(input('Pick number of tickets  '))
            self.clear()
        for i in range(num_tickets):
            row = int(input('Row '))
            col = int(input('Col '))
            while self.controler.make_reservation(
                    (self.controler.user.id), projection_id, row, col)is False:
                print('seat is taken pick again')
                row = int(input('Row '))
                col = int(input('Col '))
            self.clear()
            self.print_room(projection_id)

    def options(self):
        self.clear()
        print('Options :')
        print('make reservation')
        print('show movie projections')
        print('show movies')
        print('login')
        print('finalize')
        print('options')
        print('register')
        print('exit')
