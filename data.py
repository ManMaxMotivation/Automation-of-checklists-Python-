# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
# передаём заголовок Authorization. Авторизационный заголовок в формате Bearer {authToken}. При передаче - возвращает все наборы, созданные пользователем.
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "
}

# данные пользователя для создания новой записи пользователя в системе
# содержат имя пользователя, телефон и адрес
user_body = {
    "firstName": "Марс",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

# данные набора для создания нового набора в системе
# содержат имя набора
kit_body = {
       "name": "Набор"
   }