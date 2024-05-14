class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Методы для получения значений атрибутов
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Метод для установки имени
    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users_list = []

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User) and user not in self.__users_list:
            self.__users_list.append(user)
            print(f"User {user.get_name()} добавлен.")
        else:
            print("Недопустимый пользователь или пользователь, который уже существует.")

    # Метод для удаления пользователя
    def remove_user(self, user):
        if user in self.__users_list:
            self.__users_list.remove(user)
            print(f"User {user.get_name()} удалён.")
        else:
            print("Пользователь не найден.")

    # Метод для получения списка пользователей
    def get_users_list(self):
        return self.__users_list


# Пример использования
# Создание пользователей
user1 = User(1, "Агафья")
user2 = User(2, "Евстолий")

# Создание администратора
admin = Admin(99, "AdminUser")

# Администратор добавляет пользователей
admin.add_user(user1)  # Выведет: User Агафья added.
admin.add_user(user2)  # Выведет: User Евстолий added.

# Администратор пытается добавить того же пользователя снова
admin.add_user(user1)  # Выведет: Недопустимый пользователь или пользователь, который уже существует.

# Администратор удаляет пользователя
admin.remove_user(user1)  # Выведет: User Агафья removed.

# Попытка удалить несуществующего пользователя
admin.remove_user(user1)  # Выведет: Пользователь не найден.

# Получение списка пользователей
for user in admin.get_users_list():
    print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}")