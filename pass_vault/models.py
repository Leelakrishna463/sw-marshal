""" Models for pass_vault """
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from sw_marshal.env_handler import ENV_VAR

class Application(models.Model):
    """
    Application model which represents different apps for which pass_vault works
    """
    APP_TYPES = [
        ("WEB", "Web"),
        ("MBE", "Mobile"),
        ("DTP", "Desktop")
    ]
    title = models.CharField(
        primary_key=True,
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the app"
    )
    logo = models.ImageField(
        blank=True,
        upload_to=ENV_VAR['PW_APP_LOGO_PATH'],
    )
    type = models.CharField(max_length=3, choices=APP_TYPES, default=APP_TYPES[0][0])
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def logo_img(self):
        """ Display Logo Image in Django Admin"""
        src = getattr(self, 'logo', "")
        alt = getattr(self, 'alt', f"{self.title} logo")
        return mark_safe(
            f'<img src="{src}" alt="{alt}" style="width: 30px; height:30px;" />'
        )

    logo_img.short_description = 'Logo Thumbnail'

    def __str__(self):
        return f"{self.title}"


class PasswordAbstract(models.Model):
    """ Abstract model for Password """
    PASSWORD_TYPES = [
        ("PK", "Pass Key"),
        ("MF", "Multi Factor"),
        ("BM", "BioMetric"),
        ("TB", "Token Based")
    ]

    app = models.ForeignKey(to=Application, on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='+'
    )
    username = models.CharField(max_length=255)
    password = models.TextField()
    type = models.CharField(max_length=2, choices=PASSWORD_TYPES)

    class Meta:
        """ Meta class """
        abstract = True

    @staticmethod
    def get_field_names():
        """ Helper method to get fields of model """
        PRIVATE_FIELDS = ['id']
        return [field.name for field in filter(
            lambda field: field.name not in PRIVATE_FIELDS,
            PasswordHistory._meta.get_fields())
        ]


class Password(PasswordAbstract):
    """ Password model that stores current password and its information """
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.app} credentials-{self.username}"

    class Meta:
        "Meta class"
        unique_together = ('app', 'password')


class PasswordHistory(PasswordAbstract):
    """ Password History model that stores all passwords """
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta class """
        verbose_name = "Password History"
        verbose_name_plural = "Password Histories"
