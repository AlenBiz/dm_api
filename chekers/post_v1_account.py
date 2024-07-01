from datetime import datetime

import allure
from hamcrest import assert_that, starts_with, all_of, has_property, has_properties, equal_to, instance_of
import allure


class PostV1Account:

    @classmethod
    def check_response_values_post_v1_account(cls, login, response):
        with allure.step("проверка ответа"):
            today = datetime.now().strftime('%Y-%m-%d')
            assert_that(str(response.resource.registration), starts_with(today))
            assert_that(
                response, all_of(
                    has_property
                    ('resource', has_property('login', equal_to(login))),
                    has_property('resource', has_property('registration', instance_of(datetime))),
                    has_property('resource', has_properties({
                        'rating': has_properties({
                            'enabled': equal_to(True),
                            'quality': equal_to(0),
                            'quantity': equal_to(0)
                        })
                    }))
                )
            )
