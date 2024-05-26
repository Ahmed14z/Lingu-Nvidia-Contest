from django.urls import path
from .views import chatbot_view, money_manager_view

urlpatterns = [
    path('', chatbot_view, name='chatbot_view'),
    path('money-manager/', money_manager_view, name='money_manager'),
]
