from django.shortcuts import render
from django.views.generic import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializer import *
from app.models import DataModel
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# Create your views here.


@api_view(['GET'])
def index(request):
    user = request.user
    queryset = DataModel.objects.all()
    serializer = DataModelSerializer(queryset, many=True)
    return Response({
        'status': 200,
        'user': f'{user}',
        'message': 'Working',
        'Employees Data': serializer.data
    })


@api_view(['POST'])
def post_data(request):
    data = request.data
    serializer = DataModelSerializer(data=data)
    if not serializer.is_valid():
        return Response({
            'status': 403,
            'erros': serializer.errors,
            'message': "Something went wrong!"
        })
    serializer.save()
    return Response({
        'status': 200,
        'payload': serializer.data,
        'message': "Data saved!"
    })


@api_view(['PUT'])
def updated_data(request, pk):
    try:
        queryset = DataModel.objects.get(id=pk)
        serializer = DataModelSerializer(
            queryset, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({
                'status': 403,
                'erros': serializer.errors,
                'message': "Something went wrong!"
            })
        serializer.save()
        return Response({
            'status': 200,
            'payload': serializer.data,
            'message': "Data updated!"
        })
    except Exception as e:
        return Response({
            'status': 403,
            'errors': f'{e}',
            'message': 'Something went wrong!'
        })


@api_view(['DELETE'])
def delte_data(request, pk):
    try:
        queryset = DataModel.objects.get(id=pk)
        queryset.delete()
        return Response({
            'status': 200,
            'message': "Data deleted successfully!"
        })
    except Exception as e:
        return Response({
            'status': 403,
            'errors': f'{e}',
            'message': 'Something went wrong!'
        })


@api_view(['GET'])
def get_books(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response({
        'status': 200,
        'message': 'Data fetched successfully',
        'payload': serializer.data
    })


class DataAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        queryset = DataModel.objects.all()
        serializer = DataModelSerializer(queryset, many=True)
        return Response({
            'status': 200,
            'message': 'Working',
            'Employees Data': serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = DataModelSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status': 403,
                'erros': serializer.errors,
                'message': "Something went wrong!"
            })
        serializer.save()
        return Response({
            'status': 200,
            'payload': serializer.data,
            'message': "Data saved!"
        })

    def put(self, request):
        try:
            queryset = DataModel.objects.get(id=request.data['id'])
            serializer = DataModelSerializer(
                queryset, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({
                    'status': 403,
                    'erros': serializer.errors,
                    'message': "Something went wrong!"
                })
            serializer.save()
            return Response({
                'status': 200,
                'payload': serializer.data,
                'message': "Data updated!"
            })
        except Exception as e:
            return Response({
                'status': 403,
                'errors': f'{e}',
                'message': 'Something went wrong!'
            })

    def delete(self, request):
        try:
            queryset = DataModel.objects.get(id=request.data['id'])
            queryset.delete()
            return Response({
                'status': 200,
                'message': "Data deleted successfully!"
            })
        except Exception as e:
            return Response({
                'status': 403,
                'errors': f'{e}',
                'message': 'Something went wrong!'
            })


class RegisterAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({
                'status': 403,
                'erros': serializer.errors,
                'message': "Something went wrong!"
            })
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token_obj.key,
            'user_id': user.pk,
            'username': user.username,
            'payload':serializer.data
        })