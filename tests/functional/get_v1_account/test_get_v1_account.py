from datetime import datetime
from hamcrest import assert_that, has_property, has_properties, any_of, instance_of, equal_to, all_of, only_contains, \
    has_length, greater_than_or_equal_to

from chekers.get_v1_account import GetV1Account
from chekers.http_chekers import check_status_code_http
from dm_api_account.models.user_envelope import UserRole



def test_get_v1_account_auth(auth_account_helper):
    response = auth_account_helper.dm_account_api.account_api.get_v1_account()
    GetV1Account.check_response_values_get_v1_account(response)





def test_get_v1_account_no_auth(account_helper):
    with check_status_code_http(401, 'User must be authenticated'):
        account_helper.dm_account_api.account_api.get_v1_account()

