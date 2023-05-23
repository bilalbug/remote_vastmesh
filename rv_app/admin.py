from django.contrib import admin
from . models import CustomUser, Employee, Recruiter, Meeting, Job, Podcast, BlogPost, Admin
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Recruiter)
admin.site.register(Meeting)
admin.site.register(Job)
admin.site.register(Podcast)
admin.site.register(BlogPost)
admin.site.register(Admin)
