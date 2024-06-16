
import structlog
from helpers.account_helpers import AccountHelper
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmConfiguration
from services.api_mailhog import MailHogApiAccount
from services.dm_api_account import DMApiAccount
from faker import Faker

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, ensure_ascii=True, sort_keys=True)
    ]
)


def test_put_v1_account_email():
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_configuration = DmConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_configuration)
    mailhog = MailHogApiAccount(configuration=mailhog_configuration)
    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog)
    # Тестовые данные
    fake = Faker()
    login = fake.last_name() + fake.first_name()
    email = f'{login}@mail.ru'
    new_email = f'new{login}@mail.ru'
    password = '12345678'

    # регистрация пользователя
    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.user_login_pass(login=login, password=password)
    account_helper.user_change_email(login=login, password=password, new_email=new_email)
    account_helper.user_login_pass(login=login, password=password)
