# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или
# другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса,
# к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = "https://c640435f-a1a4-448c-841c-418cdce4871a.serverhub.praktikum-services.ru"

# CREATE_USER_PATH хранит путь к API-методу для создания нового пользователя.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание пользователя.
CREATE_USER_PATH = "/api/v1/users/"

# PRODUCTS_KITS_PATH хранит путь к API-методу для создания нового набора.
# Эндпоинт для создания набора внутри конкретной карточки ИЛИ пользователя.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание набора.
CREATE_PRODUCTS_KITS_PATH = "/api/v1/kits"