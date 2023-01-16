from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('about', views.about, name='about'),
    path('login', views.handleLogin, name='handleLogin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.handlelogout, name='handlelogout')
]