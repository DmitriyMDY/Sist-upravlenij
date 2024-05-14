Для реализации системы управления учетными
записями пользователей, разделения на обычных
сотрудников и администраторов, а также инкапсуляции
данных, можно создать следующие классы: User и Admin.

# Реализация классов
**Класс User:**

*Инкапсулирует данные о пользователе:* идентификатор, имя и уровень 
доступа.
Предоставляет методы для измерения атрибутов и установки 
(где необходимо).

_Инициализация :_ метод __init__определяет идентификатор, имя и уровень доступа.

_Методы доступа :_ Методы get_user_id, get_name, get_access_levelдля получения признаков атрибутов и set_nameдля изменения имени.

**КлассAdmin:**

_Наследует класс User._
Добавляет дополнительный атрибут уровня доступа, специфичный для 
администраторов.
Содержит методы add_userи remove_userдля управления списком 
пользователей.

_Наследование :_ Наследует User, переопределяет и дополняет функцию.

_Уровень доступа :_ Устанавливается в 'admin'.
![фото](https://avatars.dzeninfra.ru/get-zen_doc/1637352/pub_62d3b8f6ac1f664e51d629fb_62d3b94f73d68b4415d0e277/scale_1200)

_Методы управления пользователями :_ разрешать и удалять пользователей из списка add_user.remove_user

_Методget_users_list :_ Возвращает список пользователей.

Эта реализация обеспечивает аппаратуру инкапсуляции данных и 
обеспечивает методы для безопасного взаимодействия с атрибутами 
классов.
 
