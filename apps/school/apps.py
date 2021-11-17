from django.apps import AppConfig


class SchoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #TODO
    """
try changing this:
    class ContactConfig(AppConfig): name = "contact"
to this:
    class ContactConfig(AppConfig): name = "apps.contact"
    """
    name = 'apps.school'
