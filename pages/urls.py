from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
]