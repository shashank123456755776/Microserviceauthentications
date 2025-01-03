from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import requests
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        logger.debug(f"API Key received: {api_key}")

        if not api_key:
            logger.error("API Key missing from the request header.")
            raise AuthenticationFailed("Missing API Key")

        try:
            response = requests.get(
                settings.AUTH_SERVICE_URL,
                headers={"X-API-KEY": api_key},
                timeout=5
            )
            if response.status_code != 200:
                logger.error(f"Invalid API Key response from AUTH_SERVICE_URL: {response.status_code}")
                raise AuthenticationFailed("Invalid API Key")

            user_data = response.json()
            logger.debug(f"User data from AUTH_SERVICE: {user_data}")

            # Assuming 'username', 'role', and 'email' are in the user data response from AUTH_SERVICE_URL
            User = get_user_model()

            # Get or create the user based on username, ensuring role and other fields are populated
            user, created = User.objects.get_or_create(
             username=user_data['username'],
             defaults={
             'email': user_data.get('email', ''),
             }
)
# Explicitly update role for existing users
            if not created:
                 user.role = user_data.get('role', 'User')
                 user.save()

            request.user = user  # Set the authenticated user on the request
            return (user, None)

        except requests.exceptions.RequestException as e:
            logger.error(f"Error during authentication with AUTH_SERVICE: {e}")
            raise AuthenticationFailed("Unable to validate API Key")
