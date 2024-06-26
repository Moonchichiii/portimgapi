from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegisterSerializer, UserSerializer
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


# Create your views here.

class CustomRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        if not user.is_active:
            raise ValueError("User account is disabled.")
        return super().for_user(user)

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@ensure_csrf_cookie
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = CustomRefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        csrf_token = get_token(request)

        response = Response(
            {
                'user': UserSerializer(user).data,
                'csrfToken': csrf_token,
                'access': access_token,
                'refresh': refresh_token
            },
            status=status.HTTP_201_CREATED
        )
        response.set_cookie('access_token', access_token, httponly=True, secure=False)
        response.set_cookie('refresh_token', refresh_token, httponly=True, secure=False)
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        tokens = response.data
        user = User.objects.get(username=request.data['username'])
        if not user.is_active:
            return Response({"detail": "User account is disabled."}, status=status.HTTP_403_FORBIDDEN)
        
        user_serializer = UserSerializer(user)
        csrf_token = get_token(request)
        response.set_cookie('access_token', tokens['access'], httponly=True, secure=False)
        response.set_cookie('refresh_token', tokens['refresh'], httponly=True, secure=False)
        response.data = {
            'user': user_serializer.data,
            'csrfToken': csrf_token,
            'access': tokens['access'],
            'refresh': tokens['refresh'],
        }
        return response

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data
            response.set_cookie('access_token', tokens['access'], httponly=True, secure=False)
            return response
        except Exception as e:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout(request):
    response = Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response

@api_view(['GET'])
def current_user(request):
    user = request.user
    if user.is_authenticated:
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    else:
        return Response({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
