import yaml
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

User = get_user_model()


DEFAULT_GROUPS = [
    {'id': 1, 'name': 'admin'},
    {'id': 2, 'name': 'user'}
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        # init default groups
        for i, item in enumerate(DEFAULT_GROUPS):
            group, created = Group.objects.update_or_create(defaults=item, id=item['id'])
            if created:
                self.stdout.write(
                    '  Creating group "%(name)s"... ' % item + self.style.SUCCESS('OK')
                )
        self.stdout.write('  Default groups initialization done.')
