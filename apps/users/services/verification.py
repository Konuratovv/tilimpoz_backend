from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from ..models import CustomUser