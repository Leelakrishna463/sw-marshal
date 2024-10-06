""" urls for PassVault """
from rest_framework import routers
from pass_vault.views import PasswordViewSet

passvault_default_router = routers.DefaultRouter()
passvault_default_router.register(r'passwords', PasswordViewSet)

passvault_url_patterns = passvault_default_router.urls
