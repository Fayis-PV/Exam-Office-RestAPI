from django.middleware.csrf import get_token

class CSRFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' or  request.method == 'PUT' or  request.method == 'DELETE':
            request.META['HTTP_X_CSRFTOKEN'] = get_token(request)

        return self.get_response(request)
