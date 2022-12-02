# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, View 
from django.shortcuts import redirect
from mainapp.models import Subscriber, TemplateName, SentEmailList
from mainapp.tasks import send_mass_mail_celery


class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['subscribers_list'] = Subscriber.objects.all()
		context['template_names'] = TemplateName.objects.all()
		context['email_sent_list'] = SentEmailList.objects.all().select_related("subscriber", "template_name")
		return context
	


class EmailSendView(View):
	def post(self, request):
		subscriber_list = request.POST.getlist('subscriber_list')
		template_name = request.POST.get('template_name')
		notes = request.POST.get('notes')
		send_mass_mail_celery(subscriber_list, template_name, notes)
		return redirect('home_url')