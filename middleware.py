from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import compress_string
from django.utils.cache import patch_vary_headers
from django.conf import settings
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
EXEMPT_URLS += [compile('user_login')]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
  """
  Middleware that requires a user to be authenticated to view any page other
  than LOGIN_URL. Exemptions to this requirement can optionally be specified
  in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
  you can copy from your urls.py).
  
  Requires authentication middleware and template context processors to be
  loaded. You'll get an error if they aren't.
  """
  def process_request(self, request):
    assert hasattr(request, 'user'), "The Login Required middleware\
requires authentication middleware to be installed. Edit your\
MIDDLEWARE_CLASSES setting to insert\
'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't\
work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
'django.core.context_processors.auth'."
    if not request.user.is_authenticated():
      path = request.path_info.lstrip('/')
      if not any(m.match(path) for m in EXEMPT_URLS):
        return HttpResponseRedirect(settings.LOGIN_URL)
 
 
try:
    from django.conf import settings
    XS_SHARING_ALLOWED_ORIGINS = settings.XS_SHARING_ALLOWED_ORIGINS
    XS_SHARING_ALLOWED_METHODS = settings.XS_SHARING_ALLOWED_METHODS
    XS_SHARING_ALLOWED_HEADERS = settings.XS_SHARING_ALLOWED_HEADERS
    XS_SHARING_ALLOWED_CREDENTIALS = settings.XS_SHARING_ALLOWED_CREDENTIALS
except AttributeError:
    XS_SHARING_ALLOWED_ORIGINS = '*'
    XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE', 'PATCH']
    XS_SHARING_ALLOWED_HEADERS = ['Content-Type', '*']
    XS_SHARING_ALLOWED_CREDENTIALS = 'true'
 
 
class XsSharing(object):
    """
    This middleware allows cross-domain XHR using the html5 postMessage API.
     
    Access-Control-Allow-Origin: http://foo.example
    Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
 
    Based off https://gist.github.com/426829
    """
    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = HttpResponse()
            response['Access-Control-Allow-Origin']  = XS_SHARING_ALLOWED_ORIGINS 
            response['Access-Control-Allow-Methods'] = ",".join( XS_SHARING_ALLOWED_METHODS ) 
            response['Access-Control-Allow-Headers'] = ",".join( XS_SHARING_ALLOWED_HEADERS )
            response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS
            return response
 
        return None
 
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin']  = XS_SHARING_ALLOWED_ORIGINS 
        response['Access-Control-Allow-Methods'] = ",".join( XS_SHARING_ALLOWED_METHODS )
        response['Access-Control-Allow-Headers'] = ",".join( XS_SHARING_ALLOWED_HEADERS )
        response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS
 
        return response
