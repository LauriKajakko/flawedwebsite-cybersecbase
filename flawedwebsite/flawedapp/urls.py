from django.urls import path

from .views import homePageView, addView, noteView, searchView, add2View, note2View, userView, unsafequery
urlpatterns = [
    path('', homePageView, name='home'),
    path('index', noteView, name='index'),
    path('indexcopy', note2View, name='indexcopy'),
    path('add', addView, name='add'),
    path('add2', add2View, name='add2'),
    path('search', searchView, name='search'),
    path('userview', userView, name='userview'),
    path('unsafequery', unsafequery, name='unsafequery')
]
