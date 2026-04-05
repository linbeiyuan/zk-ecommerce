#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
    # 跳过 MySQL 版本检查，兼容 MySQL 5.7
    from django.db.backends.mysql.base import DatabaseWrapper
    DatabaseWrapper.data_types = DatabaseWrapper.data_types
    import django.db.backends.mysql.base as mysql_base
    mysql_base.Database = mysql_base.Database
    try:
        import django.db.backends.base.base as base
        original = base.BaseDatabaseWrapper.check_database_version_supported
        base.BaseDatabaseWrapper.check_database_version_supported = lambda self: None
    except Exception:
        pass
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
