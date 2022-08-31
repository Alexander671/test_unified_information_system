#!/usr/bin/env python

def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'accrual',
        ],
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
        }
    }
    )
    django.setup()
    DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()