import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator,\
    RegexValidator
from address.models import AddressField
from core.models import StartEndModel, YearTermModel
from chapters.models import Chapter


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    modified = models.DateTimeField(auto_now=True)
    badge_number = models.PositiveIntegerField()
    major = models.CharField(max_length=50)
    graduation_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1950),
            MaxValueValidator(datetime.now().year + 10)],
        help_text="Use the following format: <YYYY>")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17, blank=True)
    address = AddressField()
    chapter = models.ForeignKey(Chapter)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class UserSemesterServiceHours(YearTermModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    service_hours = models.PositiveIntegerField(default=0)


class UserSemesterGPA(YearTermModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    gpa = models.FloatField()


class UserStatusChange(StartEndModel):
    STATUS = [
        ('alumni', 'alumni'),
        ('active', 'active'),
        ('pnm', 'prospective'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.CharField(
        max_length=7,
        choices=STATUS
    )


class UserRoleChange(StartEndModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    role = models.CharField(max_length=50)


class UserOrgParticipate(StartEndModel):
    TYPES = [
        ('pro', 'Professional'),
        ('tec', 'Technical'),
        ('hon', 'Honor'),
        ('oth', 'Other'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    org_name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=3,
        choices=TYPES
    )
    officer = models.BooleanField()
