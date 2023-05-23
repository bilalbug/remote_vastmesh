from rest_framework import serializers
from .models import BlogPost, Podcast, Job, Meeting, Recruiter, Employee, Admin, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'
