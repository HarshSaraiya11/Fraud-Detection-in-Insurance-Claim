from django.urls import path

from ananta_insurance import views

urlpatterns = [
    path('claim_form', views.claim_form, name='claim_form'),
    path('success', views.success, name='success'),
]