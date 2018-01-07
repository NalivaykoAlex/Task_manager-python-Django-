from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile


EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:

    def process_request(self, request):
        assert hasattr(request, 'user')
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(url.match(path) for url in EXEMPT_URLS):
              return HttpResponseRedirect(settings.LOGIN_URL)



