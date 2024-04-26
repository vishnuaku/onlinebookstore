# settings.py

# Import the AppConfig class
from django.apps import AppConfig

# Define your AppConfig classes
class BooksConfig(AppConfig):
    name = 'books'

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Set the default_auto_field

# Set the DEFAULT_AUTO_FIELD setting
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
