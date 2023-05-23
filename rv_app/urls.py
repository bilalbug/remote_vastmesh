from django import views
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'recruiters', RecruiterViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'podcasts', PodcastViewSet)
router.register(r'blogposts', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUser.as_view()),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
]
