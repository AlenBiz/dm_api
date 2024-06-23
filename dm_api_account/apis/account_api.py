from dm_api_account.models.registration import Registration
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
            validate_responce=True
    ):
        """Activate registered user"""
        headers = {
            'accept': 'text/plain'
        }
        response = self.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        if validate_responce:
            return UserEnvelope(**response.json())
        return response

    def get_v1_account(
            self,
            **kwargs
    ):
        """Get current user"""
        response = self.get(
            path='/v1/account',
            **kwargs
        )
        return response

    def put_v1_account_email(
            self,
            json_data,
            validate_responce=True
    ):
        """Change registered user email"""
        response = self.put(
            path='/v1/account/email',
            json=json_data
        )
        if validate_responce:
            return UserEnvelope(**response.json())
        return response

    def post_v1_account_password(
            self,
            json_data,
            **kwargs,

    ):
        """Reset register user password"""
        response = self.post(
            path='/v1/account/password',
            json=json_data,
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            json_data,
            **kwargs
    ):
        """Change register user password"""
        response = self.put(
            path='/v1/account/password',
            json=json_data,
            **kwargs
        )
        UserEnvelope(**response.json())
        return response
