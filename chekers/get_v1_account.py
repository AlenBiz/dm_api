from datetime import datetime

from hamcrest import assert_that, all_of, has_property, has_properties, equal_to, only_contains, has_length, \
    greater_than_or_equal_to, instance_of

from dm_api_account.models.user_envelope import UserRole


class GetV1Account:
    @classmethod
    def check_response_values_get_v1_account(cls, response):
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