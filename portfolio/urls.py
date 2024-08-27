from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('home_page/', views.home_page, name='home'),
    path('home/', views.home_page, name='home'),
    path('contact_me', views.contact_me, name='contact_me'),
    path('project/<int:id>', views.project, name='project'),

]