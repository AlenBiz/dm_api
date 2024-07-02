import allure
from chekers.post_v1_account import PostV1Account
import pytest
from chekers.http_chekers import check_status_code_http


@allure.suite("Тесты на проверку метода POST v1/account")
@allure.sub_suite("Позитивные тесты")
class TestsPostV1Account:
    @allure.title("Проверка регистрации нового пользователя")
    def test_post_v1_account(self, account_helper, prepare_user):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email

        account_helper.register_new_user(login=login, password=password, email=email)
        response = account_helper.user_login(login=login, password=password, validate_response=True)
        PostV1Account.check_response_values_post_v1_account(login, response)


@allure.suite("Тесты на проверку метода POST v1/account")
@allure.sub_suite("Негативные тесты")
@pytest.mark.parametrize('login, email, password, status_code, message',
                         [
                             ('AlenBiz', 'biziaeva4y5y@mail.ru', '123456', 400, 'Validation failed'),
                             ('AlenBiz', 'biziaevmail.ru', '12345678', 400, 'Validation failed'),
                             ('A', 'biziaeva1242@example.com', '12345678', 400, 'Validation failed')
                         ])
def test_post_v1_account_negative(account_helper, login, email, password, status_code, message):
    with check_status_code_http(expected_status_code=status_code, expected_message=message):
        response = account_helper.register_new_not_activated_user(login=login, password=password, email=email)
        print(response)
