""" Views for Pass Vault """
from rest_framework import viewsets
from pass_vault.models import Password
from pass_vault.serializers import PasswordSerializer


class PasswordViewSet(viewsets.ModelViewSet):
    """ ViewSet for Passwords """
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
