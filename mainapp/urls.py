from django.conf.urls import url
from views import HomeView, EmailSendView


urlpatterns = [
	url(r"email_send/", EmailSendView.as_view(), name="email_send_url"),
	url(r"", HomeView.as_view(), name="home_url"),
]