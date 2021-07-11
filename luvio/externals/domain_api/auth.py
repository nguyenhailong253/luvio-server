import os
import requests
from requests.auth import HTTPBasicAuth
import base64

domain_auth_url = 'https://auth.domain.com.au/v1/connect/token'

class DomainApiService:
    def __init__(self):
        self.access_token = os.getenv("DOMAIN_ACCESS_TOKEN")
        if not self.access_token:
            self.access_token = self.refresh_token()
        # Check env variable for access token. If non, call refresh token method. Otherwise just use it
        # When calling Domain API, if receive 401, meaning token might have expired, try refresh token and then re call

    def refresh_token(self):
        client_id = os.getenv('DOMAIN_CLIENT_ID')
        client_secrets = os.getenv('DOMAIN_CLIENT_SECRETS')

        req_body = {
            'scope': 'api_agencies_read api_listings_read api_properties_read api_addresslocators_read api_demographics_read api_locations_read api_salesresults_read api_suburbperformance_read',
            'grant_type': 'client_credentials'
        }

        response = requests.post(domain_auth_url, data=req_body, auth=HTTPBasicAuth(client_id, client_secrets))
        return response.json()['access_token']