# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.generic.views import TemplateView


class HomeView(TemplateView):
	template_name = "home.html"

