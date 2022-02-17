class Account:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def set_login(self, login):
        self.__login = login

    def get_login(self):
        return self.__login

    def set_pass(self, password):
        if len(password) > 8:
            self.__password = password
        else:
            raise Exception("Password must be longer than 8 characters")

    def get_pass(self):
        return self.__password

    def show(self):
        return f'Login : {self.get_login()} and pass: {self.get_pass()}' 

class all_accounts:
    acc = Account('A', "B")
    login = acc.get_login()
    password = acc.get_pass()

a1 = Account('n_turdalin', '123456')
# print(a1.show())
a1.set_pass('123')

    