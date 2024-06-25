from datetime import datetime
from hamcrest import has_properties, assert_that, only_contains, all_of, has_length, greater_than_or_equal_to, \
    has_string, starts_with, any_of
from dm_api_account.models.user_envelope import UserRole

from hamcrest import assert_that, has_property, all_of, instance_of, equal_to, has_properties
from datetime import datetime


def test_get_v1_account_auth(auth_account_helper):
    auth_account_helper.dm_account_api.account_api.get_v1_account()

    #     response, has_property('resource',has_property('login', equal_to('biziaev')))))

    #
    # assert_that(
    #     response,
    # has_property("resource",
    # has_properties({
    #     'roles':
    #         any_of('Guest',
    #                'Player',
    #                'Administrator',
    #                'NannyModerator',
    #                'RegularModerator',
    #                'SeniorModerator')
    # })

    # has_property('resource', has_property('registration', instance_of(datetime))),
    # has_property('resource', has_properties({
    #     'rating': has_properties({
    #         'enabled': equal_to(True),
    #         'quality': equal_to(0),
    #         'quantity': equal_to(0)
    #     })
    # }))

    # ))




# def test_get_v1_account_no_auth(account_helper):
#     account_helper.dm_account_api.account_api.get_v1_account()
