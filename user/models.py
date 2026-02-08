from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.db import models

from .managers import CustomUserManager
from utils.enum_utils import UserRole, Gender
from utils.mixin import random_device_token, user_profile_upload_to


# Base model
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


#  Customization user model
class User(AbstractBaseUser, Timestamp, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    fullname = models.CharField(max_length=255, blank=True, default="")
    role = models.IntegerField(
        choices=UserRole.get_choices(), default=UserRole.CUSTOMER.value
    )

    # Additional fields for user management
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_online = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname", "phone"]

    def __str__(self):
        return self.fullname

    @property
    def role_name(self):
        return UserRole(self.role).name.title()


# Generic users profile
class Profile(Timestamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=255, blank=True, default="")
    state = models.CharField(max_length=255, blank=True, default="")
    city = models.CharField(max_length=255, blank=True, default="")
    zip_code = models.CharField(max_length=255, blank=True, default="")
    latitude = models.FloatField(default=32.00, blank=True, null=True)
    longitude = models.FloatField(default=32.87, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True, default=now)
    gender = models.IntegerField(choices=Gender.get_gender(), default=Gender.MALE.value)
    device_token = models.CharField(
        max_length=200, blank=True, null=True, default=random_device_token
    )
    avatar = models.ImageField(upload_to=user_profile_upload_to, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.fullname}"

    @property
    def get_gender(self):
        return Gender(self.gender).name.title()

    @property
    def role_name(self):
        return UserRole(self.user.role).name.title()

    @property
    def fullname(self):
        return self.user.fullname

    @property
    def email(self):
        return self.user.email

    @property
    def phone(self):
        return self.user.phone


# When user create profile will be created at the same time.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)
        return profile


post_save.connect(create_user_profile, sender=User)
