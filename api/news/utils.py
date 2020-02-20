from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if response.status_code is status.HTTP_400_BAD_REQUEST:
            data = response.data
            response.data = {"message": "The given data was invalid."}
            if hasattr(data, 'items'):
                errors = [{k: v[0]} for k, v in data.items()]
                response.data['errors'] = errors
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data = {"message": "404 Not Founded"}
        else:
            data = response.data
            response.data = {"message": data["detail"]}

    return response
