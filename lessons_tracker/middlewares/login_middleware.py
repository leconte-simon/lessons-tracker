import re

from django.conf import settings
from django.shortcuts import redirect

from typing import Callable
from rest_framework.request import Request
from rest_framework.response import Response


class RequireLoginMiddleware:
    """
    Middleware that redirects unauthenticated users to the login page for
    each URL in LOGIN_REQUIRED_URLS and not in LOGIN_REQUIRED_URLS_EXCEPTIONS.
    For example:
    ------
    LOGIN_REQUIRED_URLS = (
        r'/topsecret/(.*)$',
    )
    LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/topsecret/login(.*)$',
        r'/topsecret/logout(.*)$',
    )
    ------
    LOGIN_REQUIRED_URLS is where you define URL patterns; each pattern must
    be a valid regex.

    LOGIN_REQUIRED_URLS_EXCEPTIONS is, conversely, where you explicitly
    define any exceptions (like login and logout URLs).
    """

    def __init__(self, get_response: Callable[[Request], Response]) -> None:
        self.get_response = get_response
        self.required = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS)
        self.exceptions = tuple(
            re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS
        )

    def __call__(self, request: Request) -> Response:
        if not request.user.is_authenticated:
            for url in self.exceptions:
                if url.match(request.path):
                    return self.get_response(request)
            for url in self.required:
                if url.match(request.path):
                    return redirect(f"/accounts/login/?next={request.path}")
        return self.get_response(request)
