import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shezhire.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = "admin"          # ← если не уверен, см. шаг ниже
NEW_PASSWORD = "Admin12345" # ← задай СВОЙ новый пароль

try:
    user = User.objects.get(username=USERNAME)
    user.set_password(NEW_PASSWORD)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("✅ Пароль администратора обновлён")
except User.DoesNotExist:
    User.objects.create_superuser(
        username=USERNAME,
        password=NEW_PASSWORD,
        email="admin@example.com"
    )
    print("✅ Суперпользователь создан")
