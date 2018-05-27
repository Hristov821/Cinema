from View import View



class menu():

    def __init__(self):
        self.view = View()

    def run(self):
        self.view.options()
        comand = input('-->> ')
        while comand.lower() != 'exit':
            if comand.lower() == 'make reservation':
                self.view.make_reservation()
            if comand.lower() == 'show movie projections':
                movie_name = input('Movie name ')
                while self.view.print_movie_projections(movie_name) is False:
                    print('Wrong name or film doesnt exist type again')
                    movie_name = input('Movie name ')

            if comand.lower() == 'show movies':
                self.view.print_movies()
            if comand.lower() == 'login':
                self.view.login()
            if comand.lower() == 'finalize':
                self.view.finalize()
            if comand.lower() == 'options':
                self.view.options()
            if comand.lower() == 'register':
                self.view.register_user()
            comand = input('-->>')


menu = menu()
menu.run()
