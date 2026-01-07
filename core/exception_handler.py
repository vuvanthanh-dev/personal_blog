from rest_framework.views import exception_handler
from rest_framework import status

from .exceptions import AppException
from .responses import api_error


def custom_exception_handler(exc, context):
    if isinstance(exc, AppException):
        return api_error(
            error_code=exc.error_code,
            message=str(exc.detail),
            data=getattr(exc, "data", None),
            status_code=exc.status_code,
        )

    response = exception_handler(exc, context)

    if response is not None:
        return api_error(
            error_code="ERROR_500",
            message=response.data.get("detail", "Có lỗi xảy ra"),
            status_code=response.status_code,
        )

    return api_error(
        error_code="ERROR_500",
        message="Hệ thống đang bận, vui lòng thử lại sau",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )