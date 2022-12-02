from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mass_mail
from django.conf import settings
from django.template import loader


@shared_task
def send_mass_mail_celery(subscriber_list, template_name, notes):
    message_1 = ('Title 1',
            'This is an email body 1',
            settings.EMAIL_HOST_USER,
            ['test.mail.87@bk.ru'])
    message_2 = ('Title 2',
            'This is an email body 2',
            settings.EMAIL_HOST_USER,
            ['bexruzmuminov@bk.ru'])
    send_mass_mail((message_1, message_2), fail_silently=False)
    return