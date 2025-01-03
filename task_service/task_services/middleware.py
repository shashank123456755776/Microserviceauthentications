import requests
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
import logging

# Configure logging for better debugging
logger = logging.getLogger(__name__)

class ValidateAPIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract API Key from header
        api_key = request.headers.get('X-API-KEY')
        print(f"API Key received: {api_key}")
        logger.debug(f"API Key received: {api_key}")

        if not api_key:
            logger.error("Missing API Key")
            raise AuthenticationFailed("Missing API Key")

        # Verify the API Key with the authentication service
        try:
            logger.debug(f"Sending GET request to AUTH_SERVICE_URL: {settings.AUTH_SERVICE_URL}")
            response = requests.get(
                settings.AUTH_SERVICE_URL, 
                headers={"X-API-KEY": api_key},  # Send the API key as a header
                timeout=5  # Timeout for the request
            )
            logger.debug(f"Response from AUTH_SERVICE_URL: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error connecting to AUTH_SERVICE_URL: {str(e)}")
            raise AuthenticationFailed("Unable to validate API Key")

        # Handle the response from the authentication service
        if response.status_code != 200:
            logger.error(f"Invalid API Key response from AUTH_SERVICE_URL: {response.status_code} - {response.text}")
            raise AuthenticationFailed("Invalid API Key")

        try:
            user_data = response.json()
            request.META['X-User-UUID'] = user_data.get('uuid', '')
            request.META['X-User-Role'] = user_data.get('role', '')
        except ValueError as e:
            logger.error(f"Invalid JSON in response: {str(e)}")
            raise AuthenticationFailed("Invalid response from authentication service")

        # Proceed with the request
        return self.get_response(request)
