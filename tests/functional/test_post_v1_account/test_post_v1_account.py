import pytest
from hamcrest import assert_that, has_property, all_of, instance_of, equal_to, has_properties, starts_with
from datetime import datetime

from chekers.http_chekers import check_status_code_http
from chekers.post_v1_account import PostV1Account
from dm_api_account.models.registration import Registration
from services import dm_api_account


def test_post_v1_account(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    account_helper.register_new_user(login=login, password=password, email=email)
    response = account_helper.user_login(login=login, password=password, validate_response=True)
    PostV1Account.check_response_values_post_v1_account(login, response)

















