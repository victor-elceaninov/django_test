from datetime import datetime
from django.utils.deprecation import MiddlewareMixin


class LogRestMiddleware(MiddlewareMixin):
    def _log_request(self, request):
        user = str(getattr(request, 'user', ''))
        method = str(getattr(request, 'method', '')).upper()
        query_params = str(request.body)
        query_params = query_params if query_params else ''

        log_info = f"{request.META['REMOTE_ADDR']} - {user} " \
                   f"[{datetime.now().strftime('%d/%b/%Y:%H:%M:%S.%f %z')}] " \
                   f"\"{method} {request.get_full_path()} HTTP/1.1\"\n" \
                   f"request_body: {query_params}\n"

        with open('../log.log', 'a') as log:
            log.write(log_info)

    def _log_response(self, request, response):
        size = str(len(response.content))
        if response['content-type'] == 'application/json':
            if getattr(response, 'streaming', False):
                response_body = '<<<Streaming>>>'
            else:
                response_body = response.content
        else:
            response_body = '<<<Not JSON>>>'

        log_info = f"response_header: {response.status_code} {size}\n" \
                   f"response_body: {str(response_body)}\n" \
                   f"run_time: {datetime.now() - request.start_time}\n\n"

        with open('../log.log', 'a') as log:
            log.write(log_info)

    def process_response(self, request, response):
        request.start_time = datetime.now()
        self._log_request(request)
        self._log_response(request, response)
        return response

    def __call__(self, request):
        request.start_time = datetime.now()
        self._log_request(request)
        response = self.get_response(request)
        self._log_response(request, response)
        return response
