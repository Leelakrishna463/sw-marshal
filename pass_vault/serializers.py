""" Serializers for PassVault App"""
from rest_framework import serializers
from pass_vault.views import Password

class PasswordSerializer(serializers.ModelSerializer):
    """ Serializer for Password Viewset """
    class Meta:
        """ Meta class """
        fields = '__all__'
        model = Password
