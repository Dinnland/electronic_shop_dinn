from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Создание учетной записи администратора django"""
        user = User.objects.create(
            email='dinn.land@mail.ru',
            first_name='Admin',
            last_name='God',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123456789')
        user.save()
