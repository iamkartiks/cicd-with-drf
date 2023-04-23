from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UsersAPIView(APIView):
    """
    Arguments : API View
    Returns : List of all the users from the database
    
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)


class AddUserAPI(APIView):
    """
    Arguments : API View, request_data
                request_data = ["username","email","password"]
    Returns : created user data (username & email)
    """
    def post(self, request):    
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)