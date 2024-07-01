from dm_api_account.models.change_password import ChangePassword
from dm_api_account.models.registration import Registration
from dm_api_account.models.reset_password import ResetPassword
from dm_api_account.models.user_details_envelope import UserDetailsEnvelope
from dm_api_account.models.user_envelope import UserEnvelope
from restclient.client import RestClient


class AccountApi(RestClient):
    def post_v1_account(
            self,
            registration: Registration
    ):
        """Register new user"""
        response = self.post(
            path='/v1/account',
            json=registration.model_dump(exclude_none=True, by_alias=True)
        )
        return response

    def put_v1_account_token(
            self,
            token,
            validate_response=True
    ):
        """Activate registered user"""
        headers = {
            'accept': 'text/plain'
        }
        response = self.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    def get_v1_account(
            self,
            validate_response=True,
            **kwargs
    ):
        """Get current user"""
        response = self.get(
            path='/v1/account',
            **kwargs
        )
        if validate_response:
            return UserDetailsEnvelope(**response.json())
        return response

    def put_v1_account_email(
            self,
            json_data,
            validate_response=True
    ):
        """Change registered user email"""
        response = self.put(
            path='/v1/account/email',
            json=json_data
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    def post_v1_account_password(
            self,
            resetpassword: ResetPassword,
            validate_response=True,
            **kwargs,

    ):
        """Reset register user password"""
        response = self.post(
            path='/v1/account/password',
            json=resetpassword.model_dump(exclude_none=True, by_alias=True),
            **kwargs
        )
        if validate_response:
            UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            changepassword: ChangePassword,
            **kwargs
    ):
        """Change register user password"""
        response = self.put(
            path='/v1/account/password',
            json=changepassword.model_dump(exclude_none=True, by_alias=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response
