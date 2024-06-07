import  requests
class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def post_v1_account(self, json_data):
        """Register new user"""
        response = requests.post(url=f'{self.host}/v1/account', json=json_data)
        return response

    def put_v1_account_token(self, token):
        """Activate registered user"""
        headers = {
            'accept': 'text/plain'
        }
        response = requests.put(url=f'{self.host}/v1/account/{token}', headers=headers)
        print(f'{self.host}/v1/account/{token}')
        return response

    def put_account_email(self, json_data):
        """Change registered user email"""
        response = requests.put(f'{self.host}/v1/account/email', json=json_data)
        return response

