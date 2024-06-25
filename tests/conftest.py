from collections import namedtuple
import pytest
from helpers.account_helpers import AccountHelper
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmConfiguration
from services.api_mailhog import MailHogApiAccount
from services.dm_api_account import DMApiAccount
from faker import Faker
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True
        )
    ]
)


@pytest.fixture(scope='session')
def mailhog_api():
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    mailhog_client = MailHogApiAccount(configuration=mailhog_configuration)
    return mailhog_client


@pytest.fixture(scope='session')
def account_api():
    dm_configuration = DmConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_configuration)
    return account


@pytest.fixture(scope='session')
def account_helper(account_api, mailhog_api):
    account_helper = AccountHelper(dm_account_api=account_api, mailhog=mailhog_api)
    return account_helper


@pytest.fixture(scope='session')
def auth_account_helper(mailhog_api):
    dm_configuration = DmConfiguration(
        host='http://5.63.153.31:5051', disable_log=False
    )
    account = DMApiAccount(configuration=dm_configuration)
    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog_api)
    account_helper.auth_client(
        login='biziaev',
        password='12345678'
    )
    return account_helper


@pytest.fixture()
def prepare_user():
    fake = Faker()
    login = fake.last_name() + fake.first_name()
    email = f'{login}@mail.ru'
    password = '12345678'
    User = namedtuple('User', ['login', 'password', 'email'])
    user = User(login=login, password=password, email=email)
    return user