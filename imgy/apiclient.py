import http
import boto3
import requests

IMGY_API_ENDPOINT = 'https://hf8cnre055.execute-api.eu-west-1.amazonaws.com/dev/api/'

CLIENT_ID = '3252vq7h3r1vjg3a56iddigd52'
AUTH_FLOW = 'USER_PASSWORD_AUTH'

class ApiClient:

    def __init__(self, username, password):
        self.test = ""
        self.username = username
        self.password = password
        self.client = boto3.client('cognito-idp')

    def get_jwt_token(self):
        token = ''

        try:
            response = self.client.initiate_auth(
                ClientId=CLIENT_ID,
                AuthFlow=AUTH_FLOW,
                AuthParameters={
                    'USERNAME': self.username,
                    'PASSWORD': self.password
                }
            )

            if not response:
                raise Exception('Response is not valid')

            if not response['AuthenticationResult']:
                raise Exception('Authentication Result not found in the response')

            if not response['AuthenticationResult']['IdToken']:
                raise Exception('Token not found in the response')

            token = response['AuthenticationResult']['IdToken']

        except Exception as e:
            pass

        return token

    def upload_file(self):
        raise NotImplementedError


    # TODO: make sure the file is downloaded properly
    def download_file(self, image_id):
        token = self.get_jwt_token()

        headers = {"Authorization":"Bearer " + token}
        result = requests.get(IMGY_API_ENDPOINT + 'image/' +  image_id,headers=headers).json()
        file = requests.get(result['signedURL'])

        return file
