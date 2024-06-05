import pprint
from json import loads
import requests

def test_post_v1_account():
    # Тестовые данные
    login = 'biziaeva99'
    email = f'{login}@mail.ru'
    password = '12345678'

    # регистация пользователя
    json_data = {
        'login': login,
        'email': email,
        'password': password
    }
    response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f"Пользователь не был создан {response.json()}"

    # получить письма из почтового ящика
    params = {
        'limit': '50'
    }
    response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    assert response.status_code == 200, f"Письма не были получены {response.json()}"

    # Получить активационный токен
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]

    assert token is not None, f"Токен для пользователя {login} не был получен"

    # Активация пользователя

    response = requests.put(f'http://5.63.153.31:5051/v1/account/{token}')
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Пользователь {login} не был активирован"
    # Авторизация

    json_data = {
        'login': login,
        'email': email,
        'password': password
    }

    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"Пользователь {login} не смог авторизоваться"