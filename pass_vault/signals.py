""" Signals for Pass Vault App"""
from pass_vault.models import Password, PasswordHistory
from django.db.models.signals import post_save


def create_password_history(sender, **kwargs) -> None:
    """ Signal utility for creating password history when password is updated """
    password_history = {}
    for field in PasswordHistory.get_field_names():
        password_history.update({
            field: getattr(kwargs['instance'], field)
        })
    PasswordHistory.objects.create(**password_history)

post_save.connect(
    receiver=create_password_history,
    sender=Password,
    dispatch_uid="create_password_history"
)
