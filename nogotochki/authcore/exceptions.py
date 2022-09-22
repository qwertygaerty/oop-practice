from rest_framework.exceptions import APIException


class AuthenticationFailed(APIException):
    code = 401
    warning: 'Authentication failed'


class ForbiddenForYou(APIException):
    code = 403
    warning: 'Forbidden for you'


class OrderIsProcessed:
    code = 201
    message = 'Order is processed'


class CartIsEmpty:
    code = 422
    message = '"Cart is empty'
