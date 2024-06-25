from datetime import datetime

from hamcrest import assert_that, has_property, has_properties, any_of, instance_of, equal_to, all_of, only_contains, \
    has_length, greater_than_or_equal_to, has_string, starts_with

from dm_api_account.models.user_envelope import UserRole


def test_get_v1_account_auth(auth_account_helper):
    response = auth_account_helper.dm_account_api.account_api.get_v1_account()
    assert_that(response, all_of(
        has_property('resource',
                     has_properties({
                         'login': equal_to('biziaev'),
                         'roles': all_of(
                             only_contains(
                                 UserRole.GUEST,
                                 UserRole.PLAYER,
                                 UserRole.ADMINISTRATOR,
                                 UserRole.NANNY_MODERATOR,
                                 UserRole.REGULAR_MODERATOR,
                                 UserRole.SENIOR_MODERATOR
                             ),
                             has_length(greater_than_or_equal_to(2))
                         ),
                         "online": instance_of(datetime)
                     }))))
    print(response)

# def test_get_v1_account_no_auth(account_helper):
#     account_helper.dm_account_api.account_api.get_v1_account()
