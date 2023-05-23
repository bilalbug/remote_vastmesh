from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong!'})

        serializer.save()
        user = CustomUser.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token_obj), 'message': 'User Registered!'})


@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'user_type': user.user_type,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone': user.phone.as_e164,
            'image': user.image.url
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    if not user.check_password(password):
        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user_id': user.id,
        'user_type': user.user_type,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
        'image': user.image.url
    }, status=status.HTTP_200_OK)


class CustomUserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class AdminViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class RecruiterViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class JobViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
