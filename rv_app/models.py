from django.db import models
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from django_countries.fields import CountryField
from django.utils import timezone
from datetime import timedelta
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class CustomUser(models.Model):
    user_type = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('recruiter', 'Recruiter'),
    )

    id = models.AutoField(primary_key=True, editable=False)
    user_type = models.CharField(max_length=20, choices=user_type)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = PhoneNumberField()
    image = models.ImageField(
        upload_to="Images/Users/", null=True, height_field=None, width_field=None, max_length=None)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['user_type', 'password', 'first_name',
                       'last_name', 'phone', 'is_anonymous', 'is_authenticated', 'is_active', 'is_staff', 'is_superuser']

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Admin(models.Model):
    admin_role = (
        ('ceo', 'Chief Executive Officer'),
        ('dg', 'Director General'),
        ('prsdnt', 'President'),
        ('vp', 'Vice President'),
        ('pm', 'Project Manager'),
        ('tl', 'Team Lead'),
    )
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, editable=False)
    admin_role = models.CharField(max_length=20, choices=admin_role)

    def __str__(self) -> str:
        return str(self.user_id) + " as " + self.admin_role + "-0" + str(self.id)


class Employee(models.Model):
    user_category = (
        ('sftdev', 'Software Developer'),
        ('uiux', 'UI/UX Designer'),
        ('techrec', 'Technical Recruiter'),
        ('sdr', 'Sales Development Representative'),
        ('pms', 'Performance Marketing Specialist'),
    )

    english_level = (
        ('bgnr', 'Beginner'),
        ('intr', 'Intermediate'),
        ('advn', 'Advance'),
    )

    hear_about_us = (
        ('linkedin', 'LinkedIn'),
        ('fbk', 'FaceBook'),
        ('ggl', 'Google'),
        ('yt', 'YouTube'),
        ('hfst', 'HireFast'),
        ('otr', 'Other'),
    )

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, editable=False)
    category = models.CharField(max_length=20, choices=user_category)
    years_of_exp = models.IntegerField()
    upload_resume = models.FileField(upload_to="Resume/", max_length=100)
    english_level = models.CharField(max_length=20, choices=english_level)
    kind_of_work = models.CharField(max_length=200)
    current_salary = MoneyField(max_digits=14, decimal_places=2,
                                default_currency='USD')
    expected_salary = MoneyField(max_digits=14, decimal_places=2,
                                 default_currency='USD')
    hear_about_us = models.CharField(max_length=20, choices=hear_about_us)
    # skill_list = ArrayField(models.CharField(max_length=200, blank=True, default="default"))

    def __str__(self) -> str:
        return str(self.user_id)


class Recruiter(models.Model):
    hear_about_us = (
        ('linkedin', 'LinkedIn'),
        ('fbk', 'FaceBook'),
        ('ggl', 'Google'),
        ('yt', 'YouTube'),
        ('hfst', 'HireFast'),
        ('otr', 'Other'),
    )

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, editable=False)
    country = CountryField()
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=254)
    company_phone_number = PhoneNumberField()
    hear_about_us = models.CharField(
        max_length=20, choices=hear_about_us)

    def __str__(self) -> str:
        return str(self.user_id) + " from " + self.company_name


class Meeting(models.Model):
    recruiter_id = models.ForeignKey(
        Recruiter, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, editable=False)
    # required_skills = ArrayField(models.CharField(max_length=250, blank=True))
    number_of_employees_required = models.IntegerField()
    employees_required_date = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    meeting_date_time = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    meeting_duration = models.DurationField(default=timedelta(minutes=30))
    meeting_attendee = models.ManyToManyField(Admin)

    def __str__(self) -> str:
        return str(self.recruiter_id) + " on " + str(self.meeting_date_time)


class Job(models.Model):
    posted_by = models.ForeignKey(
        Recruiter, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, editable=False)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    job_posted_date = models.DateField(auto_now=True)
    job_rate_per_hour = MoneyField(default=0, max_digits=14, decimal_places=2,
                                   default_currency='USD')

    def __str__(self) -> str:
        return self.job_title + " per hour " + str(self.job_rate)


class Podcast(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='Podcasts/podcast_images/')
    audio_file = models.FileField(upload_to='Podcasts/podcast_audios/')
    publish_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta(minutes=30))
    host = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + " by " + str(self.host)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='Blogs/blogs_images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + " by " + str(self.author)
