from rest_framework.response import Response
from rest_framework import status

def api_success(data=None, message="", error_code="ERROR_200", status_code=status.HTTP_200_OK):
    return Response(
        {
            "code": error_code,
            "message": message,
            "data": data,
        },
        status=status_code,
    )

def api_error(message="Hệ thống đang bận, vui lòng thử lại sau", error_code="ERROR_500", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, data=None):
    return Response(
        {
            "code": error_code,
            "message": message,
            "data": data,
        },
        status=status_code,
    )
