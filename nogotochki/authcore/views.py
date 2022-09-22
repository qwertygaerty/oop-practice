from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authcore.exceptions import ValidationAPIException, NogtiAPIException
from authcore.models import User
from authcore.serializers import EmailSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@api_view(['POST'])
def login(request):
    serializer = EmailSerializer(data=request.data)
    if not (serializer.is_valid()):
        raise ValidationAPIException(message='Validation error',
                                     code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                     errors=serializer.errors)
    try:
        user = User.objects.get(email=serializer.data['email'], password=serializer.data['password'])
    except User.DoesNotExist:

        raise NogtiAPIException(message='Authentication failed',
                                code=status.HTTP_401_UNAUTHORIZED)

    user.api_token = get_random_string(length=32)
    user.save()

    response = {
        'data': {
            'user_token': user.api_token,
        }
    }
    return Response(response, status=status.HTTP_200_OK)


def signup():
    pass
