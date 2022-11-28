# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
    """Model definition for Subscriber."""

    name = models.CharField(max_length=256)
    surename = models.CharField(max_length=256)
    birth_date = models.DateField()
    email = models.CharField(max_length=256, unique=True)

    class Meta:
        """Meta definition for Subscribers."""

        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        """Unicode representation of Subscriber."""
        return "{0} {1}".format(self.name, self.surename)


class TemplateName(models.Model):
    """Model definition for TemplateName."""

    display_name = models.CharField(max_length=256)
    template_name = models.CharField(max_length=256)

    class Meta:
        """Meta definition for TemplateName."""

        verbose_name = 'TemplateName'
        verbose_name_plural = 'TemplateName'

    def __str__(self):
        """Unicode representation of TemplateName."""
        return "{0} {1}".format(self.display_name, self.template_name)


class SentEmailList(models.Model): 
    """Model definition for SentEmailList."""
    date = models.DateTimeField(auto_now_add=True)
    subscriber = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    template_name = models.ForeignKey('TemplateName', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for SentEmailList."""

        verbose_name = 'SentEmailList'
        verbose_name_plural = 'SentEmailLists'

    def __str__(self):
        """Unicode representation of SentEmailList."""
        return "{0} {1}".format(self.display_name, self.template_name)