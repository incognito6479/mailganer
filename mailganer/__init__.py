from __future__ import absolute_import, unicode_literals

import sys

sys.dont_write_bytecode = True

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)