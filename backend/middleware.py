from django.conf import settings
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class JWTSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):

        if request.path == "/logout/":
            request.session.flush()
            return redirect("/login/")

        # Add JWT token to the authorization header
        access_token = request.session.get("access_token")
        if access_token:
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"
