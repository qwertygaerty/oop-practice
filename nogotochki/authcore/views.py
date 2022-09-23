from django.contrib.auth import logout
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAuthenticated

from authcore.exceptions import ValidationAPIException, NogtiAPIException
from authcore.models import User, Service, Cart, Order
from authcore.serializers import EmailSerializer, SignUpSerializer, ServiceSerializer, CartSerializer, OrderSerializer


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
        'token': user.api_token,
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    if not serializer.is_valid():
        raise ValidationAPIException(message='Validation error',
                                     code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                     errors=serializer.errors)

    user = User.objects.create(**request.data)
    user.api_token = get_random_string(length=32)
    user.save()

    response = {
        'token': user.api_token,
    }

    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def service(request):
    queryset = Service.objects.all()

    response = {
        'items': ServiceSerializer(queryset, many=True).data
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def cart_toggle(request, pk=None):
    us = User.get_auth_user(request)
    serv = Service.objects.get(id=pk)

    if request.method == 'POST':

        if not serv:
            raise ValidationAPIException(message='Not Found', code=status.HTTP_422_UNPROCESSABLE_ENTITY, )

        cart = Cart.objects.filter(user=us).first()

        if not cart:
            cart = Cart.objects.create(user=us)

        cart.items.add(serv)
        cart.save()

        response = {
            "message": "Service add to card",
        }

        return Response(response, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        cart = Cart.objects.filter(user=us).first()
        cart.items.remove(serv)

        response = {
            "message": " Item removed from cart",
        }

        return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def cart_get(request):
    queryset = Cart.objects.filter(user=User.get_auth_user(request))

    services = []

    for q in queryset:
        services.append(q.get_services())

    response = CartSerializer(queryset, many=True).data[0]

    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def order(request):
    response = {}
    us = User.get_auth_user(request)
    cart = Cart.objects.get(user=us)

    if request.method == 'POST':

        if len(cart.get_ids()) == 0:
            raise NogtiAPIException(message='Cart is empty',
                                    code=status.HTTP_422_UNPROCESSABLE_ENTITY, )

        order_price = cart.get_price()
        ord = Order.objects.create(services=cart.get_ids(), order_price=123, cart=cart)
        ord.order_price = order_price
        ord.save()

        cart.items.clear()

        response = {
            "order_id": ord.id,
            "message": "Order is processed"
        }
        return Response(response, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        response = {
            "items": OrderSerializer(Order.objects.filter(cart__user=us), many=True).data
        }

    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def logout_user(request):
    us = User.get_auth_user(request)
    us.api_token = None
    us.save()

    response = {
        "message": "logout"
    }
    return Response(response, status=status.HTTP_200_OK)

