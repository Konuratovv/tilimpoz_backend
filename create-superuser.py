from apps.users.models import CustomUser

SUPERUSER_EMAIL = 'admin@admin.com'
SUPERUSER_PASSWORD = '1'

def create_superuser():
    if CustomUser.objects.filter(email=SUPERUSER_EMAIL).exists():
        print('Superuser already exists.')
    else:
        CustomUser.objects.create_superuser(email=SUPERUSER_EMAIL, password=SUPERUSER_PASSWORD)
        print('Superuser created.')


create_superuser()