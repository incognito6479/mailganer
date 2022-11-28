# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, View 
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings


class HomeView(TemplateView):
	template_name = "home.html"


class EmailSendView(View):
	def post(self, request):
		subscriber_list = request.POST.get('subscriber_list')
		template_name = request.POST.get('template_name')
		notes = request.POST.get('notes')
		send_mail(str(template_name),
				 'This is an email body',
				 settings.EMAIL_HOST_USER,
				 ['test.mail.87@bk.ru', 'bexruzmuminov@bk.ru'])
		return redirect('home_url')