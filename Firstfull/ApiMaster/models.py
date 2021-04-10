from django.contrib.auth.models import AbstractUser
from django.db import models
from paranoid_model.models import Paranoid

# from services.curr_user import add_user

TITLE = (
    ("Mr", "Mr"),
    ("Mrs", "Mrs")
)

QUALITY = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)


class UserProfile(AbstractUser):
    title = models.CharField(max_length=10, null=True, choices=TITLE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    mobile_no = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(max_length=25, null=True, unique=True)
    email_id = models.EmailField('email address', null=True, unique=True)
    date_of_birth = models.DateTimeField(null=True)
    occupation = models.CharField(max_length=20, null=True)
    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class Crop(Paranoid):
    name_of_crop = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=5, null=True, blank=True)
    quantity = models.CharField(max_length=2)
    qaulity = models.CharField(max_length=10, choices=QUALITY, default=None)
    date_of_import = models.DateField(null=True, blank=True)
    date_before_used = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name_of_crop


"""    def save(self, *args, **kwargs):
        add_user(self)
        super(Crop, self).save(*args, **kwargs)
"""
