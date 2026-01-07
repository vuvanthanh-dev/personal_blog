from rest_framework import status

class AppException(Exception):
    status_code = status.HTTP_400_BAD_REQUEST
    default_error_code = "ERROR_UNKNOWN"
    default_message = ""

    def __init__(self, message=None, error_code=None, status_code=None, data=None):
        self.detail = message or self.default_message
        self.error_code = error_code or self.default_error_code
        self.data = data

        if status_code:
            self.status_code = status_code


class NotFoundException(AppException):
    status_code = 404


class BadRequestException(AppException):
    status_code = 400


class UnauthorizedException(AppException):
    status_code = 401

class ForbiddenException(AppException):
    status_code = 403


class ConflictException(AppException):
    status_code = 409


class InternalServerErrorException(AppException):
    status_code = 500


class ServiceUnavailableException(AppException):
    status_code = 503


class GatewayTimeoutException(AppException):
    status_code = 504


class ValidationException(BadRequestException):
    status_code = 422


class PayloadTooLargeException(AppException):
    status_code = 413


class UnsupportedMediaTypeException(AppException):
    status_code = 415