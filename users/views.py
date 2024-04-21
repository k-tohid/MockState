from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsOwnerOrReadOnly


class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        # this is a hook to perform operations on the object before sending it
        password = serializer.initial_data.get('password')
        instance = serializer.save()
        instance.set_password(password)
        instance.save()
        token, is_created = Token.objects.get_or_create(user=instance)
        self.token = token

    def create(self, request, *args, **kwargs):
        # this is the function to send the data
        response = super().create(request, *args, **kwargs)
        data = response.data
        data["token"] = self.token.key
        return Response(data, status=status.HTTP_201_CREATED)


class CustomUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "username"


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )