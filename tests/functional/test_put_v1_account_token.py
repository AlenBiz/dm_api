from json import loads

import structlog

from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmConfiguration
from services.api_mailhog import MailHogApiAccount
from services.dm_api_account import DMApiAccount

from helpers.account_helpers import AccountHelper
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmConfiguration
from services.api_mailhog import MailHogApiAccount
from services.dm_api_account import DMApiAccount
from faker import Faker
import structlog
from faker import Faker

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, ensure_ascii=True, sort_keys=True)
    ]
)


def test_put_v1_account_token():
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_configuration = DmConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_configuration)
    mailhog = MailHogApiAccount(configuration=mailhog_configuration)
    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog)
    # Тестовые данные
    fake = Faker()
    login = fake.last_name() + fake.first_name()
    email = f'{login}@mail.ru'
    password = '12345678'

    # Регистация пользователя
    json_data = {
        'login': login,
        'email': email,
        'password': password
    }
    response = account.account_api.post_v1_account(json_data=json_data)
    print('Регистрация нового пользователя')
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f"Пользователь не был создан {response.json()}"

    # Авторизация
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True
    }
    response = account.login_api.post_v1_account_login(json_data=json_data)
    print('Авторизация без активации')
    assert response.status_code == 403, f"Пользователь {login} авторизировался без активации"

    # получить письма из почтового ящика
    response = mailhog.mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, f"Письма не были получены {response.json()}"

    # Получить активационный токен
    token = get_token_by_login(login, response)
    print('Получение токена')
    assert token is not None, f"Токен для пользователя {login} не был получен"

    # Активация пользователя
    response = account.account_api.put_v1_account_token(token=token)
    print('Активация пользователя')
    assert response.status_code == 200, f"Пользователь {login} не был активирован"

    account_helper.user_login_pass(login=login, password=password, rememberMe=True)


def get_token_by_login(login, response):
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
    return token
