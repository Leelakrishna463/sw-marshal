"""
Register PassVault Models in Django Admin
"""
from django.contrib import admin
from pass_vault.models import Application, Password, PasswordHistory

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """ Admin for Application Model """
    list_display = ['title', 'logo_img', 'url']
    ordering = ['title']


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    """ Admin for Password Model """
    list_display = ['app', 'user', 'username', 'password', 'type']
    ordering = ['app']


@admin.register(PasswordHistory)
class PasswordHistoryAdmin(admin.ModelAdmin):
    """ Admin for PasswordHistory """
    list_display = ['app', 'user', 'username', 'password', 'type']
    ordering = ['app']
