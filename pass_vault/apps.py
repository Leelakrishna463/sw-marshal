from django.apps import AppConfig


class PassVaultConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pass_vault'

    def ready(self) -> None:
        import pass_vault.signals
