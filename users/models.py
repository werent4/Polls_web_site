from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_slug
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Username",
        max_length=150,
        unique=True,
        validators=[validate_slug],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(verbose_name='E-mail', blank=True, unique=True, null=True)
    email_checked = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        #return '%s (%s)' % (self.get_full_name(), self.email)
        return '%s (%s)' % (self.username, self.email)