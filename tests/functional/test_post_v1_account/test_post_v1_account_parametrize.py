

import pytest

from chekers.http_chekers import check_status_code_http


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
