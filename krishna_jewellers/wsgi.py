import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krishna_jewellers.settings')

# This is the critical WSGI application variable
application = get_wsgi_application() 
