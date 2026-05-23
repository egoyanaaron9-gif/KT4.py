class User:
    count = 0

    def __init__(self, name, login, password, rating):
        self.name = name
        self.login = login
        self._password = password
        self.rating = rating

        User.count += 1

    def show_info(self):
        print(f'Name: {self.name}, Login: {self.login}')

    def __lt__(self, other):
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating

    def __getattr__(self, item):
        return f'Неизвестное свойство {item}'

class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, rating):
        super().__init__(name, login, password, rating)
        self.role = role

        SuperUser.count += 1
        User.count -= 1

user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()

print(f'Всего обычных пользователей: {User.count}')
print(f'Всего супер-пользователей: {SuperUser.count}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Starr'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'   

print(user1.grade)
admin.grade = 10
