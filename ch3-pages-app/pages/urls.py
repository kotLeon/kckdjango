from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import AboutPageView, HomePageView, PostyPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
	path('posty/', PostyPageView.as_view(), name='posty'),
]
