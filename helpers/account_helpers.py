from json import loads

from api_mailhog.apis.mailhog_api import MailhogApi
from services.dm_api_account import DMApiAccount


class AccountHelper:
    def __init__(
            self,
            dm_account_api: DMApiAccount,
            mailhog: MailhogApi
    ):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog

    def register_new_user(
            self,
            login: str,
            password: str,
            email: str
    ):
        json_data = {
            'login': login,
            'email': email,
            'password': password
        }
        response = self.dm_account_api.account_api.post_v1_account(json_data=json_data)
        assert response.status_code == 201, f"Пользователь не был создан {response.json()}"
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        assert response.status_code == 200, f"Письма не были получены {response.json()}"
        token = self.get_activation_token_by_login(login=login, response=response)
        assert token is not None, f"Токен для пользователя {login} не был получен"
        response = self.dm_account_api.account_api.put_v1_account_token(token=token)
        assert response.status_code == 200, f"Пользователь {login} не был активирован"

    @staticmethod
    def get_activation_token_by_login(
            login,
            response):
        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            user_login = user_data['Login']
            if user_login == login:
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
        return token

    def user_login_pass(
            self,
            login: str,
            password: str,
            rememberMe: bool = True
    ):
        json_data = {
            'login': login,
            'password': password,
            'rememberMe': rememberMe
        }
        response = self.dm_account_api.login_api.post_v1_account_login(json_data=json_data)
        assert response.status_code == 200, f"Пользователь {login} не смог авторизоваться"
        return response

    def user_login_fail(
            self,
            login: str,
            password: str,
            rememberMe: bool = True
    ):
        json_data = {
            'login': login,
            'password': password,
            'rememberMe': rememberMe
        }
        response = self.dm_account_api.login_api.post_v1_account_login(json_data=json_data)
        assert response.status_code == 403, f"Пользователь {login} смог авторизоваться, требуется активация"
        return response

    def user_change_email(
            self,
            login: str,
            password: str,
            new_email: str
    ):
        json_data = {
            'login': login,
            'password': password,
            'email': new_email
        }
        response = self.dm_account_api.account_api.put_account_email(json_data=json_data)
        assert response.status_code == 200, f"Пользователь {login} не смог поменять поменять почту"
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        assert response.status_code == 200, f"Письма не были получены {response.json()}"
        token = self.get_activation_token_by_login(login=login, response=response)
        assert token is not None, f"Токен для пользователя {login} не был получен"
        response = self.dm_account_api.account_api.put_v1_account_token(token=token)
        assert response.status_code == 200, f"Пользователь {login} не был активирован"
