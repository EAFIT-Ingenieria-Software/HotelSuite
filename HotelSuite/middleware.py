from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class AdminMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated or request.user.get_role() != 'admin':
                return HttpResponse("Access Denied")
        return self.get_response(request)
