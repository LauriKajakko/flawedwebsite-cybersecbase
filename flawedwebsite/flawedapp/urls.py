from django.urls import path

from .views import homePageView, addView, noteView

urlpatterns = [
    path('', homePageView, name='home'),
    path('index', noteView, name='index'),
    path('add', addView, name='add')
]
