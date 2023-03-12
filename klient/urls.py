from django.urls import path
from . import views
from .views import LoginPage,IndexListView,IndexSearchedListView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',LoginPage.as_view(),name='login'),
    path('index/', IndexListView.as_view(template_name='klient/index.html'), name='index'),
    path('add/', views.add, name='add'),
    path('search/', IndexSearchedListView.as_view(), name='search'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('logout/',LogoutView.as_view(),name='logout')
]